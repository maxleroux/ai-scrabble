import dawg

DICTIONARY = "./official_scrabble_dict.txt"

class solver:
    def __init__(self, game):
        self.game = game
        self.dawg = dawg.dawg()
        WordCount = 0
        words = open(DICTIONARY, "rt").read().split()
        words.sort() 
        for word in words:
            WordCount += 1
            # insert all words, using the reversed version as the data associated with
            # it
            self.dawg.insert(word, ''.join(reversed(word)))
            if ( WordCount % 100 ) == 0: print("{0}\r".format(WordCount), end="")
        self.dawg.finish()
        self.anagrams = []
        # 
    
    def rack_evaluation(self):
        return
    
    def move_generator(self):
        return
    # SIMPLE MOVE GENERATOR: loop first over all squares & try to find all moves 
    # that start on that square —> WalkDawg after it has been improved for handling 
    # of blanks, letters on board, edge limitations, and crosswords

    def isLast(self, edge):
        parent, current_edge, child = list(self.dawg.minimizedNodes.values()).index(edge)
        return child.final
    
    def getChar(self,edge):
        print("edge ", edge)
        return list(self.dawg.minimizedNodes.keys())[list(self.dawg.minimizedNodes.values()).index(edge)]

    def anagramHandler(self, word):
        self.anagrams.append(word)
        print(self.anagrams)

    # this needs to also account for :
    # 1) using blanks
    # 2) handling of tiles on board
    # 3) checking for edge of board --> attachments method from scrabble-ai?
    # 4) handling of crossword constraints
    def traverseDAWG(self, nodeIndex):
        print("hit 1")
        if nodeIndex == 1 :
            return
        
        word = ""
        wordIndex = 0
        print("hit 2")

        while True:
            print("hit 3")
            
            nodeIndex = nodeIndex+1
            print(self.dawg)
            # print(self.dawg.minimizedNodes['A'].edge)
            # edge = self.dawg.minimizedNodes[list(self.dawg.minimizedNodes.keys())[0]]
            print("root", self.dawg.root)
            print("edges", self.dawg.root.edges)
            edge = self.dawg.root.edges['A']


            c = self.getChar(edge)

            if (self.game.rack[c] != 0):
                self.game.rack[c] = self.game.rack[c]-1

                wordIndex = wordIndex+1
                word[wordIndex] = c

                if (self.dawg.lookup(word)):
                    self.anagramHandler(word)

                parent, current_edge, child = self.dawg.minimizedNodes.values().index(edge)
                self.traverseDAWG(child)

                self.dawg.rack[c] = self.dawg.rack[c]+1
                wordIndex = wordIndex-1
                print("hit 4")

            if self.isLast(edge):
                return

    
    

    