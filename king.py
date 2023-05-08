from rook import Rook

class King:

    def __init__(self, side):
        self.side = side

        if self.side == 1:
            self.text = '\u265A'
        else:
            self.text = '\u2654'

        self.firstMove = True


    def possibleMoves(self, pos, board):

        row = pos[0]
        col = pos[1]

        result = []

        #8 possible positions
        posResult = [
                    [row-1,col-1],[row-1,col],[row-1,col+1],
                    [row,col-1],                [row,col+1],
                    [row+1,col-1],[row+1,col],[row+1,col+1]
                    ]

        #check validity for each of them
        for x in posResult:
            if x[0] >= 0 and x[0] <= 7 and x[1] >= 0 and x[1] <= 7:
                if board[x[0]][x[1]] == 0:
                    result.append([x[0],x[1]])
                elif board[x[0]][x[1]].side != self.side:
                    result.append([x[0],x[1]])


        #check for castle
        if self.firstMove:

            if board[row][col-1] == 0 and board[row][col-2] == 0 and board[row][col-3] == 0 and type(board[row][col-4]) == Rook:
                if board[row][col-4].side == self.side and board[row][col-4].firstMove == True:
                    result.append([row,col-2])

            if board[row][col+1] == 0 and board[row][col+2] == 0 and type(board[row][col+3]) == Rook:
                if board[row][col+3].side == self.side and board[row][col+3].firstMove == True:
                    result.append([row,col+2])



        return result