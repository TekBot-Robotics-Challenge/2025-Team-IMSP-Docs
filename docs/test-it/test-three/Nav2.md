# Nav2

## **Qu'est-ce que Nav2 ?**

Nav2 (Navigation2) représente la stack de navigation ROS 2 la plus avancée, conçue avec une architecture modulaire et optimisée pour des déploiements en environnement de production. Développée comme successeur de la navigation ROS 1, cette plateforme complète offre un ensemble de fonctionnalités sophistiquées permettant aux robots mobiles autonomes de naviguer efficacement dans des environnements complexes. Elle permet aux robots mobiles de :

- Localiser leur position avec précision dans un environnement donné (que ce soit via une approche SLAM dynamique ou en utilisant une carte statique préétablie)
- Planifier un chemin optimal et sécurisé d'un point A à un point B, en tenant compte des contraintes géométriques et cinématiques du robot
- Exécuter ce chemin planifié en temps réel tout en détectant et évitant dynamiquement les obstacles statiques et mobiles qui pourraient apparaître
- Gérer intelligemment des stratégies de reprises automatiques en cas d'échec ou de blocage (recovery behaviors) pour assurer la robustesse de la navigation

## **Principes clés & vocabulaire**

- **Behavior Tree (BT)** : graphe hiérarchique qui orchestre les différentes étapes de navigation (planification, suivi, récupérations).
- **Lifecycle Nodes** : chaque module (planner, controller, costmap, etc.) passe par des états (unconfigured → inactive → active) pour un démarrage/arrêt propre.
- **Costmaps** :
    - *Global Costmap* (statique) pour la planification à grande échelle
    - *Local Costmap* (dynamique) pour la commande en temps réel
- **Planner Server** : calcule un chemin (ROS 2 Action `ComputePathToPose`)
- **Controller Server** : suit le chemin généré (ROS 2 Action `FollowPath`)
- **Recovery Behaviors** : actions automatiques (spin, recul, clear costmaps) déclenchées si le robot bute ou se perd
- **TF** : arbres de transformations (REP-105) nécessaires pour passer d'un repère à un autre

## **Comment fonctionne Nav2 ?**

1. **Sourcing & TF :**
    - Vous sourcez `/opt/ros/humble/setup.bash` et votre workspace
    - Les frames TF (odom → base_link, map → odom…) sont publiées
2. **Chargement de la carte :**
    - Carte statique via `map_server` ou flux SLAM (`slam_toolbox`)
3. **Behavior Tree :**
    - Le fichier XML BT définit l'ordre des actions (planifier, suivre, récupérer)
4. **ROS 2 Actions :**
    - Le BT envoie des requêtes au Planner Server et au Controller Server
    - Chaque serveur renvoie son état (`RUNNING`, `SUCCESS`, `FAILURE`)
5. **Publication de commandes :**
    - Nav2 publie sur `/cmd_vel` les vitesses linéaires et angulaires adaptées à la cinématique
6. **Surveillance et récupérations :**
    - En cas d'obstacle bloquant, Nav2 déclenche automatiquement un recovery behavior

## **Installation**

> Avant de commencer, il est essentiel de vous assurer que vous avez correctement installé ROS2 dans sa version Humble sur votre système. Cette étape préliminaire est cruciale pour permettre l'installation de Nav2. Si vous n'avez pas encore installé ROS2 Humble ou si vous rencontrez des difficultés avec votre installation actuelle, veuillez [voir plus](../test-two/installation-ros2-humble.md) pour obtenir des instructions détaillées sur la procédure d'installation.
> 

Ouvrez un terminal, sourcez ROS 2 puis installez Nav2 et les bringup packages :

```bash
source /opt/ros/humble/setup.bash
sudo apt update
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup

```

Ensuite, dans votre workspace (par ex. `~/tekbot_ws`) :

```bash
source install/setup.bash
ros2 launch nav2_bringup navigation_launch.py use_sim_time:=true map:=/path/to/your/map.yaml

```