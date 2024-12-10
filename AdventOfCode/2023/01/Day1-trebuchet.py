

if True :
    fichier = open("input.txt", "r")
    lignes = fichier.readlines()
else:
    #text = ("1abc2 pqr3stu8vwx a1b2c3d4e5f treb7uchet")
    text = "two1nine eightwothree abcone2threexyz xtwone3four 4nineeightseven2 zoneight234 7pqrstsixteen"
    lignes = text.split(" ")

sum = 0

for ligne in lignes:
    print("Line >> ",ligne)
    digit1 = ""
    indexDigit1 = len(ligne)

    digit2 = ""
    indexDigit2 = -1

    try:
        # trouver le premier digit de la ligne
        for i in range(len(ligne)):
            if ligne[i].isdigit():
                digit1 = ligne[i]
                indexDigit1 = i
                print("digit1 ",ligne[i]," : ",i)
                break




        find1 = ligne.find("one")
        print("find one : ",find1)
        if find1 > -1 and find1 < indexDigit1:
            indexDigit1 = find1
            digit1 = "1"
        find1 = ligne.find("two")
        print("find two : ", find1)
        if find1 !=-1 and find1 < indexDigit1:
            indexDigit1 = find1
            digit1 = "2"
            print("change digit1 : ", digit1,":",indexDigit1)
        find1 = ligne.find("three")
        print("find three : ", find1)
        if find1 !=-1 and find1 < indexDigit1:
            indexDigit1 = find1
            digit1 = "3"
        find1 = ligne.find("four")
        print("find four : ", find1)
        if find1 !=-1 and find1 < indexDigit1:
            indexDigit1 = find1
            digit1 = "4"
        find1 = ligne.find("five")
        print("find five : ", find1)
        if find1 !=-1 and find1 < indexDigit1:
            indexDigit1 = find1
            digit1 = "5"
        find1 = ligne.find("six")
        print("find six : ", find1)
        if find1 !=-1 and find1 < indexDigit1:
            indexDigit1 = find1
            digit1 = "6"
        find1 = ligne.find("seven")
        print("find seven : ", find1)
        if find1 !=-1 and find1 < indexDigit1:
            indexDigit1 = find1
            digit1 = "7"
        find1 = ligne.find("eight")
        print("find eight : ", find1)
        if find1 !=-1 and find1 < indexDigit1:
            indexDigit1 = find1
            digit1 = "8"
        find1 = ligne.find("nine")
        print("find nine : ", find1)
        if find1 !=-1 and find1 < indexDigit1:
            indexDigit1 = find1
            digit1 = "9"


        for i in range(len(ligne)-1,-1,-1):
            if ligne[i].isdigit():
                digit2 = ligne[i]
                indexDigit2 = i
                print("digit2 ", ligne[i], " : ", i)
                break

        find1 = ligne.rfind("one")
        print("rfind one : ", find1)
        if find1 > indexDigit2:
            indexDigit2 = find1
            digit2 = "1"
        find1 = ligne.rfind("two")
        print("rfind two : ", find1)
        if find1 > indexDigit2:
            indexDigit2 = find1
            digit2 = "2"
        find1 = ligne.rfind("three")
        print("rfind three : ", find1)
        if find1 > indexDigit2:
            indexDigit2 = find1
            digit2 = "3"
        find1 = ligne.rfind("four")
        if find1 > indexDigit2:
            indexDigit2 = find1
            digit2 = "4"
        find1 = ligne.rfind("five")
        if find1 > indexDigit2:
            indexDigit2 = find1
            digit2 = "5"
        find1 = ligne.rfind("six")
        if find1 > indexDigit2:
            indexDigit2 = find1
            digit2 = "6"
        find1 = ligne.rfind("seven")
        if find1 > indexDigit2:
            indexDigit2 = find1
            digit2 = "7"
        find1 = ligne.rfind("eight")
        if find1 > indexDigit2:
            indexDigit2 = find1
            digit2 = "8"
        find1 = ligne.rfind("nine")
        if find1 > indexDigit2:
            indexDigit2 = find1
            digit2 = "9"

        # trouver le dernier digit de la ligne
        sum = sum + int(digit1 + digit2)
        print(digit1, digit2, ">>", ligne)
    except:
        print("ERROR >>",ligne)


print("sum ",sum)