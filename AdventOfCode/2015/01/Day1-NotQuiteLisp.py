# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = False

# Affichage de log supplémentaire pour faciliter le debugage
# if verbose:
#     print("infos")
verbose = True

if useDataTest:
    # Utilisation des données test

    with open("input_test.txt", "r") as fichier:
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
    with open("input_challenge.txt", "r") as fichier:
        lignes = fichier.readlines()
# Création des variables qui vont stocker les résultats du challenge
resultatChallenge = 0
resultatChallenge2 = 0

##################################################################"
##   Etape 0  Mise en forme des données (optionnelle)
##################################################################

##################################################################"
##   Etape 1 et 2
## Il est ici possible de faire les deux étapes dans la même boucle
##################################################################
#####################
##   Solution 1 faire +1 -1
#####################


# Ajout étape 2
# Variable qui va compter le nombre d'instruction executés
cpt = 0

# Pour chaque lignes des données du challenge on fait :
for ligne in lignes:
    # Pour chaque caractère de la ligne d'instruction on fait :
    for c in ligne:


        # Si c'est "(" alors on monte d'un étage => resultatChallenge + 1
        if c == "(":
            resultatChallenge += 1

        # Si c'est ")" alors on descend d'un étage => resultatChallenge - 1
        if c == ")":
            resultatChallenge -= 1

        # Ajout étape 2
        # On incrémente le compteur d'instructions
        cpt += 1
        if resultatChallenge == -1 and resultatChallenge2 == 0:
            resultatChallenge2 = cpt

#####################
##   Solution 2 compter les +1 et les -1 puis faire la différence
##   NE fonctionne que pour l'étape 1
#####################

# Variable qui va compter les montées de niveau "("
nbMonte =0
# Variable qui va compter les descendes de niveau ")"
nbDescend = 0

# Pour chaque lignes des données du challenge on fait :
for ligne in lignes:
    # Pour chaque caractère de la ligne d'instruction on fait :
    for c in ligne:

        # Si c'est "(" alors on incrémente le compteur de montée
        if c == "(":
            nbMonte += 1

        # Si c'est ")" alors on incremente le compteur de descente
        if c == ")":
            nbDescend += 1
            
    if verbose:
        print(f"Résultat Solution 2 = {nbMonte-nbDescend}")

##################################################################
##   Affiche les résultats
##################################################################

print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")
print(f"\nRésultat du challenge partie 2 : {resultatChallenge2}")









