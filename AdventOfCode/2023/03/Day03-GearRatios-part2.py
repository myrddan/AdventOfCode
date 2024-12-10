

def rechercheNumber(ligne, indexRecherche):
    print(ligne,indexRecherche)
    indexStart = indexRecherche
    indexEnd = indexRecherche

    for i in range(indexRecherche,len(ligne)):
        if ligne[i].isdigit():
            indexEnd = i
        else:
            break

    for i in range (indexRecherche,-1,-1):
        if ligne[i].isdigit():
            indexStart = i
        else:
            break
    print("Nombre :",ligne[indexStart:indexEnd+1])
    return int(ligne[indexStart:indexEnd+1])

if False:
    text = "467..114.. ...*...... ..35..633. ......#... 617*...... .....+.58. ..592..... ......755. ...$.*.... .664.598.."
    lignes = text.split(" ")
else:
    fichier = open("input", "r")
    lignes = fichier.readlines()

sum = 0
for i in range(len(lignes)):
    ligne = lignes[i]

    for j in range(len(ligne)):
        if ligne[j] == "*":
            cptTrouve = 0
            sumTemp = 1
            print("trouve",ligne[j],">>",i+1,":",j+1)
            #Recherche digit ligne au dessus
            if i > 0:
                topLeft = False
                topRight = False
                if lignes[i-1][j].isdigit():
                    if lignes[i - 1][j-1].isdigit():
                        topLeft = True
                    if lignes[i - 1][j + 1].isdigit():
                        topRight = True
                    cptTrouve +=1
                    sumTemp *= rechercheNumber(lignes[i - 1],j)

                if not topLeft and lignes[i - 1][j-1].isdigit():
                    sumTemp *= rechercheNumber(lignes[i - 1],j - 1)
                    cptTrouve += 1


                if not topRight and lignes[i - 1][j + 1].isdigit():
                    sumTemp *= rechercheNumber(lignes[i - 1],j + 1)
                    cptTrouve += 1

            #Recherche a gauche

            if j > 0:
                if  lignes[i ][j - 1].isdigit():
                    sumTemp *= rechercheNumber(ligne, j - 1)
                    cptTrouve += 1

            # Recherche a droite
            if j < len(ligne) -1:
                if  lignes[i ][j + 1].isdigit():
                    sumTemp *= rechercheNumber(ligne, j + 1)
                    cptTrouve += 1

            #recherche en dessous
            if i < len(lignes) -1 :
                bopLeft = False
                bopRight = False
                if lignes[i + 1][j].isdigit():
                    if lignes[i + 1][j - 1].isdigit():
                        bopLeft = True
                    if lignes[i + 1][j + 1].isdigit():
                        bopRight = True

                    sumTemp *= rechercheNumber(lignes[i + 1], j)
                    cptTrouve += 1

                if not bopLeft and lignes[i + 1][j - 1].isdigit():
                    sumTemp *= rechercheNumber(lignes[i + 1], j - 1)
                    cptTrouve += 1

                if not bopRight and lignes[i + 1][j + 1].isdigit():
                    sumTemp *= rechercheNumber(lignes[i + 1], j +1)
                    cptTrouve += 1

            if cptTrouve == 2:
                print("2 valeurs :",sumTemp)
                sum += sumTemp


print("Total :",sum)