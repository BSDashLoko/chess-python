class Queen:

    def __init__(self, side):
        self.side = side

        if self.side == 1:
            self.text = '\u265B'
        else:
            self.text = '\u2655'

        self.firstMove = True


    def possibleMoves(self, pos, board):

        row = pos[0]
        col = pos[1]

        result = []

        #left movement
        pCol = col-1
        while pCol >=0:
            if board[row][pCol] == 0:
                result.append([row,pCol])
            else:
                if board[row][pCol].side == self.side:
                    break
                else:
                    result.append([row,pCol])
                    break
            pCol -= 1


        #right movement
        pCol = col+1
        while pCol <=7:
            if board[row][pCol] == 0:
                result.append([row,pCol])
            else:
                if board[row][pCol].side == self.side:
                    break
                else:
                    result.append([row,pCol])
                    break
            pCol += 1



        
        #up movement
        pRow = row-1
        while pRow >=0:
            if board[pRow][col] == 0:
                result.append([pRow,col])
            else:
                if board[pRow][col].side == self.side:
                    break
                else:
                    result.append([pRow,col])
                    break
            pRow -= 1


        #down movement
        pRow = row+1
        while pRow <=7:
            if board[pRow][col] == 0:
                result.append([pRow,col])
            else:
                if board[pRow][col].side == self.side:
                    break
                else:
                    result.append([pRow,col])
                    break
            pRow += 1


        

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