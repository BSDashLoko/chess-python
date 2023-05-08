class Knight:

    def __init__(self, side):
        self.side = side

        if self.side == 1:
            self.text = '\u265E'
        else:
            self.text = '\u2658'

        self.firstMove = True


    def possibleMoves(self, pos, board):

        row = pos[0]
        col = pos[1]

        result = []

        #8 possible positions
        posResult = [
                    [row-2,col-1],[row-2,col+1],
                    [row+2,col-1],[row+2,col+1],
                    [row-1,col-2],[row+1,col-2],
                    [row-1,col+2],[row+1,col+2],
                    ]

        #check validity for each of them
        for x in posResult:
            if x[0] >= 0 and x[0] <= 7 and x[1] >= 0 and x[1] <= 7:
                if board[x[0]][x[1]] == 0:
                    result.append([x[0],x[1]])
                elif board[x[0]][x[1]].side != self.side:
                    result.append([x[0],x[1]])


        return result