# Partie Mécanique

## 📍 Objectif

La partie mécanique de ce test aura pour objectif principal de réaliser l’architecture entier du convoyeur ainsi que de  concevoir les différentes pièces qui le composent tout en respectant les exigences mécanique du système.  C’est l’occasion pour nous non seulement  de démontrer notre esprit créatif  et novateur mais également  d’appliquer toutes les notions acquises en matière de modélisation 3D lors des tests précédents. 

## ⚙️ Analyse fonctionnelle

Afin d’avoir une vue globale du projet et une idée claire de la tâche à accomplir, il est important  d’effectuer une analyse fonctionnelle du projet. Celle ci aura pour objectif de définir clairement l’utilité du système ainsi que les contraintes auxquels doit satisfaire le système. 

### Diagramme bête à cornes

Il s’agit ici de définir de manière claire et précise l’utilité du système pour les utilisateurs. 

![IMG-20250724-WA0005.jpg](./assets/images/IMG-20250724-WA0005.jpg)

### Diagramme d’énergie puissance

Ce diagramme permet de mieux  analyser les échanges de matière et d'Energie se faisant dans le système. 

![IMG-20250712-WA0012.jpg](./assets/images/IMG-20250712-WA0012.jpg)

 

                                                                                                                                                                              

## ⚒️ Architecture globale du convoyeur

### 🔗Quelques options mécaniques

1. **Le type de convoyeur**

La 1ère phase de l’atteinte de notre objectif a été la sélection du type de convoyeur à réaliser en tenant compte du délais de réalisation et des solutions à notre portées. A cette étape nous avons directement pensé à un convoyeur à bande étant donné qu’il s’agit d’un type de convoyeur largement utilisé dans l’industrie mais également du fait que sa conception rime bien entre simplicité et efficacité. 

Pour faire simple, un convoyeur à bande est un système de transport continue qui utilise une bande sans fin mis en mouvement par un tambour associé à un moteur  pour déplacer des matériaux d’un point A à un point B. Il se compose principalement  : 

- D’une bande qui sert de support pour les objets à déplacer
- De deux tambours : Un relié au moteur chargé de faire mouvoir le système et le second permettant de retourner la bande
- De support verticaux
- De guides latéraux

![Test4.Convoyeur_à_bande.png](./assets/images/Test4.Convoyeur__bande.png)

![Test4.Description.png](./assets/images/Test4.Description.png)

1. **Adhérence entre les tambours et la bande** 

Le défis majeur qui se présente lors de l’utilisation d’un tel type de convoyeur est l’adhérence parfaite entre la bande et les tambour devant la faire tourner. D’autant plus qu’on utilise du plastique comme matériau pour la réalisation des tambour, et nous savons tous que le plastique est très peu réputé pour ses qualités d’adhérence… Nous avons donc décidé d’utiliser des courroies comme intermédiaire entre la bande et les tambour . Pour être plus explicite, nous disposerons de deux courroies : l’un à gauche et l’autre à droite, chacun d’entre eux étant reliée aux deux tambours extrêmes .Ensuite on posera la bande sur les deux courroies de sorte que le mouvement d’ensemble des courroies puisse faire bouger la bande . Ici se présente une illustration du système : 

1. **Transmission entre le moteur et les tambours** 

Au regard de la charge des objets à transporter et de la puissance du moteur que nous avons choisi ( le moteur pas à pas Nema 17) nous avons jugé qu’un simple encastrement de l’arbre du moteur dans l’un des extrémité du tambour suffirait à assurer une bonne continuité entre le mouvement du moteur et celui des tambours. Ensuite des roulements à billes seront utilisés afin de faciliter le mouvement de rotation des tambours autour de leur axes respectifs. 

![Capture d'écran 2025-07-24 205504.png](./assets/images/Capture_dcran_2025-07-24_205504.png)

1. **Maintient de la tension de la bande** 

Ici, nous avons préféré opter pour une solution à la fois simple, efficace et facile à concevoir. L’idée est de diviser le convoyeur en deux parties ( sur la longueur )de sorte que l’un puisse entrer dans l’autre avec une vis au dessus pour bloquer les deux parties dès que l’on a atteint la longueur voulue. En voici une illustration :

![Test4_Description_retractabilité.png](./assets/images/Test4_Description_retractabilit.png)

### ⚙️ Résumé différentes parties du convoyeur

Nous allons ici décrire le système en détaillant ses constituants ainsi que leur rôle depuis le tambour moteur jusqu’au tambour de retour. 

- **La partie moteur**
    
    En commençant par le moteur, nous avons ensuite un support permettant de le maintenir fixe et qui contient un espace circulaire réservé au roulement dont le cylindre inférieur est relié à l’arbre du tambour. Ici se présente une illustration : 
    

            

![Partie_moteur1.jpg](./assets/images/Partie_moteur1.jpg)

- **Partie latérale 1**
    
    Relié au support moteur décris précédemment à travers des joins ( voir la description détaillée des différentes pièces ), il s’agit d’une pièce destiné à entrer dans la 2e partie latérale qu’on verra plus tard l’ensemble permettant d’ajuster la longueur du convoyeur . Cette 
    
    ![fourche.png](./assets/images/fourche.png)
    
- **Partie latérale 2**
    
    Etant une partie creuse, elle est destinée à recueillir la partie précédente afin de permettre l’allongement et la rétractabilité de notre système comme nous l’avons mentionné un peu plus haut.
    
    ![Input.jpg](./assets/images/Input.jpg)
    
- **Partie tambour de retour**
    
    Cette  est constituée d’un support relié à la partie précédente par des joins, d’un roulement encastré puis  du tambour de retour dont l’arbre est  relié au cylindre inférieur du roulement l’ensemble permettant au tambour de retour d’effectuer librement son mouvement de rotation .
    
    Ici se présente une illustration de cette partie : 
    
    ![Partie_retour.jpg](./assets/images/Partie_retour.jpg)
    

La description présenté ci dessus se répète également de l’autre côté du convoyeur du fait de la symétrie du  système. Vous trouverez sur cette page une description un peu plus détaillée de chaque pièce constituant le convoyeur ainsi que les fonctions de bases utilisés pour leur conception.

[Différentes pièces du convoyeur](./convoyeur_pieces.md)

## L’assemblage dans SolidWorks

L’assemblage des différentes pièces énumérées ci dessus repose sur l’application des contraintes classiques : Coaxiale et coïncidence de face entre les entités correspondantes afin d’avoir le résultat voulu. L’application de ces contraintes a été décrite dans toutes nos documentations précédentes et donc ici, nous allons juste en faire usage afin de réaliser notre convoyeur en 3D. 

Après application de toutes les contraintes, on obtient l’assemblage final suivant : 

![Convoyeur.png](./assets/images/Convoyeur.png)

![ConvoYeur (2).png](./assets/images/ConvoYeur_(2).png)

## L’impression des pièces

Suite à la modélisation des pièces, celles dont le matériau pourrait être du plastique  ont été slicé avec le logiciel cura (Un logiciel largement utilisé pour la découpe d’objets 3D en vue d’impression) puis copié dans une imprimante pour l’impression . Ici se présente quelques vus des pièces principales imprimées 

![Couvercle IMSP - Copie.jpg](./assets/images/Couvercle_IMSP_-_Copie.jpg)

![Couvercle_TRC - Copie.jpg](./assets/images/Couvercle_TRC_-_Copie.jpg)

![Support_moteur.jpg](./assets/images/Support_moteur.jpg)

![Fouches_en_impression.jpg](./assets/images/Fouches_en_impression.jpg)

![Support_retour1.jpg](./assets/images/Support_retour1.jpg)

![Impression_en_cours.jpg](./assets/images/Impression_en_cours.jpg)

![Image_fourche.jpg](./assets/images/Image_fourche.jpg)

![joins avant1.jpg](./assets/images/joins_avant1.jpg)

![joins arriere.jpg](./assets/images/joins_arriere.jpg)

![WhatsApp Image 2025-07-26 à 13.03.35_8227bd98.jpg](./assets/images/WhatsApp_Image_2025-07-26__13.03.35_8227bd98.jpg)

## Pieces complémentaires

Il s’agit principalement ici des courroies et des roulements 

### Les courroies

En tenant compte de la circonférence des tambours,  de la distance entre nos deux tambours ainsi que des longueurs maximales et minimales du convoyeur, nous avons fixé une longueur de 1275mm pour nos courroie avec une tolérance de 25 mm . Ensuite, sur le marché, nous avons cherché puis trouvé une courroie respectant nos exigences . Vous trouverez en annexes quelques spécifications techniques de la courroie acquise . 

### Les roulements

Les diamètre externes et interne étant fixé au départ à (16mm) et (37mm) respectivement, nous avons cherché puis trouvé des modèles similaires que nous avons ensuite adaptés à nos modélisations. 

Vous trouverez plus de précision sur ces composants en annexe 

## Le montage physique

Toutes les pièces étant réunis , nous avons ensuite effectué le montage conformément à l’assemblage SolidWorks réalisé. En voici quelques images : 

![Assemblage part1.8.jpg](./assets/images/2ac7caee-e4c7-4e4a-ad97-1024c0a789c6.png)

![lateral_part1.jpg](./assets/images/f8942c1d-7f25-44db-9bef-f1b21d42a3e6.png)

![Lateral_part3 - Copie.jpg](./assets/images/Lateral_part3_-_Copie.jpg)

![Montage_courroie1.jpg](./assets/images/Montage_courroie1.jpg)

![Assemblage_complet_beau - Copie.jpg](./assets/images/0c63819d-0cf4-4507-ab51-bfdbdd64e7c9.png)

![Alex_ajustage.jpg](./assets/images/Alex_ajustage.jpg)

Ici se présente une vidéo résumant les différentes étapes de l’assemblage : 

[https://player.vimeo.com/video/1104742193?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479](https://player.vimeo.com/video/1104742193?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479)

## Problèmes rencontrés lors du montage

### 1. Maintien des tambours dans les roulements

Le premier problème que nous avons rencontré lors du montage était le glissement des tambours entre les roulements ce qui affecte les performances de notre système . Pour l’instant nous avons opté pour une solution rapide et efficace qui consiste à condamner les deux éléments avec de la colle forte. Mais il faut remarquer que cette méthode n’est pas vraiment durable et comme perspective, nous pourrions utiliser des circlips afin d’assurer une meilleur durabilité. 

### 2. Faible résistance de certaines pièces

Ce problème est liés à plusieurs facteurs tels que la précision de l’imprimante utilisée,  le remplissage ainsi que la géométrie de la pièce. Il s’agit notamment des pièces suivantes : 

![Support_retour2.jpg](./assets/images/Support_retour2.jpg)

//Piece 2 

Comme précédemment nous avons utilisé de la colle forte en attendant de réimprimer la  pièce avec un meilleur remplissage . 

## Vue final système

![WhatsApp Image 2025-07-26 à 15.16.11_e04ef43a.jpg](./assets/images/WhatsApp_Image_2025-07-26__15.16.11_e04ef43a.jpg)

![WhatsApp Image 2025-07-26 à 11.09.44_9cd955fb.jpg](./assets/images/WhatsApp_Image_2025-07-26__11.09.44_9cd955fb.jpg)

## Conclusion et apport

Centré sur la conception mécanique  d'un système de convoyeur, ce test nous a apporté énormément aussi bien en terme de compétence que d'organisation.  C'était l'occasion pour nous d'appliquer toutes les connaissances qu'on a apprises jusque là non seulement en terme de concept mécanique mais également en terme de Conception assistée par ordinateur et de plus le système réalisé nous sera d'une très grande utilité dans la conception de notre futur système robotique de collecte et de tri de déchets. En outre ce test a renforcé notre esprit d'équipe ( et c'est vraiment l'apport le plus marquant) dans le sens où on se rend compte du pouvoir de notre complémentarité car vu la complexité du projet  il fallait effectuer une répartition efficace des tâches afin de réussir le test.

## Annexe

[Annexe ](./annexe.md)