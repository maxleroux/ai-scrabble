import dawg

class solver:
    def __init__(self, game):
        self.game = game
        self.dawg = dawg()
        # 
    
    def rack_evaluation(self):
        return
    
    def move_generator(self):
        return
    # SIMPLE MOVE GENERATOR: loop first over all squares & try to find all moves 
    # that start on that square —> WalkDawg after it has been improved for handling 
    # of blanks, letters on board, edge limitations, and crosswords

    def isLast(self,edge):
        return
    
    def getChar(edge):
        return

    # this needs to also account for :
    # 1) using blanks
    # 2) handling of tiles on board
    # 3) checking for edge of board --> attachments method from scrabble-ai?
    # 4) handling of crossword constraints
    def traverseDAWG(nodeIndex):
        if nodeIndex == 0 :
            return
        
        edge = 0

        while True:
            if not solver.isLast(edge):
                return
            
            # idk how to do this 
            # it's supposed to be edge = dawg[nodeindex++]
            edge = dawg

            c = solver.getChar(edge)

            if (tileCounts[c]):
                tileCounts[c] = tileCounts[c] -1
                word[wordIndex++] = c

                if (isLegalWord(edge)):
                    anagramHandler(word, wordIndex)

                traverseDawg(getNextNode(edge))

                tileCounts[c]++
                wordIndex--

    
    

    