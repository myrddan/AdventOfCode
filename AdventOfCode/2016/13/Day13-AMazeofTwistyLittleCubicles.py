
# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = False

# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = True

# Affichage de log supplémentaire pour faciliter le debugage
verbose = True

def getCase(x,y,favoriteNumber)->str:

    number = (x * x) + (3 * x) + (2 * x * y) + y + (y*y) + favoriteNumber
    binRep = str(bin(number))[2:]

    if verbose:
        print(f"x={x} y={y} number = {number} binrep ={binRep}")

    if binRep.count("1")%2==0:
        return '.'
    else:
        return "#"


def aff():
    print("")
    for ligne in lignes:
        print("".join(ligne))

if useDataTest:
    # Utilisation des données test

    # fichier = open("input_test.txt", "r")
    # lignes = fichier.readlines()
    lignes = []
    for y in range(7):
        lignes.append([])
        for x in range(10):
            lignes[y].append(getCase(x,y,10))
    start = (1, 1)
    end = (4, 7)
else:
    lignes = []
    for y in range(50):
        lignes.append([])
        for x in range(50):
            lignes[y].append(getCase(x,y,1364))

    aff()

    start = (1, 1)
    end = (39, 31)

import re

# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0

##################################################################"
##   Etape 1 Préparer mes données
##################################################################


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        # Noeud parent utiliser pour remonter le parcours
        self.parent = parent
        # Tuple contenant l'abscisse et l'ordonnée de la case
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(maze, start, end,wall):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    end_node = Node(None, end)

    # Contient la liste des noeuds à traiter
    open_list = []
    # Contient la liste des noeuds traités
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:


        # Le est placé dans la closed_list, afin de rechercher le plus petit poid on va commencer par sélectionner le premier
        # de la liste ouverte
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        if verbose:
            print(f" Nodes {current_node.position}")
            lignes[current_node.position[0]][current_node.position[1]] = "?"
            aff()

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        # for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] == wall:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            if new_node not in closed_list:
                children.append(new_node)

        # Loop through children
        for child in children:
            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = abs((child.position[0] - end_node.position[0] ) + (child.position[1] - end_node.position[1]))

            child.f = child.g + child.h
            if verbose:
                print(child.position, " h =", child.h)
            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

        # On a finit de traiter la case, on transfert le current de la liste open vers la closed

        open_list.pop(current_index)
        closed_list.append(current_node)





 # maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 #            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 #            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 #            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 #            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 #            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 #            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 #            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# print(lignes)



path = astar(lignes, start, end, "#")
for pos in path:
    lignes[pos[0]][pos[1]] = "O"

aff()
print(path)

resultatChallenge = len(path) -1


print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")
##################################################################
##   Etape 2 exploiter les données
##################################################################


# print(f"\nRésultat du challenge partie 2 : {np.sum(sum(data[:2]) > data[2])}")





