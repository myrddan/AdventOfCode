# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = False
# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = False

if useDataTest :
    # Utilisation des données test
    lignes = []
    if isLvlOne:
        lignes.append("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
    else:
        lignes.append("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
else:
    # Utilisation des données du challlenge
    fichier = open("input.txt", "r")
    lignes = fichier.readlines()

import re

# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0

# Boolean utilisé pour la seconde partie
# Il sert à ne prendre en compte que les mul actif
# On active lorsqu'on trouve l'instruction "do()"
# On desactive lorsqu'on trouve l'instruction "don't()"
isEnabled = True

for ligne in lignes:
    if isLvlOne:
        # Utilisation d'une expression régulière pour extraire les mul() avec le bon format
        for instructions in re.findall(r"mul\(\d+,\d+\)", ligne):
            # Utilisation d'une expression régulière pour extraire les caractères
            # Exemple ["mul","2","4"]
            numbers = re.findall(r"\w+", instructions)

            # Calcule de la multiplication des deux nombres trouvés
            calcul = int(numbers[1]) * int(numbers[2])

            # On affiche chaque ligne pour faciliter le debug
            print(numbers, " > ", calcul)

            # On ajoute le calcul dans la somme résultat du challenge
            resultatChallenge += calcul
    else:
        # Utilisation d'une expression régulière pour extraire les mul() avec le bon format ou les "don't()" ou les "do()"
        # Le hors en regex s'écrit avec | (pipe)
        for instructions in re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)",ligne):
            # Si on trouve l'inscruction don't(), on deactive la prise en compte des mul
            if instructions.startswith("don't()"):
                isEnabled = False
                print("DISABLED")
            # Si on trouve l'inscruction do(), on active la prise en compte des mul
            elif instructions.startswith("do()"):
                isEnabled = True
                print("ENABLED")
            # Dans else, on aura forcément une instruction mul
            else:
                numbers = re.findall(r"\w+",instructions)
                calcul = 0
                # On ne fait le calcul que si enabled est à vrai.
                # ça permet d'afficher zero et de voir que le regex trouve bien les bon mul mais ne les prend pas en compte
                if isEnabled:
                    calcul = int(numbers[1]) * int(numbers[2])
                print(numbers," > ",calcul)

                # On ajoute le calcul dans la somme résultat du challenge
                resultatChallenge += calcul

if isLvlOne:
    print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")
else:
    print(f"\nRésultat du challenge partie 2 : {resultatChallenge}")