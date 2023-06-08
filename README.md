# chess python

 - chess minigame in python console

# Explicação inicial
O código tem a função de criar um jogo de xadrez, em um tabuleiro 8x8, seguindo as regras de movimento de cada peça, com cada jogador tendo sua vez de realizar seu movimento, com a adição de movimentos específicos como o roque, e o jogo acaba quando algum dos reis é eliminado.

# Game Loop
O main.py importa as classes das outras peças, inicializa o tabuleiro com 0 nas posições vazias e uma instância da peça no lugar do tabuleiro que ela fica, definindo seu lado no construtor (0 são peças brancas e 1 são peças pretas).

Quando é iniciado o loop de jogo, ele define o primeiro lado a jogar como as brancas, reseta o tabuleiro com base no backup e inicia o loop de jogada chamado repeat, nele o tabuleiro é mostrado com base no lado que está jogando (função showBoard() que itera sobre o tabuleiro substituindo 0 por ▯ e as peças pelo unicode da peça com o atributo [nome da peça].text) e ele pega do usuário a posição da peça a ser movida (row,col) a partir da função strToCoord() que checa se a string digitada é uma posição válida e transforma, por exemplo, e3 em (5,4), com isso, o programa checa se a posição é válida (está no tabuleiro, e é a posição de uma peça do lado que está jogando e que pode se mover) e quando o usuário digita uma posição válida ela é salva em piecePos. Agora o outro loop printa as possiveis posições que a peça pode se mover, pelo método possibleMoves() presente em todas as classes, que dita as regras do xadrez, e pelo método coordToStr(), que faz o inverso da strToCoord(), retornando, por exemplo, e3 com as coordenadas (5,4). Com a lista de possíveis movimentos, o programa pede a posição para se mover com strToCoord(), se a coordenada está contida em possibleMoves, ele atribui a essa coordenada o valor da peça, e deixa o local antigo dela vazio. Além disso, nessa parte do código é checado se houve o roque (não se o roque é possível), se a peça movida foi um Rei e se ela se movimentou 2 casas, e, se sim, ele move também a torre para o lado oposto do movimento do Rei.

![tabuleiro](https://github.com/BSDashLoko/chess-python/blob/main/board.png)

Com isso, a jogada é terminada e se troca-se as variáveis side e sideStr para a outra cor, se era a vez das peças brancas, agora é das pretas e vice-versa. Depois se checa se algum Rei foi derrotado, para dar a vitória ao outro lado, é checado a existência de um Rei de cada cor, para continuar o jogo, senão, acabá-lo e adicionar uma vitória para o vencedor em uma das variáveis (wWin e bWin). E, se a partida acabar, é perguntado se o loop newGame será reiniciado ou não.

![vitoria](https://github.com/BSDashLoko/chess-python/blob/main/win.png)

### showBoard()
Essa função leva como argumentos o tabuleiro e o lado para qual o tabuleiro será apresentado. Então se itera sobre cada elemento da matriz (começando pela última linha no caso das peças pretas, para inverter a visão do tabuleiro), trocando o 0 por ▯ e as peças pelo unicode da peça com o atributo [nome da peça].text. No começo de cada linha é printado o número dessa linha, e no final é adicionado a letra correspondente de cada coluna.

### strToCoord()
A função leva como argumento uma mensagem que será mostrada ao usuário para pedir uma posição de xadrez, se checa se a string digitada possui uma letra na primeira posição e um número na segunda, sem mais caracteres. Então a letra se transforma no número da coluna com ord, e diminuindo 97 do valor, para que a=0; b=1; c=2 e assim por diante, já o número, subtrái-se ele de 8 para resultar no número da linha, para que 1 = 7; 2 = 6; de acordo com a nomenclatura de posição de xadrez.


### coordToStr()
Essa função faz o processo inverso da strToCoord, transformando a coluna na letra correspondente com chr e o número da linha em nomenclatura de xadrez.

# Classes de peça
Todas as peçar possuem uma classe atribuída a ela, todas com um construtor com o atributo side, que define self.side da peça, o lado, em que 0 são as peças brancas e 1 são as peças pretas, e com base nisso, o side.text é definido como um unicode do time correspondente. Além disso, é definido self.firstMove = True para a lógica de certas peças. E principalmente, há a função possibleMoves(), que toma o tabuleiro e a posição da peça para definir para quais casas certa peça pode ir segundo a lógica específica de cada peça.

# Explicação do possibleMoves() de cada peça

### Bispo (Bishop)
Para a lógica do Bispo há 4 loops "while". Cada loop corresponde a um movimento do bispo. Ele se movimenta nas 4 diagonais (up left, up right, down left, down right). O primeiro loop é o up left (esquerda cima). Ele começa indicando que a posição iterável da linha será pRow é row-1, assim como a coluna iterável pCol será col-1. Isso quer dizer que a cada movimento do bispo na upleft vai diminuir uma casa da linha e uma da coluna. Para explicar isso é necessário pensar na seguinte forma: O tabuleiro tem 8 colunas (de 0 a 7) e 8 linhas da mesma forma. A primeira linha do tabuleiro é a linha 0, assim como a primeira coluna da esquerda é a coluna 0, logo, a primeira linha das peças brancas é a linha 7 e a última coluna da direita é a coluna 7. Tendo isso em vista, a cada movimento do bispo ele vai diminuir uma linha e uma coluna se ele andar na posição up left.

Explicado isso vamos entrar no loop do while, ele delimita o tamanho do tabuleiro para continuar. Dada essa condição, entra um if board[pRow][pCol] == 0, isso significa que a condição so vai avançar se essa posição estiver vazia, pois o 0 na matriz indica que esta vazio. Se estiver vazio será utilizado um comando de append nessa posição, ou seja, essa posição será adicionada a lista result, que estava vazia. Caso a casa nao esteja vazia, ele ira checar se a peça é inimiga ou do mesmo time. Se o valor side da peça for igual a self.side significa que é uma peça do mesmo time, logo, ele aplica a função break que faz o loop parar, pois vc nao pode comer uma peça do mesmo time e nem passar por cima. Caso não seja do mesmo time, ele adiciona essa posição ao result, pois voce pode comer essa peça, mas logo apos ele da o break, pois voce nao pode atravessar a peça inimiga.

Isso se repetirá com os outros 3 loops do while, a unica diferença sera na subtração ou adiçao de colunas e linhas, por exemplo no up right, é necessário somar a coluna pois a coluna vai para a direita, mas ainda assim diminui a linha. Outra diferença também está no while, pois agora a coluna esta : pCol <= 7, pois a peça so pode ir ate no maximo a coluna 7. O mesmo conceito se aplica para os outros whiles.
Ao fim dos 4 loops temos a função return result, assim todas as opções possiveis observadas pelo while irão compor a lista result que antes estava vazia.

![bishop](https://github.com/BSDashLoko/chess-python/blob/main/bishop.png)


### Torre (Rook)
Assim como o bispo, a torre também possuirá 4 whiles porém ela se movimentará para up, down, left, right. Ela possui a mesma estrutura do bispo, no while da esquerda ira diminuir uma coluna. O while da direita vai aumentar uma coluna, o up ira diminuir uma linha e o down aumentar uma linha. Assim como terá a mesma estrutura para ver se tem peças inimigas ou do mesmo time no tabuleiro e usando o comando append para adicionar na lista. E ao final dos whiles irá dar o return result para retornar os possiveis movimentos na lista result quando a função for chamada.


### Rainha (Queen)
A rainha é uma junção da Torre (Rook) e do Bispo (Bishop) pois ela faz o movimento dos dois: left, right, up, down, up left, up right, down left, down right. Então há 8 loops para compor o retorno do seu possibleMoves().


### Cavalo (Knight)
Para o cavalo será checado a situação das 8 casas que ele pode se movimentar baseado na sua posição:
- 2 linhas pra cima e 1 coluna pra direita
- 2 linhas pra cima e 1 coluna pra esquerda
- 2 linhas pra baixo e 1 coluna pra esquerda
- 2 linhas pra baixo e 1 coluna pra direita
- 1 linha pra cima e 2 colunas pra esquerda
- 1 linha pra cima e 2 colunas pra direita
- 1 linha pra baixo e 2 colunas pra esquerda
- 1 linha pra baixo e 2 colunas pra direita

Após isso é analisado se cada posição está dentro das 8 colunas e das 8 linhas (de 0 a 7). Então é analisado se a casa está vazia ou se tem uma peça inimiga, adicionando essa posição ao result caso positivo.


### Rei (King)
Semelhante ao cavalo, será checado a situação das 8 casas que ele pode ir:
- 1 linha pra cima e 1 coluna pra esquerda
- 1 linha pra cima
- 1 linha pra cima e 1 coluna pra direita
- 1 coluna pra esquerda
- 1 coluna pra direita
- 1 linha pra baixo e 1 coluna pra esquerda
- 1 linha pra baixo
- 1 linha pra baixo e 1 coluna pra direita

Então será analisado se essa posição é válida ou não, paralelo ao processo do cavalo.

Agora ter-se-á a checagem de roque. Primeiramente se checa se é o primeiro movimento do rei (firstMove = True), então se checa a possibilidade de roque grande, verificando se as 3 casas à esquerda do Rei estão vazias e a quarta contém uma Torre, então, se a Torre for do mesmo time e tiver firstMove = True, a jogada é adicionada à result, que será retornada. Já para o roque pequeno, é checado se as 2 casas à direita do Rei estão vazias e a terceira contém uma Torre, depois faz as mesmas verificações do roque grande.


### Peão (Pawn)
Primeiramente será checado o time do peão, para definir a variável front, que determinará para qual lado o peão poderá andar, já que depende da cor do peão, o front irá multiplicar o valor adicionado a row, pois as peças brancas diminuem uma linha para avançar (front = -1) e as pretas aumentam de linha para avançar (front = 1).

Então o programa vai checar se o peão pode andar para frente dentro dos parametros do tabuleiro (linhas de 0 a 7). Se for possível e nao tiver peças no local ele ira adicionar a posição ao result, se essa condição for completada, depois, ele irá checar se é o primeiro movimento daquele peão, para também adicionar a casa 2 casas a frente do peão, caso essa casa estiver vazia.

Então, é checado a possibilidade de comer peças na diagonal, vendo a situação da casa a frente na esquerda e direita, se a casa possuir uma peça inimiga, a possição é adicionada ao result que será retornado.



# Considerações Finais
Esse repositório foi feito como uma atividade de Universidade, pelos seguintes alunos:
- Nicholas Cartaxo RGM: 32953381
- William Henrique RGM: 34311874
