from pawn import Pawn
from rook import Rook
from bishop import Bishop
from knight import Knight
from queen import Queen
from king import King


#prints board with proper characters
def showBoard(board):
        for row in range(8):
                for col in range(8):
                        if type(board[row][col]) != int:
                                x = board[row][col].text
                        else: x = "▯"
                        if col != 7:
                                print(x, end=" ")
                        else: print(x)


#board with all the pieces
board = [
        [Rook(1),Knight(1),Bishop(1),Queen(1),King(1),Bishop(1),Knight(1),Rook(1)],
        [Pawn(1),Pawn(1),Pawn(1),Pawn(1),Pawn(1),Pawn(1),Pawn(1),Pawn(1),],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [Pawn(0),Pawn(0),Pawn(0),Pawn(0),Pawn(0),Pawn(0),Pawn(0),Pawn(0),],
        [Rook(0),Knight(0),Bishop(0),Queen(0),King(0),Bishop(0),Knight(0),Rook(0)]
        ]

#asks user to input a position ex:d4 and return its coordinate on the board
def strToCoord(message):
        while True:
                tileStr = input(message)
                if len(tileStr) != 2:
                        print("Use a nomenclatura corretamente ex:d4")
                elif type(tileStr[0]) != str or  tileStr[1].isnumeric() == False:
                        print("Use a nomenclatura corretamente ex:d4")
                else:
                        char = tileStr[0].lower()
                        number = int(tileStr[1])

                        row = 8-number
                        col = ord(char)-97
                        return (row, col)




def coordToStr(coords):
        number = 8-coords[0]
        char = chr(coords[1]+97)
        return char+str(number)



#start of game loop

newGame = True
while newGame:

        side = 0
        sideStr = "Brancas"
        repeat = True

        while repeat:

                showBoard(board)

                #gets piece to be moved
                while True:

                        row, col = strToCoord("("+sideStr+" jogam) Digite a posiçao da peça que você quer mover: ")

                        #check coord validity
                        if row >= 0 and row <= 7 and col >= 0 and col <= 7:
                                if board[row][col] != 0:
                                        if board[row][col].side == side:
                                                piecePos = [row,col]
                                                break

                                        else: print("Escolha uma das peças",sideStr)

                                else: print("Escolha uma das peças",sideStr)

                        else: print("Posição inválida!")



                #gets tile where piece will be moved and moves it
                while True:

                        #display possible moves
                        for x in board[piecePos[0]][piecePos[1]].possibleMoves(piecePos, board):
                                print(coordToStr(x), end=" ")
                        print()

                        row,col = strToCoord("Escolha um dos possíveis movimentos: ")
                        if [row,col] in board[piecePos[0]][piecePos[1]].possibleMoves(piecePos, board):
                                board[row][col] = board[piecePos[0]][piecePos[1]]
                                board[piecePos[0]][piecePos[1]] = 0

                                board[row][col].firstMove = False

                                break

                        else: print("Escolha uma posição válida")


                #changes side to play
                if side == 0:
                        side = 1
                        sideStr = "Pretas"
                else:
                        side = 0
                        sideStr = "Brancas"




                #checks to see if one of the kings is dead
                whiteKing = 0
                blackKing = 0
                for row in board:
                        for tile in row:
                                if type(tile) == King:
                                        if tile.side == 0:
                                                whiteKing += 1
                                        else:
                                                blackKing += 1

                if whiteKing == 0:
                        print("Vitória das peças pretas, parabéns!")
                        repeat = 0
                elif blackKing == 0:
                        print("Vitória das peças brancas, parabéns!")
                        repeat = 0

        newGameStr = input("Deseja jogar novamente (s/n)? ")
        if newGameStr == 's':
                newGame = True
        else:
                newGame = False


#print(board[7][4].possibleMoves([7,4],board))



#TODO CHECK FOR CASTLE AND MOVE ROOK TOO WHEN IT HAPPENS
#TODO add repeat function
input("enter to quit")
