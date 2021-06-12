from agentes.abstrato import AgenteAbstrato
from acoes import AcaoJogador
from copy import deepcopy

class AgentePrepostoEstrela(AgenteAbstrato):
  resolvido = False
  jogadas = []
  caminho = [[[0,1,2],[3,4,5],[6,7,8]]]

  def validarOpcoes(self, tabuleiro):
    opcoes = []
    for i in range(len(tabuleiro)):
      for j in range(len(tabuleiro[i])):
        if tabuleiro[i][j] == 0:
          if i+1 < 3: opcoes.append([i+1,j])
          if i-1 > -1: opcoes.append([i-1,j])

          if j+1 < 3: opcoes.append([i,j+1])
          if j-1 > -1: opcoes.append([i,j-1])
    
    return opcoes

  def gerarEstados(self, opcao, tabuleiro, valendo):
    i, j = opcao
    tabuleiro_aux = deepcopy(tabuleiro)
    tabuleiro_aux2 = deepcopy(tabuleiro)
    
    if i+1 <= 2:
      if tabuleiro_aux[i+1][j] == 0:
        tabuleiro_aux[i+1][j] = tabuleiro_aux[i][j]
        tabuleiro_aux[i][j] = 0
        
    elif i-1 >= 0:
      if tabuleiro_aux[i-1][j] == 0:
        tabuleiro_aux[i-1][j] = tabuleiro_aux[i][j]
        tabuleiro_aux[i][j] = 0

    if j+1 <= 2:
      if tabuleiro_aux[i][j+1] == 0:
        tabuleiro_aux[i][j+1] = tabuleiro_aux[i][j]
        tabuleiro_aux[i][j] = 0
        
    elif j-1 >= 0:
      if tabuleiro_aux[i][j-1] == 0:
        tabuleiro_aux[i][j-1] = tabuleiro_aux[i][j]
        tabuleiro_aux[i][j] = 0

    if tabuleiro_aux not in self.percorridos: self.jogadas.append(opcao)
    
    if valendo == False: 
      tabuleiro_aux[3] = [tabuleiro_aux2[0], tabuleiro_aux2[1], tabuleiro_aux2[2], opcao]

    return tabuleiro_aux
    
  def isFim(self, estado):
    resultado = [True, 0]
    if estado[0][0]!=0: 
      resultado[0] = False 
      resultado[1] = resultado[1] + 1
    if estado[0][2]!=2: 
      resultado[0] = False
      resultado[1] = resultado[1] + 1
    if estado[1][0]!=3: 
      resultado[0] = False
      resultado[1] = resultado[1] + 1
    if estado[1][1]!=4: 
      resultado[0] = False
      resultado[1] = resultado[1] + 1
    if estado[1][2]!=5: 
      resultado[0] = False
      resultado[1] = resultado[1] + 1
    if estado[2][0]!=6: 
      resultado[0] = False
      resultado[1] = resultado[1] + 1
    if estado[2][1]!=7: 
      resultado[0] = False
      resultado[1] = resultado[1] + 1
    if estado[2][2]!=8: 
      resultado[0] = False
      resultado[1] = resultado[1] + 1
    
    return resultado

  def adquirirPercepcao(self, percepcao_mundo):
    self.opcoes = percepcao_mundo.opcoes
    self.borda = percepcao_mundo.borda
    self.percorridos = percepcao_mundo.percorridos
    self.tabuleiro = percepcao_mundo.tabuleiro
    self.tentativas = percepcao_mundo.tentativas + 1
    
    print('jogada')
    print(percepcao_mundo.tabuleiro[0])
    print(percepcao_mundo.tabuleiro[1])
    print(percepcao_mundo.tabuleiro[2])
    
    print('\n')

  def gerarCaminho(self, tabuleiro, caminho, percorridos):
    caminho_aux =  deepcopy(caminho)
    while caminho_aux[0][:3] != tabuleiro:
      ult_percorrido = percorridos[-1]

      if self.isFim(ult_percorrido[:3]) == True:
        caminho_aux.insert(0,ult_percorrido[3])
        
      else:
        for percorrido in percorridos:
          if percorrido[:3] == caminho_aux[0][:3]:
            if percorrido[:3] is not caminho_aux: caminho_aux.insert(0, percorrido[3])

      percorridos.pop(-1)
    return caminho_aux

  def buscaEstrela(self, borda, tabuleiro, percorridos, caminho):
    borda.insert(0, tabuleiro) 
    if not self.resolvido:  
      while len(borda) > 0:
        estado_temp = False
        
        if len(borda) == 1: estado_temp = borda.pop(0)
        else:
          indice = len(borda) - 1 
          estado_temp = borda[-1]
          for i in range(len(borda)-1):
            if self.isFim(borda[i])[1] < self.isFim(estado_temp)[1]:
              estado_temp = borda[i] 
              indice = deepcopy(i)
          borda.pop(indice)
        percorridos.append(estado_temp)
       
        if self.isFim(estado_temp)[0] == True: 
          self.resolvido = True
          print('Resolvi o puzzle!')
          print('Tentativas: ', len(self.jogadas))
          tabuleiro.pop(3)
          return self.gerarCaminho(tabuleiro, caminho, percorridos)
          
          break
        else: 
          filhos = [
            self.gerarEstados(opcao, estado_temp, False) for opcao in self.validarOpcoes(estado_temp)
          ]
          
          for filho in filhos:
            ja_percorrido = False
            for percorrido in percorridos:
              if filho[:3] == percorrido[:3]: ja_percorrido = True
            if ja_percorrido == False: borda.insert(0, filho)

  def escolherProximaAcao(self):
    if not self.resolvido:
      self.caminho = self.buscaEstrela(self.borda, self.tabuleiro, self.percorridos, self.caminho)

    acao = AcaoJogador.mover(self.caminho[0][3][0], self.caminho[0][3][1])
    self.caminho.pop(0)
    return acao