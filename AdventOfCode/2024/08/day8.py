
# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = True

# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = True

# Affichage de log supplémentaire pour faciliter le debugage
verbose = True

if useDataTest :
    # Utilisation des données test
    fichier = open("input_test.txt", "r")
    lignes = fichier.readlines()

    # lignes = []
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")

else:
    # Utilisation des données du challlenge
    fichier = open("input_challenge.txt", "r")
    lignes = fichier.readlines()

import re

# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0

##################################################################"
##   Etape 1 Préparer mes données
##################################################################

data = []

# On charge les données dans une liste à deux dimensions
print("\nChargement des données dans une liste à deux dimension")
for c in lignes[0]:
    if not c == '\n':
        data.append([])

for ligne in lignes:
    for i in range(len(ligne)):
        if not ligne[i] == '\n':
            data[i].append(ligne[i])

# Affiche le tableau
print("\n Affichage des données : \n")
for j in range(len(data[1])):
    afficheLigne = ""
    for i in range(len(data)):
        afficheLigne = afficheLigne + data[i][j]
    print(afficheLigne)


##################################################################
##   Etape 2 exploiter les données
##################################################################

# On stocke la liste des antennes dans un dico qui contiendra en clé le caractère de l'antenne
# et en valeur la liste des positions
dicAntennas = {}
print(f"\nListe des antennes\n")
for j in range(len(data[1])):
    for i in range(len(data)):
        if not data[i][j] == ".":

            key = data[i][j]
            if verbose:
                print(f"Antenne {key} pos {i+1}:{j+1}")

            if not key in dicAntennas.keys():
                dicAntennas[key] = []
            # if dicAntennas.get(data[i][j]) is None:
            #     key = data[i][j]
            #     dicAntennas[key] == [(i, j)]
            dicAntennas.get(data[i][j]).append((i, j))

print(dicAntennas)

print(f" Ajouts des \"antinode \"")


for item in dicAntennas.items():
    if verbose:
        print(f" Antennes {item[0]} :")

    while len(item[1])> 1:

        for i in range(len(item[1])-1):
            posx = item[1][i][0] - (item[1][i+1][0] - item[1][i][0])
            posy = item[1][i][1] - (item[1][i+1][1] - item[1][i][1])

            if posx > -1 and posx < (len(data) -1) and posy > -1 and posy < (len(data[0]) -1) and data[posx][posy] == ".":
                data[posx][posy] = "#"

        del item[1][0]

# Affiche le tableau
print("\n Affichage des données : \n")
for j in range(len(data[1])):
    afficheLigne = ""
    for i in range(len(data)):
        afficheLigne = afficheLigne + data[i][j]
    print(afficheLigne)


if isLvlOne:
    print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")
else:
    print(f"\nRésultat du challenge partie 2 : {resultatChallenge}")



