import alphaBetaPruning
import game

board = game.create()  # board creation
print(board)
game.whoIsFirst(board)
while not game.isFinished(board):
    if game.isHumTurn(board):
        game.inputMove(board)
    else:
        board = alphaBetaPruning.go(board)  # the agent turn
game.printState(board)

