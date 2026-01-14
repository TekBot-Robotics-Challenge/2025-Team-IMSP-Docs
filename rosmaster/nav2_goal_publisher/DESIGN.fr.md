# nav2_goal_publisher – Conception et justification

Ce document décrit l’implémentation du paquet `nav2_goal_publisher` et justifie les principaux choix techniques. L’objectif est d’envoyer un unique goal Nav2 (`NavigateToPose`) de manière fiable, simple à intégrer et facilement extensible.

## Objectifs

- Fournir un nœud léger (peu de dépendances) qui envoie un goal Nav2 de façon fiable.
- Rendre la définition du goal ergonomique via des paramètres et des arguments de lancement (launch).
- Rester idiomatique ROS 2 Humble avec des points d’extension clairs.

## Structure du paquet

```
nav2_goal_publisher/
  package.xml                 # métadonnées ament_python & dépendances runtime
  setup.py                    # packaging, point d’entrée console_scripts
  setup.cfg                   # emplacements d’installation des scripts
  resource/
    nav2_goal_publisher       # requis par l’index ament
  launch/
    send_goal.launch.py       # lancement paramétrable du nœud
  nav2_goal_publisher/
    __init__.py
    send_goal_node.py         # rclpy ActionClient vers NavigateToPose
  README.md                   # usage rapide
  DESIGN.md                   # document en anglais
  DESIGN.fr.md                # ce document (version française)
```

## Pourquoi Python et `ament_python`

- Simplicité et rapidité : pour un simple client d’action sans calcul lourd, Python (`rclpy`) évite la complexité de la chaîne C++.
- Itération rapide : pas de cycle compile/édition/lien ; idéal pour les tests et la mise au point.
- Schéma standard ROS 2 : les nœuds Python sont de première classe et s’intègrent nativement à `colcon` et à l’index ament via `ament_python`.

Alternatives envisagées :
- `rclcpp` + `ament_cmake` : mise en place plus lourde pour peu de gain dans ce cas.
- Utilitaire CLI seul (`ros2 action send_goal`) : pratique ponctuellement mais moins composable/paramétrable qu’un nœud incluable dans des fichiers launch.

## Dépendances et justification

- `rclpy` : bibliothèque cliente ROS 2 Python pour créer le nœud et gérer l’action.
- `nav2_msgs` : définit l’action `NavigateToPose`.
- `geometry_msgs` : porteuse du `PoseStamped` du goal.
- `launch`, `launch_ros` : exposition propre des paramètres côté CLI/launch.
- `python3-yaml` : parseur YAML au runtime pour charger des séquences de goals depuis un fichier.

Ces dépendances sont déclarées en `exec_depend` dans `package.xml` car ce paquet est 100 % Python (dépendances runtime).

## Conception du nœud

Fichier : `nav2_goal_publisher/send_goal_node.py`

- Nom du nœud : `nav2_goal_publisher` (descriptif et cohérent avec le nom du paquet).
- Action : `navigate_to_pose` via `ActionClient(NavigateToPose)`.
- Paramètres (avec valeurs par défaut) :
  - `goal_x` (float, défaut 0.0)
  - `goal_y` (float, défaut 0.0)
  - `goal_yaw` (float, radians, défaut 0.0)
  - `frame_id` (string, défaut `map`)
  - `auto_send` (bool, défaut `True`)
  - `goals_yaml` (string, défaut "") : chemin absolu ou relatif vers un fichier YAML contenant une liste de goals
  - `halt_on_failure` (bool, défaut `False`) : si vrai, stoppe la séquence YAML en cas de rejet/échec

### Attente du serveur d’action : timer one-shot

- Stratégie : création d’un timer périodique court (200 ms) qui appelle `wait_for_server(timeout_sec=0.1)` et envoie le goal dès que le serveur est prêt.
- Pourquoi un timer et pas un `wait` bloquant ? Le timer garde le nœud réactif et évite de bloquer l’exécuteur avant la disponibilité du serveur ; c’est idiomatique avec rclpy pour un comportement one-shot au démarrage.

### Construction de la pose du goal

- Orientation réduite au lacet (yaw) pour simplifier l’interface :
  - $q_z = \sin(\text{yaw}/2)$, $q_w = \cos(\text{yaw}/2)$.
- L’en-tête utilise `frame_id` (par défaut `map`) et l’horodatage courant du nœud.

### Rétroaction (feedback) et résultat

- Feedback : journalise une ligne concise (p.ex. `distance_remaining`) pour éviter le bruit, tout en restant informatif.
- Résultat : en fin d’action (ou en cas de rejet), le nœud journalise l’issue.
  - Mode single-goal : appelle `rclpy.shutdown()` et se termine.
  - Séquence YAML : passe au goal suivant ; si `halt_on_failure` est vrai et qu’un échec/rejet survient, le nœud s’arrête immédiatement.

### Cas d’erreur et bords gérés

- Serveur d’action non prêt : le timer affiche un message d’attente et réessaie jusqu’à disponibilité.
- Rejet : journalise un avertissement et s’arrête ; pas de réessai par défaut (comportement prévisible).
- Frames/TF invalides : hors du périmètre de ce nœud ; Nav2 signalera les erreurs de transform/navigation.
- Goal inatteignable : le résultat reflètera l’échec ; le nœud se termine néanmoins proprement.

## Conception du lancement (launch)

Fichier : `launch/send_goal.launch.py`

- Expose des arguments (`goal_x`, `goal_y`, `goal_yaw`, `frame_id`, `goals_yaml`, `halt_on_failure`) mappés aux paramètres du nœud, ce qui permet :
  - les surcharges en ligne de commande (`ros2 launch ... goal_x:=2.0 ...`),
  - la réutilisation dans des descriptions launch de plus haut niveau.
- Exécute le script console `send_goal` du paquet installé (pas de chemins Python codés en dur).
- `output='screen'` : visibilité directe du feedback et du résultat.

### Support des goals en YAML

- Schéma YAML (minimal) :

  ```yaml
  goals:
    - { x: 2.0, y: 1.0, yaw: 1.57, frame_id: map }
    - { x: 0.0, y: 0.0, yaw: 0.0 }  # frame_id par défaut : paramètre du nœud
  ```

- Validation : les entrées non-dictionnaires ou incomplètes sont ignorées avec avertissements.
- Sémantique temporelle : chaque goal utilise l’horodatage courant du nœud au moment de l’envoi.
- Disponibilité du serveur : même attente via timer avant l’envoi du premier goal.

## Détails de packaging et justification

- `setup.py` :
  - `entry_points.console_scripts` : enregistre `send_goal` pour `ros2 run nav2_goal_publisher send_goal`.
  - `data_files` : installe `package.xml` et le répertoire `launch/` sous `share/` pour que `ros2 launch` découvre le fichier.
  - Suppression de `tests_require` (déprécié ; setuptools moderne le signale et l’ignore).
- `setup.cfg` :
  - garantit l’installation des scripts console dans `$base/lib/<package>`, conforme aux attentes ROS 2.
- `resource/nav2_goal_publisher` :
  - requis par ament pour l’indexation du paquet (sinon la découverte échoue).
- `package.xml` :
  - déclare le type de build `ament_python` (full Python) et les dépendances runtime nécessaires.

## Résumé du contrat (I/O)

- Entrées :
  - Paramètres : `goal_x`, `goal_y`, `goal_yaw` (rad), `frame_id` (string), `auto_send` (bool), `goals_yaml` (chemin), `halt_on_failure` (bool)
  - Nav2 doit être lancé et fournir le serveur d’action `navigate_to_pose`.
- Sorties :
  - Mode single-goal : envoie un goal `NavigateToPose` puis se termine.
  - Mode YAML : envoie N goals dans l’ordre ; se termine après le dernier goal ou immédiatement en cas d’échec si `halt_on_failure=true`.
- Critères de succès :
  - Goal accepté ; le nœud reporte le résultat (succès/échec) et se termine proprement.

## Extensibilité

- Listes de goals / waypoints : itérer sur une liste (YAML, paramètres array) et envoyer séquentiellement.
- Support degrés : ajouter un paramètre `goal_yaw_deg` (exclusif avec `goal_yaw`).
- Quaternion complet : permettre une orientation $(x,y,z,w)$ fournie et validée.
- Timeouts/réessais : paramètres pour le temps d’attente serveur et la politique de réessai.
- Namespacing : prise en charge de `--ros-args --remap navigate_to_pose:=<ns>/navigate_to_pose` pour multi-robots.

## Stratégie de tests (suggestion)

- Unitaire : factoriser le calcul du quaternion dans un utilitaire et tester quelques angles.
- Intégration : en simulation (Gazebo/Nav2 bringup), vérifier acceptation et complétion du goal atteignable.
- Statique : `flake8`/`ruff` pour le style ; effort minime adapté à la petite taille du projet.

## Notes opérationnelles

- Performance : empreinte CPU/mémoire négligeable ; le nœud s’exécute brièvement et sort.
- Journalisation : niveau info par défaut ; passer en debug pour plus de verbosité.
- Sécurité : pas d’accès réseau externe ; dépend de la connectivité ROS.

## Alternatives étudiées

- `ros2 action send_goal` (CLI) : très pratique à la main, mais moins composable/paramétrable dans des launch.
- `nav2_simple_commander` (API Python) : plus haut niveau, mais ajoute une dépendance et masque le pattern client d’action de base.
- C++ (`rclcpp`) : pertinent pour des systèmes plus grands, mais complexifie inutilement ce cas simple.

## Utilisation rapide

Voir `README.md` pour les exemples build/run. Lancement typique :

```bash
ros2 launch nav2_goal_publisher send_goal.launch.py \
  goal_x:=2.0 goal_y:=1.0 goal_yaw:=1.57 frame_id:=map
```
