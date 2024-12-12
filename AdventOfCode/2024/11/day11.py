
# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = False

# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = True

# Affichage de log supplémentaire pour faciliter le debugage
verbose = True

if useDataTest :
    # Utilisation des données test
    lignes = []
    lignes.append("125 17")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    # else:
    #     lignes.append("")
else:
    # Utilisation des données du challlenge
    lignes = []
    lignes.append("92 0 286041 8034 34394 795 8 2051489")

import re

# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0

##################################################################"
##   Etape 1 Préparer mes données
##################################################################


data = lignes[0].split(" ")

print("\nInitial arrangement:")
print(data)

cptBlink = 0
while cptBlink < 75:
    cptBlink += 1
    i = 0
    while i < len(data):
        if data[i] == "0":
            data[i] = "1"
        elif data[i] == "1":
            data[i] = "2024"
        elif (len(data[i]) % 2) == 1:
            data[i] = str(int(data[i]) * 2024)
        else:
            data.insert(i+1, str(int(data[i][int(len(data[i]) / 2):])))
            data[i] = data[i][:int(len(data[i]) / 2)]
            i += 1

        i += 1
    if cptBlink == 25:
        resultatChallenge = len(data)
    print(f"\nAfter {cptBlink} blinks: Nb Stone : {len(data)}")
    # print(data)
##################################################################
##   Etape 2 exploiter les données
##################################################################

if isLvlOne:
    print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")
else:
    print(f"\nRésultat du challenge partie 2 : {len(data)}")



