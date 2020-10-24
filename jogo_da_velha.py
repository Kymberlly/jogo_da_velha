class JogoDaVelha():
    def __init__(self):
        import uuid
        self.id = str(uuid.uuid4())
        self.firstPlayer = self.sorteia_jogador()
        self.partida = 0
        self.tabuleiro = [[None, None, None], [None, None, None], [None, None, None]]

    def iniciar_partida(self):
        return {"id": self.id, "firstPlayer": self.firstPlayer}


    def dadosPartida(self):
        print(self.id)
        print(self.firstPlayer)
        print(self.partida)
        print(self.tabuleiro)

    def sorteia_jogador(self):
        import random
        if random.randrange(0, 10) % 2 == 0:
            return "X"
        return "O"

    def autentica_partida_atual(self, id_partida):
        return self.id == id_partida

    def autentica_turno_jogador(self, jogador):
        jogador_atual = self.firstPlayer
        if self.partida % 2 != 0:
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'

        return jogador_atual == jogador

    def realiza_jogada(self, id_partida, jogador, position):
        print(id_partida, jogador, position)
        if not self.autentica_partida_atual(id_partida):
            return {'msg': 'Partida não encontrada'}

        print('DEPOIS DE AUTENTICAR JOGADA')
        if not self.autentica_turno_jogador(jogador):
            return {'msg': 'Não é turno do jogador'}
        print('DEPOIS DE AUTENTICAR JOGADOR')


        print('NO REALIZA JOGADA')

        self.partida += 1
        posX = int(position.get('x', None))
        posY = int(position.get('y', None))
        return self.marca_posicao(posX, posY, jogador)

    def marca_posicao(self, x, y, jogador):
        if not self.tabuleiro[x][y]:
            num_jogador = 1 if jogador == 'X' else -1
            self.tabuleiro[x][y] = num_jogador

        status_jogo = self.status_jogo(x, y)
        if not status_jogo:
            return False
        # MELHORAR
        return {'winner': status_jogo}

    def status_jogo(self, x, y):
        tam_tabuleiro = len(self.tabuleiro)
        horiz = self.verifica_horizontal(x, tam_tabuleiro)
        vert = self.verifica_vertical(y, tam_tabuleiro)
        diagonal_principal, diagonal_secundaria = self.verifica_diagonal(tam_tabuleiro)

        print(horiz, vert, diagonal_principal, diagonal_secundaria)

        if horiz in [3, -3]:
            return 'X' if horiz == 3 else 'O'
        if vert in [3, -3]:
            return 'X' if vert == 3 else 'O'
        if diagonal_principal in [3, -3]:
            return 'X' if diagonal_principal == 3 else 'O'
        if diagonal_secundaria in [3, -3]:
            return 'X' if diagonal_secundaria == 3 else 'O'

        if self.verifica_draw():
            return 'Draw'

        return False

    def verifica_draw(self):
        if self.partida == 9:
            return True
        return False

    def verifica_horizontal(self, x, tam_tabuleiro):
        cont = 0
        for indice in range(tam_tabuleiro):
            if self.tabuleiro[x][indice]:
                cont += self.tabuleiro[x][indice]
        return cont

    def verifica_vertical(self, y, tam_tabuleiro):
        cont = 0
        for indice in range(tam_tabuleiro):
            if self.tabuleiro[indice][y]:
                cont += self.tabuleiro[indice][y]
        return cont

    def verifica_diagonal(self, tam_tabuleiro):
        cont_diagonal_p = 0
        max_posicoes = 2
        for indice in range(tam_tabuleiro):
            if self.tabuleiro[max_posicoes][indice]:
                cont_diagonal_p += self.tabuleiro[max_posicoes][indice]
            max_posicoes -= 1

        cont_diagonal_s = 0
        for indice in range(tam_tabuleiro):
            if self.tabuleiro[indice][indice]:
                cont_diagonal_s += self.tabuleiro[indice][indice]

        return cont_diagonal_s, cont_diagonal_p

