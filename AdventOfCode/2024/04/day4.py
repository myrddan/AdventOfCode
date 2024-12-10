# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = True
# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = True

if useDataTest :
    # Utilisation des données test
    lignes = []

    lignes.append("MMMSXXMASM")
    lignes.append("MSAMXMSMSA")
    lignes.append("AMXSXMAAMM")
    lignes.append("MSAMASMSMX")
    lignes.append("XMASAMXAMM")
    lignes.append("XXAMMXXAMA")
    lignes.append("SMSMSASXSS")
    lignes.append("SAXAMASAAA")
    lignes.append("MAMMMXMMMM")
    lignes.append("MXMXAXMASX")
else:
    # Utilisation des données du challlenge
    fichier = open("input.txt", "r")
    lignes = fichier.readlines()

import re

# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0

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

# Affiche le tableau tournée
print("\n Affichage des données : \n")
for j in range(len(data[1])):
    afficheLigne = ""
    for i in range(len(data)):
        afficheLigne = afficheLigne + data[i][j]
    print(afficheLigne)

if isLvlOne:

    print("\n recherche des X\n")
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "X":
                print(f" X trouvé en {i+1}:{j+1}")

                if j < 3:
                    print("   N  : Hors limite")
                elif data[i][j-1] == "M" and data[i][j-2] == "A" and data[i][j-3] == "S":
                    resultatChallenge += 1
                    print("   N  : OUI")
                else:
                    print("   N  : N")

                try:
                    if j < 3:
                        print("   NE : Hors limite")
                    elif data[i+1][j-1] == "M" and data[i+2][j-2] == "A" and data[i+3][j-3] == "S":
                        resultatChallenge += 1
                        print("   NE : OUI")
                    else:
                        print("   NE : N")
                except:
                    print("   NE : Hors limite")

                # recherche par la droite
                try:
                    if data[i+1][j] == "M" and data[i+2][j] == "A" and data[i+3][j] == "S":
                        resultatChallenge += 1
                        print("   E  : OUI")
                    else:
                        print("   E  : N")
                except:
                    print("   E  : Hors limite")

                try:
                    if data[i+1][j+1] == "M" and data[i+2][j+2] == "A" and data[i+3][j+3] == "S":
                        resultatChallenge += 1
                        print("   SE : OUI")
                    else:
                        print("   SE : N")
                except:
                    print("   SE : Hors limite")

                try:
                    if data[i][j+1] == "M" and data[i][j+2] == "A" and data[i][j+3] == "S":
                        resultatChallenge += 1
                        print("   S  : OUI")
                    else:
                        print("   S  : N")
                except:
                    print("   S  : Hors limite")

                try:
                    if i < 3:
                        print("   SO : Hors limite")
                    elif data[i-1][j+1] == "M" and data[i-2][j+2] == "A" and data[i-3][j+3] == "S":
                        resultatChallenge += 1
                        print("   SO : OUI")
                    else:
                        print("   SO : N")
                except:
                    print("   SO : Hors limite")


                if i < 3:
                    print("   O  : Hors limite")
                elif data[i-1][j] == "M" and data[i-2][j] == "A" and data[i-3][j] == "S":
                    resultatChallenge += 1
                    print("   O  : OUI")
                else:
                    print("   O  : N")


                if j < 3 or i < 3:
                    print("   NO : Hors limite")
                elif data[i-1][j-1] == "M" and data[i-2][j-2] == "A" and data[i-3][j-3] == "S":
                    resultatChallenge += 1
                    print("   NO : OUI")
                else:
                    print("   NO : N")
else:
    print("\n recherche des A\n")
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "A":
                print(f" A trouvé en {i + 1}:{j + 1}")

                try:
                    if i < 1 or j < 1:
                        print("   Hors limite")
                    else:
                        if data[i - 1][j - 1] == "M" and data[i + 1][j - 1] == "M" \
                                and data[i - 1][j + 1] == "S" and  data[i + 1][j + 1] == "S":
                            resultatChallenge += 1
                            print("   M-N : OUI")
                        else:
                           print("   M-N : N")

                        if data[i - 1][j - 1] == "S" and data[i + 1][j - 1] == "M" \
                                and data[i - 1][j + 1] == "S" and  data[i + 1][j + 1] == "M":
                            resultatChallenge += 1
                            print("   M-E : OUI")
                        else:
                           print("   M-E : N")

                        if data[i - 1][j - 1] == "S" and data[i + 1][j - 1] == "S" \
                               and data[i - 1][j + 1] == "M" and data[i + 1][j + 1] == "M":
                           resultatChallenge += 1
                           print("   M-S : OUI")
                        else:
                           print("   M-S : N")

                        if data[i - 1][j - 1] == "M" and data[i + 1][j - 1] == "S" \
                                and data[i - 1][j + 1] == "M" and  data[i + 1][j + 1] == "S":
                            resultatChallenge += 1
                            print("   M-O : OUI")
                        else:
                           print("   M-O : N")

                except:
                    print("   Hors limite")



if isLvlOne:
    print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")
else:
    print(f"\nRésultat du challenge partie 2 : {resultatChallenge}")