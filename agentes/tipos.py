from enum import Enum

class TiposAgentes(Enum):
    PREPOSTO_HUMANO = 'Preposto humano'
    AUTO_BFS = 'Automático BFS'
    AUTO_DFS = 'Automático DFS'
    AUTO_GULOSO = 'Automático GULOSO'
    AUTO_ESTRELA = 'Automático ESTRELA'
    
    # adicionar outros tipos de agentes de acordo com
    # o necessário