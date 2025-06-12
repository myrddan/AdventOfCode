import itertools

# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = False

# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = True

# Affichage de log supplémentaire pour faciliter le debugage
verbose = True
import hashlib

def md5_hash(input_string):
    # Créer un objet de hachage MD5
    md5_hash_object = hashlib.md5()

    # Mettre à jour l'objet de hachage avec la chaîne d'entrée encodée en bytes
    md5_hash_object.update(input_string.encode('utf-8'))

    # Obtenir la valeur hexadécimale du hachage
    return md5_hash_object.hexdigest()

# Exemple d'utilisation
input_string = "abcdef609043"
hashed_value = md5_hash(input_string)
print(f"MD5 hash de '{input_string}' est: {hashed_value}")

exit()
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

import re

# Méthode qui va tester si la chaine contient 3 voyelles
def isVoyelles(chaine : str):
    return len(re.findall(r"[aeiou]",chaine)) >= 3

# Méthode qui va tester si la chaine contient une lettre doublé
def isDoubles(chaine : str):
    return re.search(r"(\w)\1",chaine)

# Méthode qui va tester si la chaine contient une association interdite
def isInterdit(chaine : str):
    return re.search(r"(ab|cd|pq|xy)",chaine)

for ligne in lignes:
    if isVoyelles(ligne) and isDoubles(ligne) and not isInterdit(ligne):
        print(f"{ligne.strip()} > OK ")
        resultatChallenge += 1
    else:
        print(f"{ligne.strip()}  > BAD ")


##################################################################
##   Etape 2
##################################################################

# Méthode qui va tester si la chaine contient une lettre doublé
def isRepetitionSeq(chaine : str):
    return re.search(r"(\w\w).*\1",chaine)

# Méthode qui va tester si la chaine contient une lettre doublé
def isRepetitionLettre(chaine : str):
    return re.search(r"(\w)\w\1",chaine)

print("\nEtape 2 \n")
for ligne in lignes:
    if isRepetitionSeq(ligne) and isRepetitionLettre(ligne):
        print(f"{ligne.strip()} > OK ")
        resultatChallenge2 += 1
    else:
        print(f"{ligne.strip()}  > BAD ")



print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")

print(f"\nRésultat du challenge partie 2 : {resultatChallenge2}")



