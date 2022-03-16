# Aviad Shlosberg
# 314960881

'''
The state is a list of 2 items: the board, the path
The target is :
012
345
678

'''
import random
import math


# returns a random board nXn
def create(n):
    b = list(range(n * n))                   # b is the board itself. A vector that represents a matrix.
    m = "<>v^"                               # m is "<>v^"- for every possible move (left, right , down, up)
    for i in range(n ** 3):                  # makes n^3 random moves
        if_legal(b, m[random.randrange(4)])  # calling the "if legal" func with random move
    return [b, ""]                           # at the beginning "" is an empty path, later on path
    # return [[4, 3, 7, 5, 8, 6, 1, 0, 2], ""]
    # contains the path that leads from the initial state to the current


def get_next(x):  # returns a list of the children states of x
    ns = []  # the next state list
    for i in "<>v^":
        s = x[0][:]  # [:] - copies the board in x[0]
        if_legal(s, i)  # try to move in direction i
        # checks if the move was legal and...
        if s.index(0) != x[0].index(0) and \
                (x[1] == "" or x[1][-1] != "><^v"["<>v^".index(i)]):  # check if it's the first move
            ns.append([s, x[1] + i])  # appends the new state to ns
    return ns


def path_len(x):
    return len(x[1])


def is_target(x):
    n = len(x[0])  # the size of the board
    return x[0] == list(range(n))  # list(range(n)) is the targe state


#############################
def if_legal(b, m):                   # gets a board and a move and makes the move if it's legal
    n = int(math.sqrt(len(b)))        # the size of the board is nXn
    index = b.index(0)                    # index is the place of the empty tile (0)
    # index%n is number between 0-(n-1)
    if index % n > 0 and m == "<":        # left move = checks if the empty tile is not in the first col
        b[index] = b[index - 1]               # swap x[index] and x[index-1]...
        b[index - 1] = 0  # ... and move the empty tile to the left
    elif index % n < n - 1 and m == ">":  # right move = check if the empty tile is not in the n's col
        b[index] = b[index + 1]
        b[index + 1] = 0
    elif index >= n and m == "^":         # up move = check if the empty tile is not in the first row
        b[index] = b[index - n]
        b[index - n] = 0
    elif index < n * n - n and m == "v":  # down move = heck if the empty tile is not in the n's row
        b[index] = b[index + n]
        b[index + n] = 0


# This is your HW
def hdistance(s):
    """
       This func receives a puzzle board state and sums the distances of the misplaced tiles
       :param s: puzzle board current state
       :return: the distances sum of the misplaced tiles
    """
    distance = 0
    n = int(math.sqrt(len(s)))  # the size of the board is nXn
    for number in s[0]:
        horizDist = abs(s[0].index(number) % n - number % n)  # to find the absolute horizontal distance
        verticDist = abs(number//n-s[0].index(number)//n)     # to find the absolute vertical distance
        distance += max(horizDist, verticDist)
    return distance


# -------------Question 2--------------
# The proposed heuristic is admissible , because it's distance is
# smaller or equal than the actual distance


# -------------Question 3--------------
# The program did much better than the program introduced in class.
# My program: [1330, 571]
# Class program: [4660, 2069]
# The reason for the improvement is that my heuristic is closer to the actual distance.
# While the class program checked if every tile is located in its place, our program checks the distance too
