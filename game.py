# move generation including rack evaluation ?

import referee
import board

class game:
    def __init__(self, rack, spots, opponentScore = 0, playerScore = 0):
        self.rack = rack
        self.board = board.board(spots)
        self.referee = referee.referee(playerScore, opponentScore)

def main():
    print("Hi! Please input:")
    print("1) the tiles that are on the rack, as a string containing all letters")
    rack = input()
    print("2) your opponent's score")
    opponentScore = int(input())
    print("3) your score")
    playerScore = int(input())
    print("4) the current state of the board (if there are no tiles on the board, just hit enter)")
    currentBoardState = input()
    gameState = game(rack, currentBoardState, opponentScore, playerScore)
    gameState.board.printBoard()

    # output: 
    # optimal move
    
    # take in the new tiles to put on the players rack and update the rack
    print("Please input the tiles that were drawn after this turn:")
    gameState.rack = input() + gameState.rack
    print(gameState.rack)

    # take in the move the opponent makes, and update the board and their score accordingly
    opponentLetterCombo = []
    opponentSpotCombo = []
    print("""Please input the move the opponent has made: input a letter, press enter, input the corresponding 
    spot (0-224) on the game board at which that letter is being placed, and press enter again; do this for all letters and their 
    places, then type the word done when all letters in the move have been entered. """)
    while True:
        currentInput = input()
        if currentInput == "done":
            break
        else:
            if currentInput in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                opponentLetterCombo.append(currentInput)
            else:
                opponentSpotCombo.append(int(currentInput))

    print(opponentLetterCombo)
    print(opponentSpotCombo)
                
    gameState.board.updateBoard(opponentLetterCombo, opponentSpotCombo)
    gameState.board.printBoard()
    opponentWordScore = referee.referee.calcWordScore(opponentLetterCombo, opponentSpotCombo, gameState.board)
    gameState.referee.opponentScore = opponentWordScore

    # output:
    # optimal move
    

    # loop the last like 4 things


main()