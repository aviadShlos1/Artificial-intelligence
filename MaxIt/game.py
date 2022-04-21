# Name: Aviad Shlosberg 314960881
#       Israel Schlesinger 201528247
# Exercise 2 Maxit Game using Alpha Beta Pruning Algorithm
import copy
import random as rd

# "Maxit Game" instructions:
''' 
MaxIt is played on a game board which looks like a grid (7x7 up to 10x10). 
Each cell in the game board contains a number which can be either positive or negative. 
The players take turns selecting numbers from the game board, 
these numbers are added to the players cumulative score (negative numbers lower the players score).
The rules for selecting numbers from the game board are quite simple. 
The player (that's you) can select any number along a horizontal row that the cursor is on. 
When you have selected a number, the cursor moves to that cell on the game board and 
the number at that location gets added to your score and removed from the board. 
Your opponent (the computer) then selects a number from the game board. 
The computer can only select numbers along the vertical column that the cursor is on. 
Play continues in this fashion until there is no move available (due to an empty row or column).
The object of the game is to have the highest score when the game ends. 
'''


TIE = 0  # The value of a tie
SIZE = 8  # the size of the board, you can modify it just here as you wish.
MAX_VAL = 15
MIN_VAL = -MAX_VAL
COMPUTER = MIN_VAL - 1  # Marks the computer's cells on the board
HUMAN = MAX_VAL + 1  # Marks the human's cells on the board
'''
The state of the game is represented by a list of 4 items:
0. The game board - a matrix (list of lists) of ints. Empty cells = 0,
   the comp's cells = COMPUTER and the human's = HUMAN
1. The heuristic value of the state.
2. Who's turn is it: HUMAN or COMPUTER
3. number of empty cells
'''


# Initializing the board
# Returns an empty board.
def create():
    flat_board = [rd.randint(MIN_VAL, MAX_VAL) for i in range(0, SIZE * SIZE)]  # fill the board
    board = [flat_board[i:i + SIZE] for i in range(0, SIZE * SIZE, SIZE)]  # cut the flatten board to nxn board
    score = {'human_score': 0, 'computer_score': 0}
    current_position = [rd.randint(0, SIZE - 1), rd.randint(0, SIZE - 1)]
    board[current_position[0]][current_position[1]] = 'X'  # you are here
    return [board, current_position, HUMAN, score]


# Return the heuristic value of s which determines the rules for selecting numbers.
# The heuristic calculates the best  step for the current state
# by calculating the big difference between a potential user move to the potential computer move.
# It takes into consideration all the options thinking deeply for the next moves.
# The more positive the result the better it is for max player and
# vise verse.
def value(s):
    return s[3]['computer_score'] - s[3]['human_score']


# random decision who plays first
def whoIsFirst(s):
    firstTurn = rd.randint(0, 1)
    if firstTurn == 1:
        s[2] = COMPUTER
        print('COMPUTER will play first')
        printState(s)
    else:
        s[2] == HUMAN
        print('USER will play first')

    print("Computer selects from the columns and user selects from the rows")


# Returns True iff it the human's turn to play
def isHumTurn(s):
    return s[2] == HUMAN


# Reads, enforces legality and executes the user's move.
def inputMove(s):
    printState(s)
    flag = True
    while flag:
        col = int(input(f"Enter your next move between 0 to {SIZE - 1}: "))
        row = s[1][0]
        if col < 0 or col >= len(s[0]) or isinstance(s[0][row][col], str):
            print("Illegal move. Please try again")
        else:
            flag = False
            makeMove(s, row, col)


# chooses the rows or the columns according to the player
# adding the scores
# switches turns
# and re-evaluates the heuristic value
# Assumes the move is legal.
def makeMove(s, row, col):

    if isHumTurn(s):
        s[3]['human_score'] += s[0][row][col]
    else:
        s[3]['computer_score'] += s[0][row][col]

    r = s[1][0]
    c = s[1][1]
    s[0][r][c] = ' '
    s[0][row][col] = 'X'  # marks the board
    s[1] = [row, col]

    if isHumTurn(s):  # Switch turns
        s[2] = COMPUTER
    else:
        s[2] = HUMAN


# returns a list of the next states of s
def getNext(s):
    cur_pos = s[1]
    s[0][cur_pos[0]][cur_pos[1]] = ' '
    new_states = []
    for i in range(0, SIZE):
        if not isHumTurn(s):
            # checking a legal move, insure the cell doesn't include a string (empty or X)
            if not isinstance(s[0][i][cur_pos[1]], str):
                temp = copy.deepcopy(s)
                makeMove(temp, i, cur_pos[1])
                new_states.append(temp)
        else:
            if not isinstance(s[0][cur_pos[0]][i], str):
                temp = copy.deepcopy(s)
                makeMove(temp, cur_pos[0], i)
                new_states.append(temp)
    return new_states


# Prints the board. The empty cells are printed as numbers = the cells name(for input)
# If the game ended prints who won.
def printState(s):
    print()
    print('human score is: ' + str(s[3]['human_score']))
    print('computer score is: ' + str(s[3]['computer_score']))
    print("The position in ", s[1], "marked by X")
    for row in range(SIZE):
        print()
        for col in range(SIZE):
            if s[0][row][col] == COMPUTER:
                print("  |", end="")
            elif s[0][row][col] == HUMAN:
                print("  |", end="")
            else:
                if isinstance(s[0][row][col], int):
                    print("%3d" % s[0][row][col], "|", end="")
                else:
                    print(f"  {s[0][row][col]} |", end="")
    print()
    if isFinished(s):
        # print(f"s={s}")

        # if the game ended prints who won.
        if s[4]['human_score'] > s[3]['computer_score']:
            print("You won!")
        elif s[4]['human_score'] < s[3]['computer_score']:
            print("Computer won!")
        else:
            print("It's a TIE")
        print('Human score is: ' + str(s[3]['human_score']))
        print('Computer score is: ' + str(s[3]['computer_score']))


# Boolean func checks if the game is finished
def isFinished(s):
    if s == 0:
        return False
    if s[2] == HUMAN:
        row = s[1][0]
        for i in range(0, SIZE):
            if isinstance(s[0][row][i], int):
                return False
    else:
        col = s[1][1]
        for i in range(0, SIZE):
            if isinstance(s[0][i][col], int):
                return False
    return True
