import itertools

# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre

# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = True

# Affichage de log supplémentaire pour faciliter le debugage
verbose = True
import hashlib

# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0
resultatChallenge2 = 0

##################################################################"
##   Etape 1
##################################################################

import re

def md5_hash(input_string):
    # Créer un objet de hachage MD5
    md5_hash_object = hashlib.md5()

    # Mettre à jour l'objet de hachage avec la chaîne d'entrée encodée en bytes
    md5_hash_object.update(input_string.encode('utf-8'))

    # Obtenir la valeur hexadécimale du hachage
    return md5_hash_object.hexdigest()


puzzleInput = "yzbqklnj"
cpt = 0

while True:

    # Exemple d'utilisation
    input_string = puzzleInput + str(cpt)
    hashed_value = md5_hash(input_string)

    if hashed_value.startswith("00000") and resultatChallenge == 0:
        print(f"MD5 hash de '{input_string}' est: {hashed_value}")
        resultatChallenge = cpt

    if hashed_value.startswith("000000"):
        print(f"MD5 hash de '{input_string}' est: {hashed_value}")
        resultatChallenge2 = cpt
        break

    cpt += 1

##################################################################
##   Etape 2
##################################################################

print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")

print(f"\nRésultat du challenge partie 2 : {resultatChallenge2}")



