from abc import ABC, abstractmethod
class AgenteAbstrato(ABC):
    '''
    Classe abstrata de agentes artificiais racionais.
    '''

    @abstractmethod
    def adquirirPercepcao(self, percepcao_mundo):
        ''' Forma uma percepcao interna por meio de seus sensores, a partir das
        informacoes de um objeto de visao de mundo.
        '''
        return
    
    @abstractmethod
    def escolherProximaAcao(self):
        ''' Escolhe proxima acao, com base em seu entendimento do mundo, a partir
        das percepções anteriores.
        '''
        return

def construir_agente(tipoAgente, personagem):
    """ Método factory para uma instância Agente arbitrária, de acordo com os
    paraâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    from agentes.humano import AgentePrepostoESHumano
    from agentes.agente_bfs import AgenteClassificadorBFS
    from agentes.agente_dfs import AgenteClassificadorDFS

    if personagem == "O_JOGADOR":
        if tipoAgente == "PREPOSTO_HUMANO":
            return AgentePrepostoESHumano()

        elif tipoAgente == "AUTO_BFS":
            return AgenteClassificadorBFS()

        elif tipoAgente == "AUTO_DFS":
            return AgenteClassificadorDFS()

        else:
            raise ValueError('Agente inválido.')

    else:
        raise ValueError('Jogador inválido.')