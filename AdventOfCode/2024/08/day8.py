
# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = False

# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = False

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

            dicAntennas.get(data[i][j]).append((i, j))

            if not isLvlOne:
                resultatChallenge += 1

print(dicAntennas)

print(f" Ajouts des \"antinode \"")


for item in dicAntennas.items():

    if isLvlOne:

        if verbose:
            print(f" Antennes {item[0]} :")

        while len(item[1])> 1:

            for i in range(1,len(item[1])):
                if verbose:
                    print("     ",item[1][0],":",item[1][i])

                posx = item[1][0][0] - (item[1][i][0] - item[1][0][0])
                posy = item[1][0][1] - (item[1][i][1] - item[1][0][1])

                if -1 < posx < len(data) and -1 < posy < len(data[0]):
                    if not data[posx][posy] == "#":
                        resultatChallenge += 1
                    if data[posx][posy] == ".":
                        data[posx][posy] = "#"
                    if verbose:
                        print("       x", posx, "y", posy," IN")
                elif verbose:
                    print("       x",posx,"y",posy," OUT")

                posx = item[1][0][0] + 2 * (item[1][i][0] - item[1][0][0])
                posy = item[1][0][1] + 2 * (item[1][i][1] - item[1][0][1])


                if -1 < posx < len(data) and -1 < posy < len(data[0]):
                    if not data[posx][posy] == "#":
                        resultatChallenge += 1
                    if data[posx][posy] == ".":
                        data[posx][posy] = "#"
                    if verbose:
                        print("       x", posx, "y", posy," IN")
                elif verbose:
                    print("       x",posx,"y",posy," OUT")

            del item[1][0]
    else:
        ###############################################"
        #  LVL 2
        if verbose:
            print(f" Antennes {item[0]} :")

        while len(item[1]) > 1:

            for i in range(1, len(item[1])):
                if verbose:
                    print("     ", item[1][0], ":", item[1][i])

                diffx = item[1][i][0] - item[1][0][0]
                diffy = item[1][i][1] - item[1][0][1]

                mul = 0

                while True:
                    mul += 1

                    posx = item[1][0][0] - mul * diffx
                    posy = item[1][0][1] - mul * diffy

                    if -1 < posx < len(data) and -1 < posy < len(data[0]):
                        if data[posx][posy] == ".":
                            data[posx][posy] = "#"
                            resultatChallenge += 1
                        if verbose:
                            print("       x", posx, "y", posy, " IN")
                    elif verbose:
                        print("       x", posx, "y", posy, " OUT")
                        break

                mul = 0

                while True:
                    mul += 1

                    posx = item[1][0][0] - mul * diffx
                    posy = item[1][0][1] - mul * diffy

                    posx = item[1][0][0] + ( 1 + mul ) * diffx
                    posy = item[1][0][1] + ( 1 + mul ) * diffy

                    if -1 < posx < len(data) and -1 < posy < len(data[0]):
                        if data[posx][posy] == ".":
                            data[posx][posy] = "#"
                            resultatChallenge += 1
                        if verbose:
                            print("       x", posx, "y", posy, " IN")
                    elif verbose:
                        print("       x", posx, "y", posy, " OUT")
                        break


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



