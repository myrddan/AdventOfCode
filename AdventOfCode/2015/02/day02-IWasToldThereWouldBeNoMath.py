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

# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0
resultatChallenge2 = 0

##################################################################"
##   Etape 1 Préparer mes données
##################################################################

for ligne in lignes:
    a,b,c = sorted(list(int(e) for e in ligne.strip().split('x')))
    resultatChallenge += 3*a*b + 2*b*c + 2*a*c

##################################################################
##   Etape 2 exploiter les données
##################################################################

for ligne in lignes:
    a,b,c = sorted(list(int(e) for e in ligne.strip().split('x')))
    resultatChallenge2 += a*2 + b*2 + a*b*c




print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")

print(f"\nRésultat du challenge partie 2 : {resultatChallenge2}")



