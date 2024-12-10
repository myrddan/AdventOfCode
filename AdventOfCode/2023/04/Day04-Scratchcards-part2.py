




if False:
    lignes = []
    lignes.append("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    lignes.append("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19")
    lignes.append("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1")
    lignes.append("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83")
    lignes.append("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36")
    lignes.append("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")

    LenWinningNumber = 5
    LenPlayNumber = 8
    IndexWin = 8
    IndexPlay = 25
else:
    #Card   1: 20 72 30 38 18 65  6 55 70 27 | 12 28 47 50 60 17 14 25 41 95 66 88 61 52 76  5 23 77 31 32 99 89 53 54 96
    fichier = open("input", "r")
    lignes = fichier.readlines()
    LenWinningNumber = 10
    LenPlayNumber = 25
    IndexWin = 10
    IndexPlay = 42

ListNbScrathCard = []
for ligne in lignes :
    ListNbScrathCard.append(1)

sum = 0


for indexLigne in range(len(lignes)):
    print(ListNbScrathCard)
    ligne = lignes[indexLigne]
    winningNumber = []
    nbWin = 0

    for i in range(LenWinningNumber):
        indexDeb = IndexWin + (3 * i)
        indexFin = IndexWin + 2 + (3 * i)
        winningNumber.append(int(ligne[indexDeb:indexFin]))

    for j in range(LenPlayNumber):
        indexDeb = IndexPlay + (3 * j)
        indexFin = IndexPlay + 2 + (3 * j)
        playNumber = int(ligne[indexDeb:indexFin])

        if playNumber in winningNumber:
            nbWin += 1

    for j in range(ListNbScrathCard[indexLigne]):
        for i in range(nbWin):
            if indexLigne + i + 1 < len(ListNbScrathCard):
                ListNbScrathCard[indexLigne + i + 1 ] += 1

print(ListNbScrathCard)
for nb in ListNbScrathCard:
    sum += nb

print("sum :",sum)