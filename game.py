# move generation including rack evaluation ?

import referee
import board
import solver
import dawg

DICTIONARY = "./official_scrabble_dict.txt"

blankRack = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
             'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
             'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0,
             'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, ' ': 0}


class game:
    def __init__(self, rack, spots, opponentScore=0, playerScore=0):
        self.rack = rack
        self.board = board.board(spots)
        self.referee = referee.referee(playerScore, opponentScore)
        self.dawg = dawg.dawg()
        WordCount = 0
        words = open(DICTIONARY, "rt").read().split()
        words.sort()
        for word in words:
            WordCount += 1
            # insert all words, using the reversed version as the data associated with
            # it
            self.dawg.insert(word, ''.join(reversed(word)))
            if (WordCount % 100) == 0:
                print("{0}\r".format(WordCount), end="")
        self.dawg.finish()


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
    solver = solver.solver(gameState)

    while True:
        letterCombo, spotCombo = solver.moveGenerator()
        print("This is the optimal move (given as the letters to be played, then the corresponding places in which to play them):")
        print("Letters: ", letterCombo)
        print("Spots: ", spotCombo)

        playerScore += gameState.referee.calcWordScore(letterCombo, spotCombo, gameState.board)
        print('Current score: ', playerScore)

        # remove from rack after move has been taken
        for letter in letterCombo:
            gameState.rack[letter] = gameState.rack[letter]-1

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
        print("valid starting spots", gameState.board.getValidConnections())
        gameState.board.printBoard()
        opponentWordScore = referee.referee.calcWordScore(
            opponentLetterDict, opponentSpotCombo, gameState.board)
        gameState.referee.opponentScore = opponentWordScore

        print('Opponent current score: ', opponentWordScore)



main()
