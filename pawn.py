class Pawn:

    def __init__(self, side):
        self.side = side

        if self.side == 1:
            self.text = '\u265F'
        else:
            self.text = '\u2659'

        self.firstMove = True


    def possibleMoves(self, pos, board):

        row = pos[0]
        col = pos[1]

        result = []

        if self.side == 0:
            front = -1
        else:
            front = 1

        #check for vertical movement
        if row+1*front >=0 and row+1*front <=7:    
            if board[row+1*front][col] == 0:
                result.append([row+1*front,col])

                if row+2*front >=0 and row+2*front <=7:
                    if board[row+2*front][col] == 0 and self.firstMove == True:
                        result.append([row+2*front,col])
            

            #check for diagonal movement to take
            if col-1 >= 0:
                if board[row+1*front][col-1] != 0:
                    if board[row+1*front][col-1].side != self.side:
                        result.append([row+1*front,col-1])

            if col+1 <= 7:
                if board[row+1*front][col+1] != 0:
                    if board[row+1*front][col+1].side != self.side:
                        result.append([row+1*front,col+1])

        return result