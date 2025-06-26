# RViz2

## Qu’est-ce que `RViz2` ?

**`RViz`** est un outil fondamental et incontournable dans l'écosystème ROS/ROS2, spécialement conçu pour permettre la visualisation en temps réel de l'ensemble des données et de l'état complet d'un robot, qu'il évolue dans un environnement virtuel simulé ou dans le monde physique réel. Cette interface graphique sophistiquée offre aux développeurs et aux utilisateurs une représentation visuelle intuitive et interactive des informations critiques du système robotique. Voici une présentation détaillée et structurée de ses nombreuses fonctionnalités avancées et de son utilisation spécifique dans le cadre du projet Tekbot :

## **Fonction :**

Visualiseur 3D complet et polyvalent pour l'écosystème ROS/ROS2. Cette interface graphique riche permet d'afficher et d'interpréter en temps réel une multitude d'éléments et de données robotiques, notamment :

- **Cartes** : Représentation détaillée et précise de l'environnement générée par les algorithmes SLAM, permettant au robot de comprendre la géométrie de son espace de navigation.
- **Nuages de points** : Visualisation tridimensionnelle des données brutes et traitées provenant des capteurs de perception comme le LIDAR, offrant une représentation spatiale de l'environnement détecté.
- **Trajectoires** : Affichage graphique des chemins planifiés ou effectivement suivis par le robot lors de ses déplacements, permettant d'analyser et d'optimiser ses mouvements dans l'espace.
- **Frames TF** : Représentation visuelle des transformations géométriques entre les différentes parties et composants du robot, essentielles pour comprendre les relations spatiales entre ses éléments constitutifs.
- **Scans laser** : Interprétation graphique des données brutes issues des capteurs laser, offrant une vue immédiate des obstacles et surfaces détectés dans l'environnement du robot.

## Installation de `RViz2`

> Avant de commencer, il est essentiel de vous assurer que vous avez correctement installé ROS2 dans sa version Humble sur votre système. Cette étape préliminaire est cruciale pour permettre l'installation de RViz2. Si vous n'avez pas encore installé ROS2 Humble ou si vous rencontrez des difficultés avec votre installation actuelle, veuillez [voir plus](../test-two/installation-ros2-humble.md) pour obtenir des instructions détaillées sur la procédure d'installation.
> 

## Installation

RViz 2 est inclus dans la distribution « desktop » de ROS 2. Pour l’installer seul :

```bash
sudo apt update
sudo apt install ros-humble-rviz2
```

Ou, si vous partez de zéro, installez toute la desktop :

```bash
sudo apt install ros-humble-desktop
```
```

## Vérifier l’installation de Rviz2

Lancez RViz 2 pour tester :

```bash
rviz2
```

La fenêtre 3D de RViz devrait s’ouvrir en affichant la vue par défaut