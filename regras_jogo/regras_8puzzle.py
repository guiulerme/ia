from regras_jogo.regras_abstratas import AbstractRegrasJogo

class RegrasPuzzle(AbstractRegrasJogo):

    def __init__(self):
        import random
        import numpy as np

        self.movimentos = 0

        numeros = [1,2,3,6,7,0,5,8,4]

        arrs = []

        for i in range(0,3):
            while len(numeros) >= 1:
                parte = numeros[i*3:(i*3)+3]
                arrs.append(parte)
                numeros = numeros[(i*3)+3:]
        
        self.elementos = arrs
        self.elementos = np.array(self.elementos)

        def registrarAgentePersonagem(self, personagem):
            return 1

        def isFim(self):
            final = np.array([1,2,3], [4,5,6], [7,8,0])
            return all(self.elementos[i][j] == final[i][j] for i in range(0,3) for j in range(0,3))

        def gerarCampoVisao(self, id_agente):
            return {"percepcao": tuple(self.elementos)}

        def registrarProximaAcao(self, id_agente, acao):
            self.acao_jogador = acao

        def atualizarEstado(self, tempo):
            from acoes import AcoesJogador
            import numpy as np 

            coord_vazio = np.where(self.elementos == 0)
            lin = coord_vazio[0][0]
            col = coord_vazio[1][0]

            if self.acao_jogador.tipo == AcoesJogador.MOVER:
                direcao = self.acao_jogador.parametros
                if direcao == "cima":
                    if (lin-1) >= 0:
                        self.elementos[lin][col], self.elementos[lin-1][col] = self.elementos[lin-1][col], self.elementos[lin][col]
                        self.movimentos += tempo
                    else:
                        print('Direção inválida.')

                elif direcao == "baixo":
                    if (lin+1) <= 2:
                        self.elementos[lin][col], self.elementos[lin+1][col] = self.elementos[lin+1][col], self.elementos[lin][col]
                        self.movimentos += tempo
                    else:
                        print('Direção inválida.')

                elif direcao == "esquerda":
                    if (col-1) >= 0:
                        self.elementos[lin][col], self.elementos[lin][col-1] = self.elementos[lin][col-1], self.elementos[lin][col]
                        self.movimentos += tempo
                    else:
                        print('Direção inválida.')

                elif direcao == "direita":
                    if (col+1) <= 2:
                        self.elementos[lin][col], self.elementos[lin][col+1] = self.elementos[lin][col+1], self.elementos[lin][col]
                        self.movimentos += tempo
                    else:
                        print('Direção inválida.')
            else:
                raise TypeError

        def terminarJogo(self):
            print(f'Muito bem! Você terminou o jogo com um total de {self.movimentos} movimentos.')