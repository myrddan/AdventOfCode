import itertools

# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = False

# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = True

# Affichage de log supplémentaire pour faciliter le debugage
verbose = False

if useDataTest :
    puzleInput = "1"
    tour = 5
else:
    puzleInput = "1113222113"
    tour = 40

import re

# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0
resultatChallenge2 = 0

instruction = {}

##################################################################"
##   Etape 1
##################################################################
print("\nEtape 1 \n")

# Déclaration d'une fonction récursive qui décrémente un compteur
# à chaque appel et une fois arriver à zéro retourne le résultat.
# On va utiliser la même fonction pour les deux étapes
def lookAndSay(chaine, tour) -> str:
    # On décrémente le compteur
    tour -= 1
    # variable qui va contenir le descriptif de la chaine en paramètre
    say = ""
    # Variable qui va contenir la position dans la chaine
    i = 0
    # Tand qu'on a pas dépassé la fin de la chaine
    while i < len(chaine):
        # On prend le caractère courant
        nombre = chaine[i]
        count = 1
        j = 1
        # Tand qu'on trouve le même caractère, on avance dans la chaine
        while i+j < len(chaine) and chaine[i + j] == nombre:
            count += 1
            j += 1

        # une fois qu'on est sorti de la boucle, on a le nombre de caractère identique
        # On ajoute le nombre d'occurences puis le chiffre trouvé
        say += str(count)
        say += str(nombre)
        # On déplace la position avec le nombre de répétition.
        i = i + j

    if verbose:
        print(f" {chaine} << {say}")
    # Si tour = zéro alors j'ai effectué mon nombre de tour
    # Je retourne le descriptif de la chaine
    if tour == 0 :
        return say
    else:
        # Sinon je continue la récursive
        return lookAndSay(say,tour)


resultatChallenge = len(lookAndSay(puzleInput,tour))
##################################################################
##   Etape 2
##################################################################

print("\nEtape 2 \n")

resultatChallenge2 = len(lookAndSay(puzleInput,50))

print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")

print(f"\nRésultat du challenge partie 2 : {resultatChallenge2}")



