# Solution 3 : Système de collecte en masse à canalisation arrière

La solution retenue repose sur un **système de canalisation arrière** permettant la **collecte simultanée des déchets d’un quartier** par encadrement et translation inverse.

Le dispositif est principalement composé d’une **berne de collecte**, intégrée à l’arrière du robot pour le stockage temporaire des déchets, et d’un **cadre rectangulaire mobile** chargé d’encercler la zone à nettoyer. Une **trappe arrière**, associée au cadre, permet de contrôler le confinement des déchets durant le déplacement.

Afin de permettre le transfert des déchets vers la berne, une **ouverture a été aménagée sur la partie inférieure de celle-ci**. Le cadre se déploie alors autour du quartier, puis effectue un **mouvement de translation inverse** qui guide les déchets vers l’ouverture de la berne. La trappe se referme ensuite pour empêcher toute dispersion, et le cadre est rétracté vers le robot.

Ce système est actionné par **deux moteurs** : un **moteur pas à pas** pour la translation du cadre et un **servomoteur** pour la commande de la trappe.

Cette solution permet une **collecte rapide en masse**, tout en **préservant la stabilité du robot**, le **champ de vision de la caméra frontale** et la **simplicité mécanique** de l’ensemble.