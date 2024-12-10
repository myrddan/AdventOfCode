
import re

lignes = []
lignes.append("32T3K")
lignes.append("JJ5J5")
lignes.append("KK677")
lignes.append("KTJJT")
lignes.append("QQQJA")


onePairPattern  = r"([23456789TQKA])\1{1}"

for ligne in lignes:
    result = re.findall(onePairPattern,ligne)
    print(ligne,result)