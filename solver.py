import dawg
import referee

DICTIONARY = "./official_scrabble_dict.txt"

rackValueDict = {'A': 0.5, 'B': -3.5, 'C': -0.5, 'D': -1, 'E': 4, 'F': -3, 'G': -3.5,
                 'H': 0.5, 'I': -1.5, 'J': -2.5, 'K': -1.5, 'L': -1.5, 'M': -0.5, 'N': 0,
                 'O': -2.5, 'P': -1.5, 'Q': -11.5, 'R': 1, 'S': 7.5, 'T': -1, 'U': -4.5,
                 'V': -6.5, 'W': -4, 'X': 3.5, 'Y': -2.5, 'Z': 3, ' ': 24.5}

class solver:
    def __init__(self, game):
        self.game = game
        self.dawg = game.dawg
        self.anagrams = []

    def rack_evaluation(self, rack):
        rackScore = 0
        for letter, count in rack():
            rackScore += rackValueDict[letter] * count
        return rackScore

    def getValidPlacement(self, anagram):
        letterCombos = []
        spotCombos = []

        for letter in anagram:
            if (letter not in self.game.board.board):
                return False, letterCombos, spotCombos

        validConnections = self.game.board.getValidConnections()
        for a in anagram:
            validityByConnection = []
            for connection in validConnections:
                row = connection//15
                column = connection % 15
                # space directions
                down = (row-1)*15 + column
                up = (row+1)*15 + column
                left = row*15 + column-1
                right = row*15 + column+1

                letterConnectionExists = True
                if (row != 0) and (self.game.board[down] not in a):
                    if (row != 14) and (self.game.board[up] not in a):
                        if (column != 0) and (self.game.board[left] not in a):
                            if (column != 14) and (self.game.board[right] not in a):
                                letterConnectionExists = False
                validityByConnection.append[letterConnectionExists]

            if False in validityByConnection:
                return False, letterCombos, spotCombos

        if (letterCombos.len() != 0):
            return True, letterCombos, spotCombos
        else:
            return False, letterCombos, spotCombos

    def moveGenerator(self):
        validAnagrams = {}
        for anagram in self.anagrams:
            canAnagramBePlaced, letterCombos, spotCombos = self.getValidPlacement(
                anagram)
            if canAnagramBePlaced:
                for i in range(letterCombos.len()):
                    validAnagrams[anagram] = [letterCombos[i], spotCombos[i]]

        maxScore = 0
        maxLetterCombo = []
        maxSpotCombo = []
        rackCopy = self.game.rack.copy()
        for anagram, letterCombo, spotCombo in validAnagrams:
            for letter in anagram:
                if letter in rackCopy:
                    rackCopy.remove(letter)
            rackValue = self.rack_evaluation(rackCopy)
            wordScore = referee.calcWordScore(
                letterCombo, spotCombo, self.game.board)
            if wordScore + rackValue > maxScore:
                maxScore = wordScore + rackValue
                maxLetterCombo.clear()
                maxLetterCombo.append[letterCombo]
                maxSpotCombo.clear()
                maxSpotCombo.append[spotCombo]

        return maxLetterCombo, maxSpotCombo

    # SIMPLE MOVE GENERATOR: loop first over all squares & try to find all moves
    # that start on that square —> traverseDawg after it has been improved for handling
    # of blanks, letters on board, edge limitations, and crosswords

    def isLast(self, child):
        return child.__str__()[0] == '1'

    def getChar(self, edge):
        return list(self.dawg.minimizedNodes.keys())[list(self.dawg.minimizedNodes.values()).index(edge)]

    def anagramHandler(self, word):
        self.anagrams.append(word)
        # print(self.anagrams)

    # this needs to also account for :
    # 1) using blanks
    # 2) handling of tiles on board
    # 3) checking for edge of board --> attachments method from scrabble-ai?
    # 4) handling of crossword constraints
    def traverseDAWG(self, node):
        if node.final == True:
            return

        word = ""
        wordIndex = 0

        loopBreaker = True
        while loopBreaker:

            label = list(node.edges.keys())[0]
            child = node.edges[label]

            if (self.game.rack[label] != 0):
                self.game.rack[label] = self.game.rack[label]-1

                wordIndex = wordIndex+1
                word = word[:wordIndex] + label + word[wordIndex+1:]

                if (self.dawg.lookup(word)):
                    self.anagramHandler(word)

                self.traverseDAWG(child)

                self.game.rack[label] = self.game.rack[label]+1
                wordIndex = wordIndex-1

            if node.final:
                break

class polynomialRegressionModel():
    def __init__(self, degree=1, learning_rate=1e-3):
        self.degree = degree
        self.learning_rate = learning_rate
        self.weights = []
        for i in range(self.degree + 1):
            self.weights.append(0)
        self.losses = []

    def get_features(self, x):
        features = [1]
        for i in range(1, self.degree+1):
            features.append(x**i)
        return features

    def get_weights(self):
        return self.weights

    def hypothesis(self, x):
        current_weights = self.get_weights()
        bias_term = current_weights[0]
        hypothesis = bias_term
        for i in range(len(self.get_features(x))):
            hypothesis += current_weights[i]*self.get_features(x)[i]
        return hypothesis

    def predict(self, x):
        return self.hypothesis(x)

    def loss(self, x, y):
        return (self.hypothesis(x)-y)**2

    def gradient(self, x, y):
        gradient = []
        for feature in self.get_features(x):
            gradient.append(2*(self.hypothesis(x)-y)*feature)
        return gradient

    def train(self, dataset, evalset=None):
        iterations = 10000
        iterations_interval = 50
        i = 0
        while i <= iterations:
            x, y = dataset.get_sample()
            grad = self.gradient(x, y)
            for j in range(len(self.get_weights())):
                self.weights[j] = self.weights[j] - self.learning_rate*grad[j]
            i = i + 1

            if i % iterations_interval == 0:
                current_average_loss = dataset.compute_average_loss(self)
                self.losses.append(current_average_loss)

def linear_regression():
    #not implemented
    #train = util.get_dataset(...)
    #val = util.get_dataset(...)
    sine_model = polynomialRegressionModel(degree=1, learning_rate=1e-4)
    sine_model.train(train)
    train.plot_data(sine_model)
    iterations = range(0, 10000, 50)
    train.plot_loss_curve(iterations, sine_model.losses)
    print(train.compute_average_loss(sine_model))

    # hyperparameter search
    degrees = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
    learning_rates = [1e-4, 1e-5, 1e-6, 1e-5,
                      1e-6, 1e-4, 1e-6, 1e-4, 1e-5, 1e-3]

    best_degree = 0
    best_learning_rate = 0

    best_validation_loss = 9999

    for i in range(10):
        current_degree = degrees[i]
        current_learning_rate = learning_rates[i]
        current_sine_model = polynomialRegressionModel(
            degree=current_degree, learning_rate=current_learning_rate)
        current_sine_model.train(train)

        average_training_loss = train.compute_average_loss(
            current_sine_model)
        average_validation_loss = val.compute_average_loss(
            current_sine_model)

        if average_validation_loss < best_validation_loss:
            best_validation_loss = average_validation_loss
            best_degree = current_degree
            best_learning_rate = current_learning_rate

    best_sine_model = polynomialRegressionModel(
        degree=best_degree, learning_rate=best_learning_rate)
    print("The best combination was degree " + str(best_degree) +
          " and learning rate " + str(best_learning_rate))
    best_sine_model.train(val)
    val.plot_data(best_sine_model)
