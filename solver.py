import dawg

DICTIONARY = "./official_scrabble_dict.txt"

class solver:
    def __init__(self, game):
        self.game = game
        self.dawg = game.dawg
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
    def traverseDAWG(self, node):
        print("hit 1")
        if node.final == True :
            return
        
        word = ""
        wordIndex = 0
        print("hit 2")

        while True:
            print("hit 3")
            
            # nodeIndex = nodeIndex+1
            print(self.dawg)
            # print(self.dawg.minimizedNodes['A'].edge)
            # edge = self.dawg.minimizedNodes[list(self.dawg.minimizedNodes.keys())[0]]
            print("root", self.dawg.root)
            print("edges", node.edges.items())
            label, child = node

            # for letter in word:
            # if letter not in node.edges: return None
            # for label, child in sorted(node.edges.items()):
            #     if label == letter: 
            #         if node.final: skipped += 1
            #         node = child
            #         break
            #     skipped += child.count

            if (self.game.rack[label] != 0):
                self.game.rack[label] = self.game.rack[label]-1

                wordIndex = wordIndex+1
                word[wordIndex] = label

                if (self.dawg.lookup(word)):
                    self.anagramHandler(word)

                # parent, current_edge, child = self.dawg.minimizedNodes.values().index(child)
                self.traverseDAWG(child)

                self.dawg.rack[label] = self.dawg.rack[label]+1
                wordIndex = wordIndex-1
                print("hit 4")

            if self.isLast(child):
                return

    
    

    