# Création du package ROS2

Dans le cadre du test ROS2, un **package** nommé **`sensor_data_evaluation`** a été créé.

### Étapes de création du package

Après s’être placé dans le dossier `src` du workspace `Test2_IT_TRC`, la commande suivante a été utilisée pour créer le package :

```bash

cd ~/test-02/src
ros2 pkg create --build-type ament_cmake sensor_data_evaluation --dependencies rclcpp std_msgs
```

Cette commande a pour effet de :

- Créer un dossier `sensor_data_evaluation/` avec la structure standard d’un package ROS2.
- Générer automatiquement les fichiers `CMakeLists.txt` et `package.xml`.
- Préparer un environnement compatible avec le système de build **`ament_cmake`**.
- Déclarer les dépendances minimales nécessaires (`rclcpp` pour les fonctionnalités de ROS2 en C++, et `std_msgs` pour l’utilisation des messages standards).

### Structure initiale du package

À la création, le package contient les éléments suivants :

```bash

sensor_data_evaluation/
├── CMakeLists.txt     # Fichier de configuration pour la compilation avec CMake
├── package.xml        # Métadonnées du package (nom, version, dépendances…)
└── src/               # Répertoire source pour ajouter les fichiers .cpp ou .py

```