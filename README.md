# chess python

 chess minigame in python console
 

O main.py importa as classes das outras peças, inicializa o tabuleiro com 0 nas posições vazias e uma instância da peça no lugar do tabuleiro que ela fica, definindo seu lado no construtor (0 são peças brancas e 1 são peças pretas).

Quando é iniciado o loop de jogo, ele define o primeiro lado a jogar como as brancas, reseta o tabuleiro com base no backup e inicia o loop de jogada chamado repeat, nele o tabuleiro é mostrado com base no lado que está jogando (função showBoard() que itera sobre o tabuleiro substituindo 0 por ▯ e as peças pelo unicode da peça com o atributo [nome da peça].text) e ele pega do usuário a posição da peça a ser movida (row,col) a partir da função strToCoord() que checa se a string digitada é uma posição válida e transforma, por exemplo, e3 em (5,4), com isso, o programa checa se a posição é válida (está no tabuleiro, e é a posição de uma peça do lado que está jogando e que pode se mover) e quando o usuário digita uma posição válida ela é salva em piecePos. Agora o outro loop printa as possiveis posições que a peça pode se mover, pelo método possibleMoves() presente em todas as classes, que dita as regras do xadrez, e pelo método coordToStr(), que faz o inverso da strToCoord(), retornando, por exemplo, e3 com as coordenadas (5,4). Com a lista de possíveis movimentos, o programa pede a posição para se mover com strToCoord(), se a coordenada está contida em possibleMoves, ele atribui  
