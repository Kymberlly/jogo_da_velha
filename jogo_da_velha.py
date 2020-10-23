class JogoDaVelha():
    def __init__(self):
        self.id = None
        self.firstPlayer = None
        self.partida = 0

        self.tabuleiro = [[None, None, None], [None, None, None], [None, None, None]]

    def iniciar_partida(self):
        import uuid
        self.id = str(uuid.uuid4())
        self.firstPlayer = self.sorteia_jogador()

        return {"id": self.id, "firstPlayer": self.firstPlayer}

    def sorteia_jogador(self):
        import random
        if random.randrange(0, 10) % 2 == 0:
            return "X"
        return "O"

    def carrega_dados_jogo(self):
        import json
        try:
            with open('log_jogo_velha.json', 'r') as arquivo:
                return json.load(arquivo)
        except:
            with open('log_jogo_velha.json', 'w') as arquivo:
                return json.dump({}, arquivo)

    def armazena_dados_jogo(self, dados_jogo):
        import json
        with open('log_jogo_velha.json', 'w') as arquivo:
            return json.dump(dados_jogo, arquivo)

    def autentica_partida_atual(self, id_partida):
        return self.id == id_partida

    def autentica_turno_jogador(self, jogador):
        print(jogador, self.firstPlayer)
        jogador_atual = self.firstPlayer
        if self.partida % 2 != 0:
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'

        print(jogador_atual)
        return jogador_atual == jogador

    def realiza_jogada(self, id_partida, jogador, posX, posY):
        if not self.autentica_partida_atual(id_partida):
            return {'msg': 'Partida não encontrada'}

        if not self.autentica_turno_jogador(jogador):
            return {'msg': 'Não é turno do jogador'}

        self.partida += 1
        return self.marca_posicao(posX, posY, jogador)


    def marca_posicao(self, x, y, jogador):
        if not self.tabuleiro[x][y]:
            num_jogador = 1 if jogador == 'X' else -1
            self.tabuleiro[x][y] = num_jogador

        status_jogo = self.status_jogo(x, y)
        if not status_jogo:
            return False

        return {'winner': status_jogo}


    def status_jogo(self, x, y):
        tam_tabuleiro = len(self.tabuleiro)
        horiz = self.verifica_horizontal(x, tam_tabuleiro)
        vert = self.verifica_vertical(y, tam_tabuleiro)
        self.verifica_diagonal(tam_tabuleiro)

        if horiz in [3, -3]:
            return 'X' if horiz == 3 else 'O'
        if vert in [3, -3]:
            return 'X' if vert == 3 else 'O'

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
            if self.tabuleiro[indice][max_posicoes]:
                cont_diagonal_p += self.tabuleiro[indice][max_posicoes]

        cont_diagonal_s = 0
        for indice in range(tam_tabuleiro):
            if self.tabuleiro[indice][indice]:
                cont_diagonal_s += self.tabuleiro[indice][indice]

