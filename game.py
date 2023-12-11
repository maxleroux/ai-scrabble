# move generation including rack evaluation ?

import referee
import board
import solver

blankRack = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
                  'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
                  'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0,
                  'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

class game:
    def __init__(self, rack, spots, opponentScore = 0, playerScore = 0):
        self.rack = rack
        self.board = board.board(spots)
        self.referee = referee.referee(playerScore, opponentScore)

def main():
    print("Hi! Please input:")
    print("1) the tiles that are on the rack, as a string containing all letters")
    rackInput = input().upper()
    rackMap = blankRack
    for letter in rackInput:
        rackMap[letter] = rackMap[letter]+1
    print("2) your opponent's score")
    opponentScore = int(input())
    print("3) your score")
    playerScore = int(input())
    print("4) the current state of the board (if there are no tiles on the board, just hit enter)")
    currentBoardState = input()
    gameState = game(rackMap, currentBoardState, opponentScore, playerScore)
    gameState.board.printBoard()

    # output: 
    # optimal move
    # remove from rack after move has been taken

    print('Current score: ', playerScore)
    
    # take in the new tiles to put on the players rack and update the rack
    print("Please input the tiles that were drawn after this turn:")
    newTiles = input().upper()
    for letter in newTiles:
        gameState.rack[letter] = gameState.rack[letter]+1
    print(gameState.rack)

    # take in the move the opponent makes, and update the board and their score accordingly
    opponentLetterDict = {}
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
            spot = int(currentInput[1:len(currentInput)])
            letter = currentInput[0:1]
            opponentLetterDict[spot] = letter
            opponentLetterCombo.append(letter)
            opponentSpotCombo.append(spot)

                
    gameState.board.updateBoard(opponentLetterCombo, opponentSpotCombo)
    gameState.board.printBoard()
    opponentWordScore = referee.referee.calcWordScore(opponentLetterDict, opponentSpotCombo, gameState.board)
    gameState.referee.opponentScore = opponentWordScore

    print('Opponent current score: ', opponentWordScore)

    gameSolver = solver.solver(gameState)
    gameSolver.traverseDAWG(0)

    # loop the last like 4 things


main()