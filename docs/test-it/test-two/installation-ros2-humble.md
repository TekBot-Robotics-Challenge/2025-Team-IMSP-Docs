# Mise en place de l’environnement ROS2 Humble

Dans le cadre de ce test, l’environnement de développement a été préparé à partir d’une installation complète de **ROS2 Humble** sur un système **Ubuntu 22.04**. L'installation s’est faite en ligne de commande, en veillant à garantir la stabilité du système, la compatibilité avec UTF-8, et l’accès aux bibliothèques ROS via les dépôts officiels.

## Configuration de la locale système

Avant toute installation, la prise en charge de l’encodage **UTF-8** a été vérifiée et configurée. Cela est essentiel dans les environnements minimaux pour éviter tout problème avec les dépendances ou les outils ROS.

```bash
locale  # vérifier les paramètres locaux

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # confirmation
```

## Configuration des sources ROS2

La suite du processus consiste à configurer les sources APT de ROS2. Cela permet d’installer les paquets depuis les dépôts officiels et de recevoir les mises à jour automatiquement.

D’abord, il faut s’assurer que le dépôt *universe* d’Ubuntu est activé :

```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```

Ensuite, les clés de sécurité et le paquet `ros2-apt-source` sont installés. Ce dernier configure automatiquement les dépôts ROS2 :

```bash
sudo apt update && sudo apt install curl -y

export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F\" '{print $4}')
curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo $VERSION_CODENAME)_all.deb"
sudo apt install /tmp/ros2-apt-source.deb
```

### Installation de ROS2

Après la configuration des sources, les paquets système ont été mis à jour pour éviter tout conflit :

```bash
sudo apt update # (systemd)
sudo apt upgrade # (udev)
```

Puis l’installation de la version complète de ROS2 s’est faite via :

```bash
sudo apt install ros-humble-desktop
```

Cette version inclut le cœur de ROS2, les bibliothèques de communication, les outils graphiques (RViz), les démos, et les tutoriels.

En complément, les outils de développement ROS ont été installés :

```bash
sudo apt install ros-dev-tools
```

### Configuration de l’environnement

Pour pouvoir utiliser les commandes ROS2 à chaque session, le script d’environnement a été ajouté au fichier `.bashrc` :

```bash

echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc

```