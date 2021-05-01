from agentes.abstrato import AgenteAbstrato
class AgentePrepostoESHumano(AgenteAbstrato):
    
    def adquirirPercepcao(self, percepcao_mundo):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        elems_dispostos = percepcao_mundo['percepcao']

        linha1 = f'{" |".join(f"{e1:2d}" for e1 in elems_dispostos[0])}'
        linha2 = f'{" |".join(f"{e2:2d}" for e2 in elems_dispostos[1])}'
        linha3 = f'{" |".join(f"{e3:2d}" for e3 in elems_dispostos[2])}'
        print(linha1, '——— '*3, linha2, '——— '*3, linha3, '————'*len(linha3), sep='\n')
    
    def escolherProximaAcao(self):
        from acoes import AcaoJogador

        valido = False
        while valido == False:
            direcao = imput("Qual direção deseja mover (cima, baixo, esquerda, direita)? ")
            if ((direcao = "cima") or (direcao == "baixo") or (direcao == "esquerda") or (direcao == "direita")):
                valido = True
                return AcaoJogador.puxar(direcao)
            else:
                print('Jogada inválida! Tente novamente.') 