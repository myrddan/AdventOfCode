

# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = False
# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = False

if useDataTest:
    # Utilisation des données test
    lignes = []
    lignes.append("3   4")
    lignes.append("4   3")
    lignes.append("2   5")
    lignes.append("1   3")
    lignes.append("3   9")
    lignes.append("3   3")
else:
    # Utilisation des données du challlenge
    fichier = open("input.txt", "r")
    lignes = fichier.readlines()


# Création d'une variable qui va stocker la somme des différences entre les nombres des deux jeux de test.
resultatChallenge = 0



##################################################################"
##   Etape 1 Préparer mes données
##################################################################
# Je vais ici parcourir mes données ligne par ligne
# Pour chaque ligne je vais récuperer les nombre de gauche et celui de droite et les stocker dans deux listes
jeuTest1 = []
jeuTest2 = []

# Pour chaque ligne de ma liste de lighes je fait :
for ligne in lignes:
    # Les données test et les données du challenge sont de tailles différentes
    # Je pourrais séparer la ligne en utilisant en séparateur l'espace
    # Mais les donnés étant de taille fixe, je peut extraire avec les index des caractères
    if useDataTest:
        jeuTest1.append(int(ligne[0:1]))
        jeuTest2.append(int(ligne[-1]))
    else:
        jeuTest1.append(int(ligne[0:5]))
        jeuTest2.append(int(ligne[-6:]))

# Il est important de vérifier à chaque étape qu'on a bien les bonnes valeurs
# J'ajoute des prints après chaque traitement
print(jeuTest1)
print(jeuTest2)

##################################################################
##   Etape 2 exploiter les données
##################################################################
if isLvlOne:
    # Je trie les listes par ordre croissant (trie par défaut, pas de paramètre nécessaire)
    jeuTest1.sort()
    jeuTest2.sort()

    print(jeuTest1)
    print(jeuTest2)

    # Les listes sont ordonnées et ont la même taille.
    # On peut donc utiliser un même compteur pour récupérer une valeur dans chaque liste
    for i in range(len(jeuTest1)):
        # On recherche la différence, avec la fonction abs() on récupère la valeur absolue ainsi,
        # si la différence est -2 alors on ajoutera bien 2 à la somme
        diff = abs(jeuTest1[i] - jeuTest2[i])
        resultatChallenge += diff

        print(f"{i+1} : {jeuTest1[i]} - {jeuTest2[i]} = {diff}")

    # On affiche la somme
    print(f"\nSomme des différence : {resultatChallenge}")
else:
    # Pas besoin de trier les listes pour la seconde partie.
    # Pour chaque valeurs de la colonne de gauche je recherche combien de fois je la trouve dans la
    # colonne de droite. Je multiplie le valeur par le nombre de fois ou je l'ai trouvé puis je rajoute ce résultat
    # dans la somme global.

    # Pour l'affiche je vais utiliser le numéro de ligne, j'utilise donc un for i in range...
    # Je pourrais utiliser remplacer par la ligne suivante :
    # for leftNumber in jeuTest1:
    for i in range(len(jeuTest1)):
        leftNumber = jeuTest1[i]
        compteur = 0

        for rightNumber in jeuTest2:
            if leftNumber == rightNumber:
                compteur += 1


        print(f"{i+1} {leftNumber} : {compteur}")

        if compteur > 0:
            calcule = leftNumber * compteur
            resultatChallenge += calcule
            print(f"Ajout à la somme de : {calcule}")

    print(f"\nSomme des multiplications : {resultatChallenge}")