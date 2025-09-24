#Projet individuel -Analyse des donnees meteorologiques mon code reponds a la question quelle est la temperature moyenne par mois a Ottawa

import pandas as pd  #lire et manipuler le CVS comme un tableau
import matplotlib.pyplot as plt #tracer des graphiques
#import numpy as np #les fonctions mathematiques et les calculs numerique

# Charger les données
df = pd.read_csv("ottawaairport_temp.csv") #lit le fichier CVS et le stocke dans un Dataframe
print(df.columns)  # affiche les noms des colonnes
print(df.dtypes)   # affiche le type de donnée de chaque colonne

# Sélectionner et convertir les colonnes
df = df[["Mois", "Temp moy.(°C)"]]  # on garde seulement Mois et la Température moyenne
df["Mois"] = pd.to_numeric(df["Mois"], errors="coerce")  # conversion en numérique
df["Temp moy.(°C)"] = pd.to_numeric(df["Temp moy.(°C)"].astype(str).str.replace(",", "."), errors="coerce") #si le CVR utilise virgule comme separateur decimal on remplace par point

# Supprimer les lignes manquantes
df = df.dropna(subset=["Mois", "Temp moy.(°C)"]) #supprime toutes les lignes ou  il manque Mois ou Température moyenne

print(df.head())#affiche les 5 premieres lignes du data frame
print(f"Nombre de lignes après nettoyage : {len(df)}")#affiche le nombre de lignes apres nettoyage

# Calculer la moyenne des températures par mois
monthly_mean = df.groupby("Mois")["Temp moy.(°C)"].mean()

# Visualisation
plt.figure(figsize=(10,6))#definir la taille de la figure
plt.plot(monthly_mean.index, monthly_mean.values, marker="o", color="blue", label="Température moyenne")#tracer la courbe
plt.title("Température moyenne par mois à Ottawa Airport(année 1995)")#titre du graphique
plt.xlabel("Mois")#nom de l'axe des x
plt.ylabel("Température moyenne (°C)") #nom de l'axe des y
plt.xticks(range(1, 13))#definir chaque mois sur l'axe des x
plt.legend()#afficher la legende
plt.grid(True)#afficher la grille
plt.show()#afficher le graphique
