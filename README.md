# TrouverLaCapitale


Dans la première partie de Main.py je traite les questions sur les données de SI.

Dans la deuxième partie je passe au jeu de données SI -erreur. 
Dans celui-ci j'ai repéré différentes erreurs:
  - des températures aillant du texte comme valeur
  - des valeurs aberrantes

Pour résoudre la première problématique j'ai opté pour un contrôle qui vérifie si la valeur est du texte, si oui on ne la prend pas en compte, sinon l'inverse.
Pour la seconde problématique j'ai décidé de comparer la valeur en cours avec la valeur précédente. Si je remarque un écart de plus ou moins 15 degrés (seuil arbitraire) alors je ne prends pas en compte la valeur en cours.

Suite à ces corrections je remarque que les deux courbes sont identiques.

Je n'ai pas eu le temps de m'attaquer à la dernière partie car j'ai passé énormément de temps sur les deux premières (débutant en python). Mon absence lors du dernier cours n'a pas aidé non plus.

