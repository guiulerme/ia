import copy

from typing import Sequence, Set
from dataclasses import dataclass


@dataclass
class PosicaoVazia():
    x: int
    y: int


@dataclass
class EstadoEightPuzzle():
    tab: []
    posicao_vazia: PosicaoVazia


@dataclass
class Mover():
    direcao: str


class ProblemaEightPuzzle():

    def __init__(self, percepcao_mundo) -> None:
        super().__init__()

        self.percepcao_mundo = percepcao_mundo

    def estado_inicial(self):
        x, y = self.percepcao_mundo.posicao_vazia
        return EstadoEightPuzzle(self.percepcao_mundo.tab, PosicaoVazia(x, y))

    @staticmethod
    def acoes(estado: EstadoEightPuzzle):
        acoes_possiveis = list()
        tab = estado.tab
        x, y = estado.posicao_vazia.x, estado.posicao_vazia.y

        if (y-1) <= 2 and (y-1) >= 0:
            acoes_possiveis.append(Mover('esquerda'))

        if (y+1) <= 2 and (y+1) >= 0:
            acoes_possiveis.append(Mover('direita'))

        if (x-1) <= 2 and (x-1) >= 0:
            acoes_possiveis.append(Mover('cima'))

        if (x+1) <= 2 and (x+1) >= 0:
            acoes_possiveis.append(Mover('baixo'))

        return acoes_possiveis

    @staticmethod
    def resultado(estado: EstadoEightPuzzle, acao: Mover):
        acoes_possiveis = ProblemaEightPuzzle.acoes(estado)

        if acao not in acoes_possiveis:
            raise ValueError("Ação inválida!")

        tab = copy.deepcopy(estado.tab)
        x, y = estado.posicao_vazia.x, estado.posicao_vazia.y

        if acao.direcao == 'esquerda':
            tab[x][y], tab[x][y-1] = tab[x][y-1], tab[x][y]

        elif acao.direcao == 'direita':
            tab[x][y], tab[x][y+1] = tab[x][y+1], tab[x][y]

        elif acao.direcao == 'cima':
            tab[x][y], tab[x-1][y] = tab[x-1][y], tab[x][y]

        elif acao.direcao == 'baixo':
            tab[x][y], tab[x+1][y] = tab[x+1][y], tab[x][y]
        
        x, y = ProblemaEightPuzzle.get_posicao_vazia(tab)
        return EstadoEightPuzzle(tab, PosicaoVazia(x,y))

    @staticmethod
    def teste_objetivo(tab) -> bool:
        parse_tab = list()
        for linha in tab:
            for coluna in linha:
                parse_tab.append(coluna)

        solucao = [1,2,3,4,5,6,7,8,0]
        return parse_tab == solucao
    
    @staticmethod
    def custo() -> int:
        return 1
    
    @staticmethod
    def get_posicao_vazia(tab):
        for linha in range(len(tab)):
            for coluna in range(len(tab[linha])):
                if tab[linha][coluna] == 0:
                    return linha, coluna