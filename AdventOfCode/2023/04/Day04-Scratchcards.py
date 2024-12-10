




if False:
    lignes = []
    lignes.append("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    lignes.append("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19")
    lignes.append("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1")
    lignes.append("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83")
    lignes.append("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36")
    lignes.append("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")


#In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17)
# and eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53).
# Of the numbers you have, four of them (48, 83, 17, and 86) are winning numbers!
# That means card 1 is worth 8 points (1 for the first match, then doubled three times
# for each of the three matches after the first).
#
#     Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
#     Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
#     Card 4 has one winning number (84), so it is worth 1 point.
#     Card 5 has no winning numbers, so it is worth no points.
#     Card 6 has no winning numbers, so it is worth no points.
#
# So, in this example, the Elf's pile of scratchcards is worth 13 points.

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

sum = 0


for ligne in lignes:
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

    if nbWin > 0:
        sum = sum + 2 ** (nbWin-1)

print("sum :",sum)