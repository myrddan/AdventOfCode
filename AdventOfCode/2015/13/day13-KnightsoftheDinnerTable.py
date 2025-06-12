import itertools

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

    fichier = open("input_test.txt", "r")
    lignes = fichier.readlines()

    # lignes = []
    # if isLvlOne:
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
    # else:
    #     lignes.append("")
else:
    # Utilisation des données du challlenge
    fichier = open("input_challenge.txt", "r")
    lignes = fichier.readlines()

import re

# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0
resultatChallenge2 = 0



##################################################################"
##   Etape 1
##################################################################
print("\nEtape 1 \n")

setNom = set()
DicRelations = {}
# Pour prendre en compte la partie deux, ajouter la ligne suivante :
setNom.add("me")

for ligne in lignes:
    decoup = ligne.split(" ")
    name1 = decoup[0]
    name2 = decoup[-1][0:-2]
    if decoup[2] == 'gain':
        happiness = int(decoup[3])
    else:
        happiness = - int(decoup[3])

    setNom.add(name1)
    DicRelations[name1+":"+name2] = happiness

from itertools import permutations

for combo in permutations(setNom, len(setNom)):
    happiness = 0
    for i in range(len(combo)):
        name1 = combo[i]
        name2 = combo[(i + 1) % len(combo)]

        if name1 == 'me' or name2 == 'me':
            happy1 = 0
            happy2 = 0
        else:
            happy1 = DicRelations[name1+":"+name2]
            # print(f" {name1}>>{name2} {happy1}")

            happy2 = DicRelations[name2+":"+name1]
            # print(f" {name2}>>{name1} {happy2}")

        happiness += happy1
        happiness += happy2
    print(f" {happiness}>> {combo}")
    if happiness > resultatChallenge:
        resultatChallenge = happiness

from itertools import combinations


##################################################################
##   Etape 2
##################################################################

print("\nEtape 2 \n")



print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")

print(f"\nRésultat du challenge partie 2 : {resultatChallenge2}")



