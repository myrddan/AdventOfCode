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
else:
    # Utilisation des données du challlenge
    fichier = open("input_challenge.txt", "r")
    lignes = fichier.readlines()

    import json

    # Ouvrir et charger le fichier JSON
    with open("input_challenge.txt", 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)


import re

# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0
resultatChallenge2 = 0



##################################################################"
##   Etape 1
##################################################################
print("\nEtape 1 \n")


# On peut pour l'étape 1 utiliser les regex
import re

for ligne in lignes:
    print(sum( int(find) for find in re.findall(r"[-\d]+",ligne)))

# Il est aussi possible d'utiliser un objet JSON

def parcourJSON(pcompteur : int,valeur) -> int:
    compteur = pcompteur
    if isinstance(valeur, dict):

        for sous_cle, sous_valeur in valeur.items():
            if isinstance(sous_valeur, dict) or isinstance(sous_valeur, list):
                compteur += parcourJSON(0,sous_valeur)
            elif isinstance(sous_valeur, int):
                compteur += sous_valeur

            if isinstance(sous_cle, int):
                compteur += sous_cle

    elif isinstance(valeur, list):
        for element in valeur:
            if isinstance(element, dict) or isinstance(element, list):
                compteur += parcourJSON(0,element)
            elif isinstance(element, int):
                compteur += element
    return compteur

if not useDataTest:
    resultatChallenge = parcourJSON(0,donnees)

##################################################################
##   Etape 2
##################################################################

print("\nEtape 2 \n")

def parcourJSON2(pcompteur,valeur) -> int:
    compteur = pcompteur
    if isinstance(valeur, dict):
        compteurTemp = 0
        isRed = False
        for sous_cle, sous_valeur in valeur.items():
            if isinstance(sous_valeur, dict) or isinstance(sous_valeur, list):
                compteurTemp += parcourJSON2(0,sous_valeur)
            elif isinstance(sous_valeur, int):
                compteurTemp += sous_valeur
            elif isinstance(sous_valeur, str) and sous_valeur == "red":
                isRed = True

            if isinstance(sous_cle, int):
                compteurTemp += sous_cle

        if not isRed:
            compteur += compteurTemp

    elif isinstance(valeur, list):
        for element in valeur:
            if isinstance(element, int):
                compteur += element
            elif isinstance(element, dict) or isinstance(element, list):
                compteur += parcourJSON2(0,element)
    return compteur


if not useDataTest:
    resultatChallenge2 = parcourJSON2(0,donnees)

print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")

print(f"\nRésultat du challenge partie 2 : {resultatChallenge2}")



