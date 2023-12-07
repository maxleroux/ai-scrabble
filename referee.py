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
letterPointDict = {'A': 9, 'B': 2, 'C': 2, 'D': 3, 'E': 12, 'F': 2,
                   'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4,
                   'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6,
                   'S': 4, 'T': 6, 'U': 3, 'V': 2, 'W': 2, 'X': 1,
                   'Y': 2, 'Z': 1}

class referee:
    def __init__(self):
        self.letterBag = []
        for letter in letterPointDict.keys():
            for _ in range(letterPointDict[letter]):
                self.letterBag.append(letter)

    # draws the given number of letters from the remaining tiles in the letter bag, or all of the tiles left in the bag if
    # that quantity is smaller than the requested number of tiles
    def drawLetters(self, num):
        drawnLetters = ''
        if num <= len(self.letterBag):
            for _ in range(num):
                x = random.random()
                index = int(math.floor(x*len(self.letterBag) / 1))
                drawnLetters += self.letterBag[index]
                self.letterBag.pop(index)
        else:
            for letter in self.letterBag:
                drawnLetters += letter
            self.letterBag = []
        return drawnLetters

    # get the amount of points the given letterCombo is worth based on the tiles played and their locations (spotCombo)
    def calcWordScore(spotCombo, letterCombo, board):
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
                if spot in letterPointDict.keys():
                    wordScore += 2 * letterPointDict[letterCombo[spot]]
                else:
                    wordScore += 2 * letterPointDict[board[spot]]
            elif spot in tripleLetter:
                if spot in letterPointDict.keys():
                    wordScore += 3 * letterPointDict[letterCombo[spot]]
                else:
                    wordScore += 3 * letterPointDict[board[spot]]
            else:
                if spot in letterPointDict.keys():
                    wordScore += letterPointDict[letterCombo[spot]]
                else:
                    wordScore += letterPointDict[board[spot]]
                
        return wordScore * (2**doubleWordSpace) * (3**tripleWordSpace)
