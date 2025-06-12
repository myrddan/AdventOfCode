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

instruction = {}

##################################################################"
##   Etape 1
##################################################################
print("\nEtape 1 \n")

for ligne in lignes:
    lenLigne = len(ligne.strip())
    lenPhrase = len(ligne.strip().encode().decode('unicode_escape')) - 2
    # print(f"{lenLigne} - {lenPhrase} = {lenLigne-lenPhrase}")
    resultatChallenge += lenLigne-lenPhrase

##################################################################
##   Etape 2
##################################################################

print("\nEtape 2 \n")

"""

En Python, la fonction intégrée repr(x) est utilisée pour obtenir une représentation sous forme de chaîne de caractères 
d'un objet x. Cette représentation est généralement une chaîne qui, si elle est passée à la fonction eval(), devrait
retourner un objet ayant la même valeur que x. 

Voici un exemple pour illustrer la différence entre repr() et str() :

s = "Bonjour\nMonde"
print(str(s))
# Sortie :
# Bonjour
# Monde

print(repr(s))
# Sortie : 'Bonjour\nMonde'

"""

import re

for ligne in lignes:
    # print(extended)
    lenLigne = len(ligne.strip())
    extended = re.sub('"', '"\"', repr(ligne.strip()))
    lenPhrase = len(extended)
    # print(f"{lenPhrase} - {lenLigne} = {lenLigne-lenPhrase}")
    resultatChallenge2 += lenPhrase - lenLigne

print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")

print(f"\nRésultat du challenge partie 2 : {resultatChallenge2}")



