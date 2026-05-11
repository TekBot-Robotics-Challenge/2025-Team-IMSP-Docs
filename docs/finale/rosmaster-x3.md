---
outline: deep
---

# SYSTEME ROSMASTER X3

[**ACCUEIL**](/2025-Team-IMSP-Docs/finale/) | [**SYSTEMES**](/2025-Team-IMSP-Docs/finale/#architecture-du-système)

---

# Introduction

Dans le cadre de la **finale du concours de robotique TRC 2K25**, nous sommes invités à simuler une **mission d’assainissement de zones urbaines et industrielles** à l’aide d’un robot autonome, en l’occurrence le **ROSMASTER X3**, dont la mission principale est de **collecter et transporter les déchets**.

Cependant, la version du robot mise à notre disposition **ne dispose pas de système de ramassage intégré**, ce qui limite considérablement son autonomie opérationnelle.

L’une des missions principales de notre équipe consiste donc à **concevoir, modéliser et intégrer un système mécanique de ramassage** conforme aux exigences du **cahier des charges**, en utilisant le logiciel **SolidWorks**.

L’objectif final est de développer un dispositif **fonctionnel, léger et stable**, pouvant être **testé virtuellement dans l’environnement Gazebo avec Nav2**, avant une éventuelle mise en œuvre pratique.

# Partie Mécanique

## Besoins à satisfaire

Concevoir un système de ramassage capable de collecter des déchets dans une arène de 10 quartiers comportant 100 déchets à raison de 10 par quartier pendant au plus 5 min. 

Pour ce faire, on doit :

- Collecter un déchet cubique de 30mm d’arrête.
- Maintenir la stabilité du robot pendant la manipulation
- Transporter les déchets sans les perdre
- Déposer les déchets  un endroit défini

## Contraintes techniques

- **Dimensions maximales**
    - Longueur : **450 mm**
    - Largeur : **245 mm**
    - Hauteur : **200 mm**
- **Contraintes énergétiques**
    - La consommation électrique du mécanisme doit être **adaptée à la capacité de la batterie du robot**, afin de ne pas réduire significativement son autonomie.
    - Les moteurs ou actionneurs sélectionnés doivent être **efficaces et légers**.
- **Matériaux**
    - Les matériaux disponibles pour la fabrication sont : **PLA** et le contreplaqué **(4mm)**.
    - Le choix des matériaux doit garantir :
        - **Rigidité suffisante** pour supporter le poids des déchets collectés.
        - **Légèreté** pour ne pas déséquilibrer le robot.
        - **Compatibilité avec l’impression 3D** et ou la découpe laser.
- E**nvironnementales**
    - Le système est conçu pour évoluer sur une **surface plane horizontale**.
    - La conception doit assurer **stabilité et adhérence** du robot lors de la collecte.
- **Mobilité**
    - Le robot doit être capable de se déplacer rapidement dans l’arène.

## **Analyse et choix du mécanisme de collecte**

### 1. Décomposition fonctionnelle

Afin de concevoir un système de ramassage **efficace et pleinement compatible** avec le robot **ROSMATER X3**, une **décomposition fonctionnelle** a été réalisée afin d’identifier les fonctions essentielles que le dispositif doit assurer, **indépendamment des choix technologiques**.

La **fonction principale** du système consiste à **collecter les déchets présents dans la zone d’intervention et à les stocker temporairement à bord du robot**, en vue de leur évacuation après chaque cycle de collecte.

Pour remplir cette fonction principale, le système doit satisfaire plusieurs **fonctions techniques secondaires**. Il doit tout d’abord **interagir avec les déchets présents au sol** afin de permettre leur prise en charge. Il doit ensuite **regrouper et diriger les déchets collectés** vers une zone dédiée au stockage. Le système doit également **assurer le stockage temporaire des déchets** jusqu’à la fin d’un cycle, tout en permettant leur **vidage de manière contrôlée**. Enfin, il doit rester **compatible avec les mouvements et les changements d’orientation du robot** au cours de sa mission.

L’ensemble de ces fonctions doit être assuré dans le respect des **contraintes du cahier des charges**, notamment les contraintes **dimensionnelles, énergétiques, matérielles et d’intégration**, afin de garantir une adaptation optimale au robot existant.

### **2. Recherche de solutions**

Dans le cadre de la conception du système de ramassage, plusieurs **solutions mécaniques** ont été étudiées afin de permettre au robot **ROSMASTER  X3** de collecter efficacement les déchets présents dans un quartier, tout en respectant les contraintes du cahier des charges.

[**Solution 1 : Pince mécanique articulée**](/finale/solution-1)

[**Solution 2 : Pelle frontale avec berne arrière**](/finale/solution-2)

[**Solution 3 : Système de collecte en masse à canalisation arrière**](/finale/solution-3)

### 3. Solution retenue

Après une analyse comparative des différentes solutions envisagées, la **solution de canalisation arrière** a été retenue comme la plus adaptée au robot **ROSMASTER X3** et aux exigences du concours. En effet, cette solution répond à l’ensemble des **contraintes techniques, mécaniques et fonctionnelles** définies dans le cahier des charges, tout en garantissant une **intégration fluide** au robot existant.

### 🔹 **Critères techniques de choix**

1. **Efficacité temporelle**
    
    Contrairement aux systèmes de pince ou de bras articulé, la solution retenue permet une **collecte en masse instantanée** de tous les déchets d’un quartier, ce qui nous rapproche plus de la contrainte de temps de **5 minutes pour 10 quartiers**.
    
2. **Simplicité mécanique et fiabilité**
    
    Le système repose sur seulement **deux actionneurs** :
    
    - un **moteur pas à pas** pour le mouvement de translation du cadre,
    - un **servomoteur** pour la gestion de la trappe arrière.
        
        Cette architecture mécanique réduit le risque de panne, facilite la maintenance et limite la consommation énergétique.
        
3. **Stabilité et équilibre**
    
    La **berne placée à l’arrière** du robot assure un bon équilibre global, notamment lors du remplissage, en contrebalançant le poids du mécanisme de ramassage.
    
4. **Préservation du champ de vision**
    
    L’absence de dispositif volumineux à l’avant du robot permet de **conserver la pleine visibilité de la caméra de profondeur**, indispensable à la navigation et à la détection d’obstacles.
    
5. **Facilité d’intégration et de fabrication**
    
    Les pièces du système sont **faciles à modéliser et à imprimer** sous **SolidWorks** et s’adaptent directement à la structure du ROSMASTRE X3 sans nécessiter de modification majeure du châssis.
    
6. **Respect des contraintes environnementales et dimensionnelles**
    
    Le système respecte les **dimensions maximales imposées** (450 mm × 245 mm × 200 mm) et reste compatible avec l’environnement de travail **sur surface horizontale**.
    

### 🔹 **Limites identifiées**

La principale limite de cette solution réside dans la **capacité maximale de la berne**, qui permet de traiter **un seul quartier à la fois** (soit environ 45 déchets). Il est donc nécessaire de **vider la berne après chaque cycle de collecte** avant de poursuivre la mission.

### 🔹 **Conclusion du choix**

Le **système de canalisation arrière avec berne** a été retenu pour sa **simplicité, sa fiabilité et son efficacité de collecte**, tout en assurant une **parfaite compatibilité** avec la structure et les contraintes du ROSMASTER X3.

Il représente le **meilleur compromis entre performance, stabilité et intégration**, et constitue une base solide pour la **modélisation**  sous **SolidWorks.**

## **4. Conception et modélisation sous SolidWorks**

Le système de ramassage a été entièrement conçu sous **SolidWorks** afin d’assurer sa compatibilité mécanique avec le **ROSMASTER  X3** et de respecter les contraintes de dimension, de stabilité et d’intégration.

### **Présentation du système conçu**

Le système se compose de trois éléments principaux :

- **Berne de collecte**

La berne est un élément central du système de ramassage. Elle est **positionnée à l’arrière du robot** afin d’assurer le **stockage temporaire des déchets collectés** tout en préservant l’équilibre du robot et le champ de vision de la caméra frontale.

La berne présente des dimensions de **235 mm de longueur**, **200 mm de largeur** et **155 mm de hauteur totale**, conformes aux contraintes de dimensionnement imposées par le cahier des charges.

Afin de faciliter l’entrée des déchets, une **ouverture a été intégrée dans la partie inférieure de la berne**. L’entrée est précédée d’une **surface inclinée à 15° par rapport à l’horizontale**, permettant aux déchets de **glisser naturellement** vers l’intérieur. Une **rampe interne** prolonge cette inclinaison afin d’assurer le **guidage et le logement des déchets** à l’intérieur de la berne, comme illustré sur la figure ci-dessous.

![Berne_1.png](./assets/rosmaster-x3/Berne_1.png)

La berne intègre également **des logements dédiés à la fixation des rails télescopiques**, assurant le guidage du système de canalisation et la fluidité du mouvement en translation.

Un **logement spécifique pour un moteur pas à pas NEMA 17** a été prévu, permettant l’entraînement des rails télescopiques et le déploiement contrôlé du mécanisme.

Enfin, la berne est équipée d’un **système de translation secondaire**, fixé au châssis du robot à l’aide de **vis M3**, garantissant une **fixation rigide**, un **bon alignement mécanique** et une **intégration stable** avec la structure du ROSMASTER X3.

![Berne_2.png](./assets/rosmaster-x3/Berne_2.png)

- **NEMA 17**

Le moteur pas à pas **NEMA 17** a été modélisé à l’aide des **fonctions d’extrusion de matière et de coupe** de SolidWorks. L’assemblage des différentes pièces repose sur des **contraintes standards de coïncidence de faces et d’axes**, assurant une intégration correcte dans le mécanisme. Les détails de la modélisation des pièces sont présenté dans le **Test 4**.

![Nema 17.png](./assets/rosmaster-x3/Nema_17.png)

- **Rails Télescopiques**

Ce support, constitué de **trois pièces principales**, assure le maintien du dispositif de délimitation rectangulaire. Sa modélisation repose sur des **esquisses simples** et l’utilisation des **fonctions d’extrusion de matière et de coupe** de SolidWorks. L’assemblage a été réalisé à l’aide de **contraintes standards** (distance, parallélisme) ainsi que de **contraintes avancées**, telles que le **coupleur linéaire**, la **largeur** et la **distance limite**, afin de garantir le mouvement attendu.

![Rail_téléscopiques.png](./assets/rosmaster-x3/Rail_tlscopiques.png)

- **Pièce Supérieure**

Elle mesure en tout 250mm de longueur pour une largeur de externe de 42mm. L’épaisseur est estimé à 12mm

![Supérieure.png](./assets/rosmaster-x3/Suprieure.png)

- **Pièce Inférieure**

Elle mesure en tout 247mm de longueur pour une largeur de externe de 25mm. L’épaisseur est estimé à 7mm

- **Pièce Intermédiaire**

![Inférieure.png](./assets/rosmaster-x3/Infrieure.png)

Elle mesure en tout 223mm de longueur pour une largeur de externe de 35mm. L’épaisseur est estimé à 9mm

![Intermédiaire.png](./assets/rosmaster-x3/Intermdiaire.png)

- **Roue dentée:**

En effet, une roue dentée de 25 dents pour un pas de 2 à  été conçu pour transmettre de façon efficace le couple du moteur au cadre rectangle.

![Complément.png](./assets/rosmaster-x3/Complment.png)

- **Rail Simple :**

![Roue_dentée.png](./assets/rosmaster-x3/Roue_dente.png)

 Conçue en contreplaqué pour servir de **guide linéaire, elle** permet de **transmettre le mouvement de translation** des rails télescopiques tout en assurant la **stabilité et le soutien** des pièces mobiles qui y sont fixées.

![image.png](./assets/rosmaster-x3/image.png)

- **Rail denté :**

Cette pièce, fabriquée en contreplaqué, a pour fonction de servir de crémaillère pour le pignon. Elle permet de transmettre efficacement le couple du moteur NEMA 17 et d’entraîner le mouvement de translation du système de délimitation des quartiers.

![Rail.png](./assets/rosmaster-x3/Rail.png)

La réalisation de cette pièce présente une **subtilité supplémentaire** par rapport au **rail simple**. Nous prendrons donc le soin de **décrire étape par étape sa conception**.

Dans un premier temps, nous avons réalisé une esquisse dans le **plan frontal** en utilisant des outils de base, tout en appliquant les **contraintes de distance appropriées** afin de définir correctement la géométrie de la pièce *(voir image de l’esquisse)*.

![Rail_sketch1.png](./assets/rosmaster-x3/Rail_sketch1.png)

Ensuite, nous avons appliqué la **fonction de création de matière (extrusion)** afin d’obtenir la pièce présentée ci-dessous . 

Par ailleurs, en faisant recours à la **bibliothèque Toolbox de SolidWorks**, nous avons importé une **crémaillère de 300 mm de longueur**, avec un **module de 2**, de manière à ce qu’elle soit parfaitement adaptée au **pignon relié au moteur NEMA 17**.

Nous avons ensuite ouvert un **assemblage SolidWorks**, dans lequel nous avons assemblé la crémaillère importée et la pièce modélisée précédemment. Le résultat de cet assemblage est présenté ci-dessous *(voir image du résultat)*.

Par la suite, au sein de l’assemblage, nous avons souhaité **modifier la pièce du rail simple** en convertissant, dans le **plan de face de cette pièce**, la **face dentée de la crémaillère** importée. Cette opération nous a conduit au résultat suivant *(une esquisse normalisée)*.

![Rail_simple.png](./assets/rosmaster-x3/Rail_simple.png)

Il est alors possible de remarquer que cette pièce est encore similaire à la pièce précédente, à savoir le **rail simple**.

![Rail_sketch2.png](./assets/rosmaster-x3/Rail_sketch2.png)

![Rail_sketch3.png](./assets/rosmaster-x3/Rail_sketch3.png)

![Rail_sketch4.png](./assets/rosmaster-x3/Rail_sketch4.png)

Ensuite, nous avons appliqué la **fonction de création de matière (extrusion Base/boss)** afin d’obtenir la pièce que nous voulons (rail dentée). 

![Rail.png](./assets/rosmaster-x3/Rail%201.png)

- **Un dispositif de délimitation:**
    
    **E**ntraîné par le **moteur pas à pas NEMA 17**, ce mécanisme se déploie par translation pour d’encadrer un quartier contraignant ainsi les déchets à pénétrer dans la berne. Il est essentiellement composée 05principales pièces.
    

![Back.png](./assets/rosmaster-x3/Back.png)

**Pièce 1 (Backpart_2) : [Polywood]**

Réalisée en deux exemplaires, cette pièce se connecte directement aux **rails télescopiques** via les **rails dentés et simples** présentés précédemment, assurant ainsi la **fixation stable du dispositif de délimitation**.

**Pièce 2 (Backpart_1) : [Polywood]**

Réalisée en contreplaqué, cette pièce se fixe à la **pièce Backpart_2** et assure le **soutien de la trappe** ainsi que du **moteur MG995** responsable de son mouvement.

- **Pièce 3 (Servo Mount) : [Métal]**

Le **Servo Mount**, servant de support pour le servomoteur MG995, **n’a pas été modélisé** et a été **importé directement depuis la plateforme GRABCAD**. Il assure une fixation stable et précise du servomoteur au dispositif de délimitation. 

- **Pièce 4 (Trappe_part_3+) :  [PLA]**

Cette pièce assure la **fixation de la trappe au dispositif de délimitation**, garantissant ainsi le **mouvement de rotation** correct de la trappe.

**Pièce 5 (Backpart_3) : [Polywood]**

Cette pièce complémentaire améliore le **contact et la fixation** entre la **Backpart_2** et les **rails télescopiques**, renforçant ainsi la **stabilité du mécanisme**.

![Back_part_2.png](./assets/rosmaster-x3/Back_part_2.png)

![Back_prt_1.png](./assets/rosmaster-x3/Back_prt_1.png)

![Metal_mount.png](./assets/rosmaster-x3/Metal_mount.png)

![Trappe_part_3.png](./assets/rosmaster-x3/Trappe_part_3.png)

![Back_part_3.png](./assets/rosmaster-x3/Back_part_3.png)

- **Trappe arrière :**

La trappe, composée de **quatre pièces principales**, est conçue pour **empêcher les déchets de s’échapper vers l’arrière** et pour **diriger les déchets vers l’intérieur de la berne** lors du mouvement inverse du moteur, assurant ainsi leur confinement complet.

La **modélisation des pièces** a été réalisée à partir d’**esquisses de base** comprenant des lignes droites, rectangles, cercles et polygones, suivie de l’application des **fonctions standards de création et d’extrusion de matière (Boss/Base et Extrude-Coupe)**.

![Trappe_out.png](./assets/rosmaster-x3/Trappe_out.png)

![Trappe_in.png](./assets/rosmaster-x3/Trappe_in.png)

- **Pièce 1 – Pièce principale de la trappe [Polywood]**

Cette pièce constitue le **support principal** du système de trappe et sert de fixation pour les autres composants. 

![Trappe_part1.png](./assets/rosmaster-x3/Trappe_part1.png)

- **Pièce 2 – Pièce de contact [Polywood]**

Fabriquée en **contreplaqué**, cette pièce sert de **surface de contact** lors de la mise en mouvement du système de ramassage, permettant un **guidage précis et sécurisé** de la trappe.

- **Pièce 3 – Pièce d’attache [PLA]**

Cette pièce assure la **fixation de la trappe au dispositif de délimitation**, garantissant ainsi le **mouvement de rotation** correct de la trappe.

- **Pièce 4 – Boss de pression**

De forme **bossée** et réalisée en **PLA**, cette pièce est fixée sur la pièce principale afin de **décupler la pression exercée par la trappe sur les déchets**, améliorant le confinement. Sa conception utilise des esquisses simples et les fonctions d’extrusion pour créer la forme bossée.

![Trappe_part_2.png](./assets/rosmaster-x3/Trappe_part_2.png)

![Trappe_part_3+.png](./assets/rosmaster-x3/Trappe_part_3%201.png)

![Trappe_part4.png](./assets/rosmaster-x3/Trappe_part4.png)

- **Connecteur : [Polywood]**

Réalisée avec du contreplaqué, le connecteur permet de **relier la trappe au servomoteur**, assurant ainsi la **transmission du mouvement de rotation** du moteur vers la trappe. Cette liaison garantit un mouvement précis et fiable lors du fonctionnement du système.

![Connecteur.png](./assets/rosmaster-x3/Connecteur.png)

- **Servomoteur MG995 et adaptateur**

Fixé à un connecteur à l’aide d’un adaptateur, le servomoteur **MG995** permet de **mettre en rotation la trappe** située à l’arrière du dispositif de délimitation.

Le moteur et son adaptateur **n’ont pas été modélisés** et ont été **importés directement depuis la plateforme de fabrication numérique GRABCAD**.

![Servo_moteur_horn.png](./assets/rosmaster-x3/Servo_moteur_horn.png)

![MG995.png](./assets/rosmaster-x3/MG995.png)

- **Roue dentée:**

En effet, une roue dentée de 25 dents pour un pas de 2 à  été conçu pour transmettre de façon efficace le couple du moteur au système de translation.

![Roue_dentée.png](./assets/rosmaster-x3/Roue_dente.png)

Réalisée avec du contreplaqué, cette pièce sert de contact direct avec la crémaillère et l’arbre du moteur via l’intermédiaire de la pièce suivante imprimée en PLA (Remplissage 100% pour une transmission durable)

![Complément.png](./assets/rosmaster-x3/Complment.png)

- **Anneau**

Afin d’assurer la **fixation du pignon sur l’arbre du moteur**, un **anneau de serrage** a été conçu. Il est muni d’un **logement pour une vis et un écrou**, permettant d’exercer une **pression radiale sur l’arbre du moteur** et de garantir un maintien fiable du pignon (cf. figure ci-dessous).

![Anneau.png](./assets/rosmaster-x3/Anneau.png)

- **Support du kit électronique**

Afin d’assurer le support des **composants électroniques** dédiés à la commande du **servomoteur MG995** et du **moteur pas à pas NEMA 17**, un **support de forme squelettique** a été conçu. Ce choix permet de **réduire l’encombrement**, de **limiter la masse** et de garantir une **ventilation permanente** des composants.

Le dispositif est constitué de **deux pièces principales**.

La première pièce correspond à un **châssis squelettique** destiné à recevoir un **veroboard**, sur lequel sont implantés le **driver du NEMA 17**, le **régulateur de tension LM4015** ainsi qu’un **ESP32** (cf. figure ci-dessous).

![Supp_electro_2.png](./assets/rosmaster-x3/Supp_electro_2.png)

![Supp_electro_1.png](./assets/rosmaster-x3/Supp_electro_1.png)

La seconde pièce a été conçue comme **support de ventilateur**, assurant le **refroidissement actif du système électronique** et contribuant à la fiabilité globale du dispositif (cf. figure ci-dessous).

![Support_ventillateur.png](./assets/rosmaster-x3/Support_ventillateur.png)

- ROSMASTER CUSTOMISE

![Screenshot 2026-01-11 202032.png](./assets/rosmaster-x3/Screenshot_2026-01-11_202032.png)

![Screenshot 2026-01-11 201906.png](./assets/rosmaster-x3/Screenshot_2026-01-11_201906.png)

![Screenshot 2026-01-11 201946.png](./assets/rosmaster-x3/Screenshot_2026-01-11_201946.png)

![Screenshot 2026-01-11 202002.png](./assets/rosmaster-x3/Screenshot_2026-01-11_202002.png)

### Justification des choix techniques

- **Matériaux :** PLA (léger, imprimable) et Contreplaqué (plus léger que le PLA, moins coûteux, renforts structurels).
- **Mouvements :** translation avec des rails télescopiques pour la canalisation, rotation pour la trappe.
- **Position arrière :** Equilibre du robot, champ de vision libre, meilleure intégration.
- **Conception allégée :** Formes évidées pour réduire le poids et optimiser la consommation énergétique.

[https://vimeo.com/1190744596?share=copy&fl=sv&fe=ci](https://vimeo.com/1190744596?share=copy&fl=sv&fe=ci)

# **Difficultés rencontrées lors de la réalisation du système de ramassage et solutions apportées.**

Après la **réalisation physique et l’assemblage** des différentes pièces constituant le système de ramassage, plusieurs **difficultés pratiques** ont été observées.

La première difficulté concernait **l’entrée des déchets dans la berne**. Malgré les dispositions prévues lors de la conception, notamment **l’inclinaison de la pente d’entrée fixée à 15° par rapport au sol** et l’ajout d’une **bosse sur la trappe arrière**, les déchets présentaient une **résistance importante au glissement** et ne pénétraient pas correctement dans la berne.

Pour résoudre ce problème, un **film en plastique issu d’une feuille de reliure transparente** a été fixé à l’entrée de la berne. Cette solution a permis de **réduire significativement les frottements**, facilitant ainsi le glissement des déchets vers l’intérieur de la berne.

![image.png](./assets/rosmaster-x3/image%201.png)

![_berne.jpeg](./assets/rosmaster-x3/_berne.jpeg)

Le second problème majeur était lié à la **fermeture de la trappe arrière**. Dans certaines configurations, la présence de déchets pouvait **bloquer le mouvement de fermeture**, compromettant le confinement du système. Cette observation nous a conduits à **repenser le mécanisme de fermeture**, en intégrant un **système mobile plus tolérant aux interférences**, tel que présenté dans la vidéo suivante.

![EP1.png](./assets/rosmaster-x3/EP1.png)

![EP2.png](./assets/rosmaster-x3/EP2.png)

La solution en question a présenté aussi des problèmes que nous avons réglé. Il s'agit en effet de la flexibilité du système mobile qui crée un blocage lors de la fermeture de la trappe arrière du  ROSMASTER X3

### **Vidéo explicative**

[Vidéo_résultat](https://vimeo.com/1154436305?fl=tl&fe=ec)

# SYSTÈME DE RAMASSAGE : UNITÉ ÉLECTRONIQUE ET CONTRÔLE

## I. Objectif du Système

L'unité électronique a pour mission de piloter les deux actionneurs du système de ramassage :

1. Un **servomoteur** pour l'ouverture/fermeture de la benne.
2. Un **moteur pas à pas** pour le mouvement de translation (augmentation du volume de stockage).
    
    L'ensemble est intégré à l'écosystème du Rosmaster X3.
    

---

## II. Architecture de Contrôle (Méthodologie)

La stratégie de contrôle repose sur une architecture **Maître-Esclave** :

- **Maître (Raspberry Pi 5) :** Exécute la logique de haut niveau et envoie des instructions via une liaison **Série (USB)**.
- **Esclave (ESP32) :** Reçoit les ordres en temps réel et génère les signaux de puissance (PWM et signaux STEP/DIR).
- **Alimentation :** Le système puise son énergie directement dans la batterie **Li-ion 7.4V** du Rosmaster.

---

## III. Spécifications du Matériel (BOM)

| **Composant** | **Rôle & Justification** |
| --- | --- |
| **ESP32** | Choisi pour sa capacité à générer des signaux PWM précis et stables, évitant les interruptions liées à l'OS non temps-réel (Ubuntu) du Raspberry Pi. |
| **Raspberry Pi 5** | Cerveau du Rosmaster, il centralise les décisions et communique les ordres via Python. |
| **Servomoteur MG995** | Actionneur de force pour la benne. Rotation 0-90° pour sécuriser le dépôt des déchets. |
| **Moteur Nema 17** | Assure la translation de la benne sur rails coulissants pour optimiser la capacité de ramassage. |
| **Driver A4988** | Interface de puissance pour le moteur pas à pas, convertissant les impulsions logiques en phases électriques. |
| **Régulateur Ajustable** | Abaisse la tension de **7.4V** à **6V** pour alimenter le servomoteur sans risque de surtension. |
| **Veroboard** | Support de prototypage pour la centralisation du circuit driver et des connectiques. |

---

## IV. Implémentation Logicielle (Firmware ESP32)

L'ESP32 utilise deux bibliothèques majeures : ESP32Servo.h pour la précision du PWM et AccelStepper.h pour la fluidité des mouvements du Nema 17 (gestion des rampes d'accélération).

### 4.1. Analyse de la Logique Arduino

**Instanciation :**

**Configuration des objets et des Pins**

- `AccelStepper stepper(...)` : Crée l'objet pour piloter le driver via les broches STEP et DIR.
- `servo.attach(SERVO_PIN)` : Relie le servo à la PIN 23 pour la gestion du PWM par l'ESP32.

**Initialisation et Paramétrage (Setup)**

- `Serial.begin(115200)` : Active la communication avec la Raspberry Pi.
- `setMaxSpeed(1000) & setAcceleration(500)` : Configure le Nema 17 pour un mouvement fluide et progressif (évite les secousses).
- `digitalWrite(EN_PIN, LOW)` : Active le driver A4988.
- **Traitement des commandes :**
    - Si la commande commence par **"S"** (ex: S90) : Extraction de la valeur numérique et positionnement du servomoteur.
    - Si la commande commence par **"M"** (ex: M400) : Calcul du déplacement relatif et exécution du mouvement pas à pas avec la fonction bloquante stepper.run().

### 4.2. Code Source complet : ESP32 Firmware

codeC++

```cpp
#include <ESP32Servo.h>
#include <AccelStepper.h>

// Définition des broches
#define STEP_PIN 25
#define DIR_PIN 26
#define EN_PIN 27
#define SERVO_PIN 23

AccelStepper stepper(AccelStepper::DRIVER, STEP_PIN, DIR_PIN);
Servo servo;

void setup() {
  Serial.begin(115200); 

  servo.attach(SERVO_PIN);

  // Configuration moteur pas à pas
  stepper.setMaxSpeed(1000);     // Pas par seconde
  stepper.setAcceleration(500);  // Accélération progressive
  
  pinMode(EN_PIN, OUTPUT);
  digitalWrite(EN_PIN, LOW);     // Activation du driver A4988

  Serial.println("ESP32 Ready");
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    // Analyse de l'instruction
    if (cmd.startsWith("S")) {       // Commande Servomoteur
      int angle = cmd.substring(1).toInt();
      servo.write(angle);
    }
    else if (cmd.startsWith("M")) {  // Commande Moteur Pas à Pas
      int steps = cmd.substring(1).toInt();
      stepper.move(steps);
      while (stepper.distanceToGo() != 0) {
        stepper.run();               // Exécution du mouvement
      }
    }
  }
}
```

---

## V. Contrôle de Haut Niveau (Script Python - Raspberry Pi)

Le script Python assure la synchronisation des mouvements. Il encode les chaînes de caractères en bytes pour la transmission série.

### 5.1 Explication de la logique Python

- **`serial.Serial('COM12', ...)` :** Ouvre le canal de communication. Le *timeout* de 1s évite de bloquer le programme si l'ESP32 ne répond pas.
- **`send_command(cmd)` :** Cette fonction est cruciale. Elle ajoute le caractère de fin de ligne \n, puis utilise .encode() pour transformer le texte en format binaire (bytes) lisible par le port série.
- **Séquence de ramassage :**
    1. `S90` : Ouverture de la benne.
    2. `M400` : Extension des rails pour augmenter la capacité.
    3. `S0` : Fermeture et sécurisation des déchets.
    4. `M-400` : Retour en position initiale (rétractation).

### 5.2. Code Source complet : Logiciel Maître

codePython

```python
import serial
import time

# Initialisation de la liaison série
# Note : Changez 'COM12' par '/dev/ttyUSB0' sur le Raspberry Pi
try:
    ser = serial.Serial('COM12', 115200, timeout=1)
    time.sleep(2) # Attente de l'initialisation de l'ESP32
except Exception as e:
    print(f"Erreur de connexion : {e}")

def send_command(cmd):
    """Envoie une commande formatée à l'ESP32"""
    ser.write(f"{cmd}\n".encode())
    print(f"Instruction transmise : {cmd}")

# Séquence de ramassage type
try:
    send_command("S90")    # Ouverture de la benne
    time.sleep(1)

    send_command("M400")   # Extension de la benne (translation)
    time.sleep(2)

    send_command("S0")     # Fermeture de la benne
    time.sleep(1)

    send_command("M-400")  # Rétractation de la benne
    time.sleep(2)

finally:
    ser.close()
    print("Connexion série fermée.")
```

***Résultat final Obtenu***

[https://vimeo.com/1190665279?share=copy&fl=sv&fe=ci](https://vimeo.com/1190665279?share=copy&fl=sv&fe=ci)