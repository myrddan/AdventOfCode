


# Après avoir vu le temps nécessaire  pour réaliser le challenge, j'ai réfléchie et compris que je pouvais le faire avec une récursive
# mais le temps nécessaire était toujours énorme, en voyant les temps de réponses des meilleurs, il devait exister une methode que je ne connaissais pas.
# L'ajout de cache à la fonction est magique.

# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = False

# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = True

# Affichage de log supplémentaire pour faciliter le debugage
verbose = True

from functools import cache

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

stones = [int(x) for x in lignes[0].split()]

@cache
def manageStone(stone,steps):
    if steps == 0:
        return 1
    if stone == 0:
        return manageStone(1,steps-1)
    if stone == "1":
        return manageStone(2024, steps - 1)

    strStone = str(stone)
    lenStone = len(strStone)

    if (lenStone % 2) == 1:
        return manageStone(stone * 2024, steps - 1)

    return manageStone(int(strStone[lenStone // 2:]),steps-1) \
           + manageStone(int(strStone[:lenStone//2]), steps - 1)


print(sum(manageStone(stone,25) for stone in stones))

print(sum(manageStone(stone,75) for stone in stones))
##################################################################
##   Etape 2 exploiter les données
##################################################################



