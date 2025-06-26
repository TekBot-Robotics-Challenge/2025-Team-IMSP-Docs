# SLAM & SLAM_TOOLBOX

## Qu'est-ce que SLAM ?

Le SLAM(*Simultaneous Localization And Mapping)* à est une technique en robotique qui permet à un robot de construire une carte de son environnement tout en déterminant sa propre position dans celui-ci. Le principe du SLAM repose sur un défi circulaire : pour créer une carte fiable, le robot doit connaître sa position exacte, mais pour se localiser précisément, il a besoin d'une carte de référence. Cette approche est largement utilisée dans divers domaines tels que la navigation autonome des robots mobiles, les véhicules autonomes, les drones (UAV), la réalité augmentée ainsi que la cartographie d’intérieur, où elle permet une exploration et une interaction efficaces avec des environnements inconnus ou complexes.

### Types de capteurs utilisés

- **LiDAR** : Capteurs laser qui mesurent les distances
- **Caméras** : Vision monoculaire ou stéréoscopique
- **Capteurs RGB-D** : Combinant couleur et profondeur
- **IMU** : Unités de mesure inertielle pour l'odométrie

## Introduction à slam_toolbox

Pour mettre en œuvre le SLAM dans un système robotique sous ROS 2, plusieurs outils sont disponibles. Parmi eux, `slam_toolbox`  un package ROS 2 qui permet de réaliser la localisation et la cartographie simultanées. Il offre la création et l’optimisation de cartes en temps réel ou en mode hors ligne. Il est plus récent que `gmapping` et compatible avec ROS 2.

Ce package utilise des algorithmes optimisés pour les systèmes embarqués, propose des modes de fonctionnement synchrones ou asynchrones, et permet la sauvegarde et le chargement des cartes. Il inclut aussi un plugin RViz pour la visualisation.

Au niveau algorithmique, `slam_toolbox` s’appuie sur Karto SLAM, intègre la détection et la correction des boucles (*loop closure*), et réalise une optimisation de graphe pour ajuster la carte et la trajectoire, minimisant ainsi les erreurs.

## Installation

> Avant de commencer, il est essentiel de vous assurer que vous avez correctement installé ROS2 dans sa version Humble sur votre système. Cette étape préliminaire est cruciale pour permettre l'installation de SLAM_toolbox. Si vous n'avez pas encore installé ROS2 Humble ou si vous rencontrez des difficultés avec votre installation actuelle, veuillez [voir plus](../test-two/installation-ros2-humble.md) pour obtenir des instructions détaillées sur la procédure d'installation.
> 

### Installation via apt (recommandée)

```bash
sudo apt install ros-humble-slam-toolbox
```

### Compilation depuis les sources

```bash
# Créer un workspace
mkdir -p ~/slam_ws/src
cd ~/slam_ws/src

# Cloner le dépôt
git clone <https://github.com/SteveMacenski/slam_toolbox.git>

# Installer les dépendances
cd ~/slam_ws
rosdep install --from-paths src --ignore-src -r -y

# Compiler
colcon build --packages-select slam_toolbox
source install/setup.bash
```

## Configuration

### Fichier de configuration de base

Créer un fichier `mapper_params_online_async.yaml` :

```yaml
slam_toolbox:
  ros__parameters:
    # Plugin params
    solver_plugin: solver_plugins::CeresSolver
    ceres_linear_solver: SPARSE_NORMAL_CHOLESKY
    ceres_preconditioner: SCHUR_JACOBI
    ceres_trust_strategy: LEVENBERG_MARQUARDT
    ceres_dogleg_type: TRADITIONAL_DOGLEG
    ceres_loss_function: None

    # ROS Parameters
    odom_frame: odom
    map_frame: map
    base_frame: base_footprint
    scan_topic: /scan
    mode: mapping # localization

    # Mapping params
    resolution: 0.05
    max_laser_range: 20.0
    minimum_time_interval: 0.5
    transform_publish_period: 0.02
    map_update_interval: 5.0
    enable_interactive_mode: true

    # General params
    use_scan_matching: true
    use_scan_barycenter: true
    minimum_travel_distance: 0.5
    minimum_travel_heading: 0.5
    scan_buffer_size: 10
    scan_buffer_maximum_scan_distance: 10.0
    link_match_minimum_response_fine: 0.1
    link_scan_maximum_distance: 1.5
    loop_search_maximum_distance: 3.0
    do_loop_closing: true
    loop_match_minimum_chain_size: 10
    loop_match_maximum_variance_coarse: 3.0
    loop_match_minimum_response_coarse: 0.35
    loop_match_minimum_response_fine: 0.45

    # Correlation params
    correlation_search_space_dimension: 0.5
    correlation_search_space_resolution: 0.01
    correlation_search_space_smear_deviation: 0.1

    # Loop closure params
    loop_search_space_dimension: 8.0
    loop_search_space_resolution: 0.05
    loop_search_space_smear_deviation: 0.03

    # Scan matcher params
    distance_variance_penalty: 0.5
    angle_variance_penalty: 1.0
    fine_search_angle_offset: 0.00349
    coarse_search_angle_offset: 0.349
    coarse_angle_resolution: 0.0349
    minimum_angle_penalty: 0.9
    minimum_distance_penalty: 0.5
    use_response_expansion: true

```

## Utilisation

### Mode mapping (cartographie)

```bash
# Lancer slam_toolbox en mode mapping
ros2 launch slam_toolbox online_async_launch.py \\
    params_file:=./mapper_params_online_async.yaml \\
    use_sim_time:=false
```

### Mode localization (localisation)

```bash
# Lancer slam_toolbox en mode localisation
ros2 launch slam_toolbox localization_launch.py \\
    map:=/path/to/your/map.yaml
```

### Avec un fichier launch personnalisé

Créer `my_slam_launch.py` :

```python
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_dir = get_package_share_directory('your_package')

    return LaunchDescription([
        DeclareLaunchArgument(
            'params_file',
            default_value=os.path.join(pkg_dir, 'config', 'mapper_params.yaml'),
            description='Chemin vers le fichier de paramètres'
        ),

        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[LaunchConfiguration('params_file')],
            remappings=[
                ('/scan', '/your_lidar_topic'),
                ('/tf', 'tf'),
                ('/tf_static', 'tf_static')
            ]
        )
    ])
```

## Paramètres principaux

### Paramètres de base

| Paramètre | Description | Valeur par défaut |
| --- | --- | --- |
| `resolution` | Résolution de la carte (m/pixel) | 0.05 |
| `max_laser_range` | Portée maximale du laser (m) | 20.0 |
| `minimum_time_interval` | Intervalle minimum entre les mises à jour (s) | 0.5 |
| `mode` | Mode de fonctionnement (`mapping` ou `localization`) | mapping |

### Paramètres de performance

| Paramètre | Description | Impact |
| --- | --- | --- |
| `scan_buffer_size` | Taille du buffer de scans | Mémoire vs précision |
| `map_update_interval` | Fréquence de mise à jour de la carte | Performance vs temps réel |
| `minimum_travel_distance` | Distance minimale pour déclencher une mise à jour | Précision vs charge CPU |

### Paramètres de loop closure

| Paramètre | Description | Recommandation |
| --- | --- | --- |
| `do_loop_closing` | Activer la détection de boucles | true pour la précision |
| `loop_search_maximum_distance` | Distance max de recherche de boucles | 3.0 pour environnements moyens |
| `loop_match_minimum_response_fine` | Seuil de validation des boucles | 0.45 pour éviter les faux positifs |

## Exemples pratiques

### Cartographie d'un bâtiment

```bash
# 1. Démarrer slam_toolbox
ros2 launch slam_toolbox online_async_launch.py

# 2. Démarrer la téléopération
ros2 run teleop_twist_keyboard teleop_twist_keyboard

# 3. Naviguer pour explorer l'environnement
# Utiliser les touches du clavier pour déplacer le robot

# 4. Sauvegarder la carte
ros2 service call /slam_toolbox/save_map slam_toolbox/srv/SaveMap \\
    "name: {data: '/home/user/maps/my_building'}"

```

### Optimisation de carte existante

```bash
# Charger une carte et l'optimiser
ros2 service call /slam_toolbox/deserialize_map slam_toolbox/srv/DeserializePoseGraph \\
    "filename: {data: '/home/user/maps/my_map'}"

# Déclencher l'optimisation
ros2 service call /slam_toolbox/manual_loop_closure slam_toolbox/srv/LoopClosure

```

## Interface RViz

### Plugin slam_toolbox

1. Ajouter le plugin dans RViz :
    - Panels → Add New Panel → slam_toolbox → SlamToolboxPlugin
2. Fonctionnalités disponibles :
    - **Save Map** : Sauvegarder la carte actuelle
    - **Load Map** : Charger une carte existante
    - **Clear Map** : Effacer la carte
    - **Loop Closure** : Forcer une fermeture de boucle

### Visualisation des données

```bash
# Lancer RViz avec configuration slam
ros2 run rviz2 rviz2 -d $(ros2 pkg prefix slam_toolbox)/share/slam_toolbox/rviz/slam_toolbox_default.rviz

```

Topics à ajouter dans RViz :

- `/map` : Carte générée
- `/scan` : Données laser
- `/slam_toolbox/scan_visualization` : Visualisation des scans utilisés
- `/slam_toolbox/graph_visualization` : Graphe de poses

## Services disponibles

### Services principaux

```bash
# Sauvegarder la carte
ros2 service call /slam_toolbox/save_map slam_toolbox/srv/SaveMap \\
    "name: {data: 'ma_carte'}"

# Charger une carte
ros2 service call /slam_toolbox/deserialize_map slam_toolbox/srv/DeserializePoseGraph \\
    "filename: {data: 'ma_carte'}"

# Effacer la carte
ros2 service call /slam_toolbox/clear_queue slam_toolbox/srv/Clear

# Mettre en pause/reprendre
ros2 service call /slam_toolbox/pause_new_measurements slam_toolbox/srv/Pause
ros2 service call /slam_toolbox/resume_new_measurements slam_toolbox/srv/Resume

```

### Services avancés

```bash
# Optimisation manuelle
ros2 service call /slam_toolbox/manual_loop_closure slam_toolbox/srv/LoopClosure

# Ajout de contraintes manuelles
ros2 service call /slam_toolbox/add_submap slam_toolbox/srv/AddSubmap

# Fusion de cartes
ros2 service call /slam_toolbox/merge_maps slam_toolbox/srv/MergeMaps

```

## Troubleshooting

### Problèmes courants

### 1. Carte déformée ou imprécise

**Symptômes** : La carte présente des déformations, des murs doublés
**Solutions** :

```yaml
# Réduire la sensibilité au mouvement
minimum_travel_distance: 0.3  # au lieu de 0.5
minimum_travel_heading: 0.3   # au lieu de 0.5

# Améliorer le scan matching
link_match_minimum_response_fine: 0.2  # au lieu de 0.1

```

### 2. Performance dégradée

**Symptômes** : CPU élevé, latence importante
**Solutions** :

```yaml
# Réduire la fréquence de mise à jour
map_update_interval: 10.0  # au lieu de 5.0
minimum_time_interval: 1.0  # au lieu de 0.5

# Limiter la recherche de boucles
loop_search_maximum_distance: 2.0  # au lieu de 3.0

```

### 3. Échecs de loop closure

**Symptômes** : Pas de fermeture de boucles détectées
**Solutions** :

```yaml
# Assouplir les contraintes
loop_match_minimum_response_coarse: 0.25  # au lieu de 0.35
loop_match_minimum_response_fine: 0.35    # au lieu de 0.45
loop_search_space_dimension: 10.0         # au lieu de 8.0

```

### 4. Problèmes de transformation

**Symptômes** : Erreurs de TF, robot "sautant"
**Solutions** :

```bash
# Vérifier les frames
ros2 run tf2_tools view_frames

# Vérifier la cohérence temporelle
ros2 topic echo /tf --field transforms[0].header.stamp

```

### 5. Problèmes spécifiques aux robots virtuels

**Symptômes** : SLAM ne fonctionne pas en simulation
**Solutions** :

```yaml
# Vérifier use_sim_time
use_sim_time: true

# Adapter les topics
scan_topic: /scan  # Vérifier le nom exact du topic LiDAR

# Réduire les seuils pour simulation
minimum_travel_distance: 0.1
transform_publish_period: 0.01

```

### Diagnostic

### Vérification des topics

```bash
# Lister les topics actifs
ros2 topic list | grep slam

# Vérifier la fréquence des messages
ros2 topic hz /scan
ros2 topic hz /map

# Examiner le contenu des messages
ros2 topic echo /slam_toolbox/feedback

```

### Logs et debug

```bash
# Activer les logs détaillés
ros2 launch slam_toolbox online_async_launch.py log_level:=debug

# Examiner les logs
ros2 log view slam_toolbox

```

### Optimisation selon l'environnement

### Environnements intérieurs (simulation)

```yaml
# Configuration optimisée pour intérieur virtuel
max_laser_range: 10.0
resolution: 0.025
minimum_travel_distance: 0.2
loop_search_maximum_distance: 5.0
use_sim_time: true

```

### Environnements extérieurs (simulation)

```yaml
# Configuration optimisée pour extérieur virtuel
max_laser_range: 30.0
resolution: 0.1
minimum_travel_distance: 1.0
minimum_travel_heading: 0.1
use_sim_time: true

```

### Environnements dynamiques (simulation)

```yaml
# Réduction de l'impact des objets mobiles
scan_buffer_size: 5
correlation_search_space_smear_deviation: 0.05
use_scan_barycenter: false
use_sim_time: true

```

## Intégration avec d'autres packages

### Navigation (nav2) pour ROS 2 Humble

```yaml
# Configuration pour nav2 avec robots virtuels
map_server:
  ros__parameters:
    use_sim_time: true
    yaml_filename: "ma_carte.yaml"

amcl:
  ros__parameters:
    use_sim_time: true
    # Désactiver AMCL si slam_toolbox est en mode localization

```

### Move Base / Navigation Stack pour robots virtuels

```python
# Launch file pour intégration complète avec ROS 2 Humble
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    # Paramètres
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    slam_params_file = LaunchConfiguration('slam_params_file')
    nav_params_file = LaunchConfiguration('nav_params_file')

    # Arguments
    slam_params_arg = DeclareLaunchArgument(
        'slam_params_file',
        default_value=PathJoinSubstitution([
            FindPackageShare('your_package'), 'config', 'slam_virtual.yaml'
        ]),
        description='Paramètres SLAM'
    )

    nav_params_arg = DeclareLaunchArgument(
        'nav_params_file',
        default_value=PathJoinSubstitution([
            FindPackageShare('your_package'), 'config', 'nav2_params.yaml'
        ]),
        description='Paramètres Nav2'
    )

    # SLAM Node
    slam_node = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[
            slam_params_file,
            {'use_sim_time': use_sim_time}
        ],
    )

    # Navigation Stack
    nav_bringup = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('nav2_bringup'),
                'launch',
                'navigation_launch.py'
            ])
        ]),
        launch_arguments={
            'use_sim_time': use_sim_time,
            'params_file': nav_params_file,
            'autostart': 'true',
        }.items()
    )

    return LaunchDescription([
        slam_params_arg,
        nav_params_arg,
        slam_node,
        nav_bringup,
    ])

```

### Intégration avec Gazebo et robots virtuels

### Configuration complète pour simulation

```python
# complete_simulation.launch.py
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    world_file = LaunchConfiguration('world_file')

    # Arguments
    world_arg = DeclareLaunchArgument(
        'world_file',
        default_value=PathJoinSubstitution([
            FindPackageShare('your_robot_package'), 'worlds', 'my_world.world'
        ]),
        description='Fichier monde Gazebo'
    )

    # Gazebo
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            ])
        ]),
        launch_arguments={
            'world': world_file,
            'use_sim_time': 'true',
        }.items()
    )

    # Robot spawn
    robot_spawn = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'my_robot'],
        output='screen'
    )

    # SLAM
    slam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('your_package'),
                'launch',
                'slam_virtual.launch.py'
            ])
        ]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # RViz
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', PathJoinSubstitution([
            FindPackageShare('your_package'), 'rviz', 'slam_config.rviz'
        ])],
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )

    return LaunchDescription([
        world_arg,
        gazebo_launch,
        robot_spawn,
        slam_launch,
        rviz_node,
    ])

```

## Guide pratique pour débutants

### Étapes pour démarrer avec slam_toolbox en simulation

### 1. Préparation de l'environnement

```bash
# Installer ROS 2 Humble et les dépendances
sudo apt update
sudo apt install ros-humble-desktop
sudo apt install ros-humble-slam-toolbox
sudo apt install ros-humble-navigation2
sudo apt install ros-humble-gazebo-ros-pkgs

# Sourcer l'environnement
source /opt/ros/humble/setup.bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

```

### 2. Test rapide avec TurtleBot3

```bash
# Installer TurtleBot3 (exemple de robot virtuel)
sudo apt install ros-humble-turtlebot3*

# Définir le modèle de robot
export TURTLEBOT3_MODEL=waffle
echo "export TURTLEBOT3_MODEL=waffle" >> ~/.bashrc

# Lancer la simulation
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

# Dans un nouveau terminal, lancer SLAM
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True

# Dans un troisième terminal, téléopération
ros2 run turtlebot3_teleop teleop_keyboard

```

### 3. Remplacer Cartographer par slam_toolbox

```bash
# Créer le fichier de configuration slam_toolbox pour TurtleBot3
mkdir -p ~/tb3_slam_config/config

# Créer le fichier YAML (utiliser la configuration virtuelle donnée plus haut)

# Lancer slam_toolbox
ros2 launch slam_toolbox online_async_launch.py \\
    slam_params_file:=~/tb3_slam_config/config/slam_virtual.yaml \\
    use_sim_time:=true

```