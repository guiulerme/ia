from enum import Enum
from dataclasses import dataclass

class AcoesJogador(Enum):
    MOVER = 'mover'

@dataclass
class AcaoJogador():
    tipo: str
    parametros: tuple = tuple()

    @classmethod
    def mover(cls, direcao):
        return cls(AcoesJogador.MOVER, (direcao))