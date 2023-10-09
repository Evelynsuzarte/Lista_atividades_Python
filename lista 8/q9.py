class restaurante:
     def _init_(self,pedido,refeicao,sobremesa,mesa):
          self.pedido = pedido
          self.refeicao = refeicao
          self.sobremesa = sobremesa
          self.mesa = mesa

def cadastro(dicionario,pedido,refeicao,sobremesa,mesa):
     if dicionario.get(pedido):
          return False
     p = restaurante()
     p.pedido = pedido
     p.refeicao = refeicao
     p.sobremesa = sobremesa
     p.mesa = mesa
     dicionario[pedido] = p
     return True

def consultar(dicionario):
     for chave in dicionario:
          if dicionario[chave].refeicao == 'ensopado':
               print("Refeição-Ensopado : %i"%chave)

def atualizar(dicionario):
     for chave in dicionario:
          if dicionario[chave].refeicao == 'feijoada':
               dicionario[chave].sobremesa = True
     return dicionario

def remover(dicionario):
     apagar = []
     for chave in dicionario:
          if dicionario[chave].mesa == 10:
               apagar.append(chave)
     for i in range(len(apagar)):
          dicionario.pop(apagar[i])
          
     return dicionario

#main
dicionario = {}
for i in range(3):
     print("--------- SEU PEDIDO ---------")
     p = restaurante()
     p.pedido = int(input("Pedido nº: "))
     p.refeicao = input("Digite a refeição: ")
     op = input("Sobremesa: s - sim ou n - não: ")
     if op == 's':
          p.sobremesa = True
     elif op == 'n':
          p.sobremesa = False
     if cadastro(dicionario,pedido,refeicao,sobremesa,mesa)== False:
          print('Erro')
     elif cadastro(dicionario,pedido,refeicao,sobremesa,mesa)==True:
          cadastro(dicionario,pedido,refeicao,sobremesa,mesa)

consultar(dicionario)
dicionario = atualizar(dicionario)
dicionario = remover(dicionario)
for chave in dicionario:
     print(dicionario[chave].pedido)
     print(dicionario[chave].refeicao)
     print(dicionario[chave].sobremesa)
     print(dicionario[chave].mesa)
     print()

