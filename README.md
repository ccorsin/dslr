# dslr
Datascience X Logistic Regression

# Objectifs :
- lire un jeu de données, à le visualiser de différentes manières,à sélectionner et nettoyer vos données
- mettre en place une régression logistique qui vous permettra de résoudredes problèmes de classification

# Data Analysis
```
$ describe.py dataset_train.csv
```

# Data viz
histogram.py
scatter_plot.py
pair_plot.py

# Logistic regression
2 programmes :
- un premier qui entraine les modèles : logreg_train.py et prend en paramètre dataset_train.csv.
  . utilise la technique du gradient descent pour minimiser l’erreur
  . le programmegénère un fichier contenant les poids qui seront réutilisés pour la prédiction
-un second qui se nommelogreg_predict.py qui prend en paramètre dataset_test.csv et un fichier contenant les poids entraînés au préalable.
