
import re
import functools
class hand():
    def __init__(self):
        self.cards = ""
        self.cardsNonOrdered = ""
        self.bid = 0
        self.rank = -1

    def __lt__(self, other):
        for i in range(5):
            result = compareCards(self.cards[i], other.cards[i])
            if result != 0:
                return result

        return 0

    def __repr__(self):
        return self.cards




listCards = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
def compareCards(x, y):
    return listCards.index(x) - listCards.index(y)


def compareHands(hand1,hand2):
    for i in range(5):
        result = compareCards(hand1.cardsNonOrdered[i], hand2.cardsNonOrdered[i])
        if result != 0:
            return result

    return 0

def sortList(list):
    pos = 0
    while True:
        minIndex = pos

        # print("pos ",pos," ",list)
        maxIndex = len(list) - pos - 1
        for i in range(pos,len(list)- pos ):
            if  compareHands(list[i],list[minIndex]) < 0:
                minIndex = i

            if compareHands(list[i], list[maxIndex]) > 0:
                maxIndex = i

        if maxIndex == pos:
            maxIndex = minIndex

        if minIndex != pos:
            temp = list[pos]
            list[pos] = list[minIndex]
            list[minIndex] = temp

        if maxIndex != len(list) - pos - 1:
            temp = list[len(list) - pos - 1]
            list[len(list) - pos - 1] = list[maxIndex]
            list[maxIndex] = temp

        if pos >=len(list) - pos:
            break

        pos += 1

# Initialisation avec mes données test
if False:
    lignes = []
    lignes.append("32T3K 765")
    lignes.append("T55J5 684")
    lignes.append("KK677 28")
    lignes.append("KTJJT 220")
    lignes.append("QQQJA 483")

else:
    fichier = open("input", "r")
    lignes = fichier.readlines()



# Import des données dans la liste des mains
hands = []
for ligne in lignes:
    h = hand()
    h.cardsNonOrdered = ligne[0:5]
    temp = []
    for c in ligne[0:5]:
        temp.append(c)
    temp = sorted(temp, key=functools.cmp_to_key(compareCards))

    for c in temp:
        h.cards += c

    h.bid = int(ligne[6:])
    hands.append(h)

# trie par type de niveau de main
allList = []

fiveOfAKind = []
allList.append(fiveOfAKind)
fiveOfAKindPattern = r"(\w)\1{4}"

fourOfAKind = []
fourOfAKindPattern = r"(\w)\1{3}"
allList.append(fourOfAKind)

fullHouse = []
allList.append(fullHouse)

threeOfAKind = []
threeOfAKindPattern = r"(\w)\1{2}"
allList.append(threeOfAKind)

twoPair = []
allList.append(twoPair)

onePair = []
onePairPattern  = r"(\w)\1{1}"
allList.append(onePair)

highCard = []
allList.append(highCard)

for h in hands:
    if len(re.findall(fiveOfAKindPattern, h.cards))==1:
        fiveOfAKind.append(h)
        # print("fiveOfAKind ",h.cards)
    elif len(re.findall(fourOfAKindPattern, h.cards))==1:
        fourOfAKind.append(h)
        # print("fourOfAKind ", h.cards)
    elif len(re.findall(onePairPattern, h.cards))==2 and len(re.findall(threeOfAKindPattern, h.cards))==1:
        fullHouse.append(h)
        # print("fullHouse ", h.cards)
    elif len(re.findall(threeOfAKindPattern, h.cards))==1:
        threeOfAKind.append(h)
        # print("threeOfAKind ", h.cards)
    elif len(re.findall(onePairPattern, h.cards))==2:
        twoPair.append(h)
        # print("twoPair ", h.cards)
    elif len(re.findall(onePairPattern, h.cards))==1:
        onePair.append(h)
        # print("onePair ", h.cards)
    else:
        highCard.append(h)
        # print("highCard ", h.cards)

cpt = len(hands)
sum = 0

for list in allList:
    sortList(list)
    print(list)
    for h in list:
        sum += h.bid * (cpt)
        # print(f" rang {cpt} cards {h.cards} bid {h.bid} total {cpt*h.bid} sum {sum}")
        print(h.cards)
        cpt -= 1

print("sum ",sum)






