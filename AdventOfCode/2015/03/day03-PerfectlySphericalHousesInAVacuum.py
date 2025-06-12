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



for ligne in lignes:
    data = {}
    x = 0
    y = 0
    data[(x, y)] = 1

    for instruction in ligne.strip():
        match(instruction):
            case ">" :
                x += 1
            case "<":
                x -= 1
            case "^" :
                y += 1
            case "v":
                y -= 1

        if (x,y) in data:
            data[x, y] += 1
        else:
            data[x, y] = 1

    print( f" Nombre de maisons visité : {len(data)}")
    print()
##################################################################
##   Etape 2
##################################################################


print("\nEtape 2 \n")
for ligne in lignes:
    data = {}

    # Chemin du père noel qui utilise les instructions impairs
    print("SANTA :")
    x = 0
    y = 0
    data[x, y] = 1

    for instruction in ligne.strip()[0::2]:
        print(instruction)
        match(instruction):
            case ">" :
                x += 1
            case "<":
                x -= 1
            case "^" :
                y += 1
            case "v":
                y -= 1

        if (x,y) in data:
            data[(x, y)] += 1
        else:
            data[(x, y)] = 1

    print(data)
    print( f" Nombre de maisons visité : {len(data)}")
    # Chemin du robot qui utilise les instructions impairs
    print("ROBOTSANTA :")
    x = 0
    y = 0
    data[(x, y)] += 1

    for instruction in ligne.strip()[1::2]:
        print(instruction)
        match(instruction):
            case ">" :
                x += 1
            case "<":
                x -= 1
            case "^" :
                y += 1
            case "v":
                y -= 1

        if (x,y) in data:
            data[(x, y)] += 1
        else:
            data[(x, y)] = 1

    print(data)
    print( f" Nombre de maisons visité : {len(data)}")
    print()


# for ligne in lignes:
#     a,b,c = sorted(list(int(e) for e in ligne.strip().split('x')))
#     resultatChallenge2 += a*2 + b*2 + a*b*c




print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")

print(f"\nRésultat du challenge partie 2 : {resultatChallenge2}")



