from .regras_abstratas import AbstractRegrasJogo
from .personagens import Personagens
from percepcoes import PercepcoesJogador
from acoes import AcoesJogador, DirecaoMover

class EightPuzzle(AbstractRegrasJogo):

    def __init__(self):
        super().__init__()
        tabuleiro_completo = [[1,2,3],[6,7,0],[5,8,4]]

        self.tabuleiro = tabuleiro_completo
        self.id_agente = {Personagens.O_JOGADOR: 0}
        self.acoes_jogador = {0: None}
        self.posicao_vazia = self.descobrir_posicao_vazia()

    def registrarAgentePersonagem(self, personagem):
            return self.id_agente[personagem]

    def isFim(self):
            tabuleiro = list()
            for lin in self.tabuleiro:
                for col in lin: 
                    tabuleiro.append(col)
            sol = [1,2,3,4,5,6,7,8,0]
            return tabuleiro == sol

    def gerarCampoVisao(self, id_agente):
            percepcoes_jogador = PercepcoesJogador(tabuleiro = self.tabuleiro, dimensoes = (3,3), posicao_vazia = self.posicao_vazia)
            return percepcoes_jogador

    def registrarProximaAcao(self, id_agente, acao):
            self.acoes_jogador[id_agente] = acao

    def atualizarEstado(self, diferencial_tempo):
        acao_jogador = self.acoes_jogador[self.id_agente[Personagens.O_JOGADOR]]

        if acao_jogador.tipo == AcoesJogador.MOVER:
            direcao = acao_jogador.parametros
            direcoes_validas = self.get_direcoes_validas()

            if direcao in direcoes_validas:
                x,y = self.posicao_vazia
                if direcao == DirecaoMover.ESQUERDA:
                    self.tabuleiro[x][y], self.tabuleiro[x][y-1] = self.tabuleiro[x][y-1], self.tabuleiro[x][y]
                elif direcao == DirecaoMover.DIREITA:
                    self.tabuleiro[x][y], self.tabuleiro[x][y+1] = self.tabuleiro[x][y+1], self.tabuleiro[x][y]
                elif direcao == DirecaoMover.CIMA:
                    self.tabuleiro[x][y], self.tabuleiro[x-1][y] = self.tabuleiro[x-1][y], self.tabuleiro[x][y]
                elif direcao == DirecaoMover.BAIXO:
                    self.tabuleiro[x][y], self.tabuleiro[x+1][y] = self.tabuleiro[x+1][y], self.tabuleiro[x][y]
            else:
                print('Direção inválida.')

            self.posicao_vazia = self.descobrir_posicao_vazia()
        return

    def terminarJogo(self):
        print(f'Você completou. Muito Bem!')

    def get_direcoes_validas(self):
        direcoes_validas = list()
        x, y = self.posicao_vazia
            
        if (y-1) <= 2 and (y-1) >= 0:
                direcoes_validas.append(DirecaoMover.ESQUERDA)
        if (y+1) <= 2 and (y+1) >= 0:
                direcoes_validas.append(DirecaoMover.DIREITA)
        if (x-1) <= 2 and (x-1) >= 0:
                direcoes_validas.append(DirecaoMover.CIMA)
        if (x+1) <= 2 and (x+1) >= 0:
                direcoes_validas.append(DirecaoMover.BAIXO)

        return direcoes_validas

    def descobrir_posicao_vazia(self):
            for i in range(3):
                for j in range(3):
                    if self.tabuleiro == 0:
                        return (i, j)
                        

def construir_jogo(*args,**kwargs):
    """ Método factory para uma instância RegrasJogo arbitrária, de acordo com os
    parâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    return EightPuzzle()