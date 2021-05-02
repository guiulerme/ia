from .humano import AgentePrepostoESHumano
from .agentes import AgenteAut
from .tipos import TiposAgentes

def construir_agente(*args, **kwargs):
    tipo_agente = args[0]
    if tipo_agente == TiposAgentes.PREPOSTO_HUMANO:
        return AgentePrepostoESHumano()
    else:
        return AgenteAut(tipo_agente)
    
    raise ValueError("Não foi escolhido nenhum tipo de agente válido.")