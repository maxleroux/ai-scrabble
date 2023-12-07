# base setup and accessing of the board's rows/cols and tiles
class board:
    def __init__(self):
        row0  = "---------------"
        row1 = "---------------"
        row2  = "---------------"
        row3  = "---------------"
        row4  = "---------------"
        row5  = "---------------"
        row6  = "---------------"
        row7  = "---------------"
        row8  = "---------------"
        row9  = "---------------"
        row10 = "---------------"
        row11 = "---------------"
        row12 = "---------------"
        row13 = "---------------"
        row14 = "---------------"
        self.board = row0 + row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8 + row9 + row10 + row11 + row12 + row13 + row14

    # add the given letters to the given spaces on the board
    def updateBoard(self, letters, spaces):
        for (letter, space) in zip(letters, spaces):
            self.board = self.board[:space] + letter + self.board[space+1:]

    # print out the current state of the game board
    def printBoard(self):
        board = self.board
        print('Here is the current board:')
        for row in range( int(len(board)//15) ):
            for column in range(15):
                print(board[15*row + column], end = ' ')
            print('')

    # get a list of spots on the board that do not currently have letters
    def getOpenSpot(self):
        board = self.board
        open = []
        for spot in range(len(board)):
            if board[spot] in '-23@#':
                open.append(spot)
        return open

    def getValidStartingSpots(self):
        ''' Finds every place where a word could start (called attachments) given a board '''
        # i dont really understand this rn but it definitely seems useful TODO
        board = self.board
        attachments = set([])

        for i in range(len(board)):
            if board[i] not in '-23@#':
                row = i//15
                column = i%15
                # space directions
                down = (row-1)*15 + column
                up = (row+1)*15 + column
                left = row*15 + column-1
                right = row*15 + column+1
                
                # attachments are added
                if (row != 0) and (board[down] in '-23@#') and (down not in attachments):
                    attachments.add(down)
                if (row != 14) and (board[up] in '-23@#') and (up not in attachments):
                    attachments.add(up)
                if (column != 0) and (board[left] in '-23@#') and (left not in attachments):
                    attachments.add(left)
                if (column != 14) and (board[right] in '-23@#') and (right not in attachments):
                    attachments.add(right)

        if len(attachments) == 0:
            attachments.add(112)
        
        return attachments