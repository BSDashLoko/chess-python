class Bishop:

    def __init__(self, side):
        self.side = side

        if self.side == 1:
            self.text = '\u265D'
        else:
            self.text = '\u2657'

        self.firstMove = True


    def possibleMoves(self, pos, board):

        row = pos[0]
        col = pos[1]

        result = []

        #up left movement
        pRow = row-1
        pCol = col-1
        while pRow >=0 and pCol >=0:
            if board[pRow][pCol] == 0:
                result.append([pRow,pCol])
            else:
                if board[pRow][pCol].side == self.side:
                    break
                else:
                    result.append([pRow,pCol])
                    break
            pRow -= 1
            pCol -= 1


        #up right movement
        pRow = row-1
        pCol = col+1
        while pRow >=0 and pCol <=7:
            if board[pRow][pCol] == 0:
                result.append([pRow,pCol])
            else:
                if board[pRow][pCol].side == self.side:
                    break
                else:
                    result.append([pRow,pCol])
                    break
            pRow -= 1
            pCol += 1



        
        #down left movement
        pRow = row+1
        pCol = col-1
        while pRow <=7 and pCol >=0:
            if board[pRow][pCol] == 0:
                result.append([pRow,pCol])
            else:
                if board[pRow][pCol].side == self.side:
                    break
                else:
                    result.append([pRow,pCol])
                    break
            pRow += 1
            pCol -= 1


        #down right movement
        pRow = row+1
        pCol = col+1
        while pRow <=7 and pCol <=7:
            if board[pRow][pCol] == 0:
                result.append([pRow,pCol])
            else:
                if board[pRow][pCol].side == self.side:
                    break
                else:
                    result.append([pRow,pCol])
                    break
            pRow += 1
            pCol += 1

        return result