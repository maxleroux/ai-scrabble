# game rules of a typical Scrabble game
import random
import math

# where the extra scoring boxes are located on the board, 0 being the top left square, 1 being the square directly
    # to the right of that, 15 being the first square on the second row, etc.
tripleWord = [0, 7, 14, 105, 119, 210, 217, 224]
doubleWord = [16, 28, 32, 42, 48, 56, 64, 70,
              154, 160, 168, 176, 182, 192, 196, 208]
doubleLetter = [3, 11, 36, 38, 45, 52, 59, 92, 96, 98, 102, 108,
                116, 122, 126, 128, 132, 165, 172, 179, 186, 188, 213, 221]
tripleLetter = [20, 24, 76, 80, 84, 88, 136, 140, 144, 148, 200, 204]
letterPointDict = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2,
                  'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1,
                  'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
                  'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, ' ': 0}

class referee:
    def __init__(self, playerScore = 0, opponentScore = 0):
        self.selfScore = playerScore
        self.opponentScore = opponentScore

    # get the amount of points the given letterCombo is worth based on the tiles played and their locations (spotCombo)
    def calcWordScore(letterCombo, spotCombo, board):
        wordScore = 0
        doubleWordSpace = 0
        tripleWordSpace = 0

        if len(letterCombo) == 7:
            wordScore += 50
    
        for spot in spotCombo:
            if spot in doubleWord:
                doubleWordSpace += 1
            elif spot in tripleWord:
                tripleWordSpace += 1
            if spot in doubleLetter:
                if spot in letterCombo.keys():
                    wordScore += 2 * letterPointDict[letterCombo[spot].upper()]
                else:
                    wordScore += 2 * letterPointDict[board[spot].upper()]
            elif spot in tripleLetter:
                if spot in letterCombo.keys():
                    wordScore += 3 * letterPointDict[letterCombo[spot].upper()]
                else:
                    wordScore += 3 * letterPointDict[board[spot].upper()]
            else:
                if spot in letterCombo.keys():
                    wordScore += letterPointDict[letterCombo[spot].upper()]
                else:
                    wordScore += letterPointDict[board[spot].upper()]
        
        

        return wordScore * (2**doubleWordSpace) * (3**tripleWordSpace)