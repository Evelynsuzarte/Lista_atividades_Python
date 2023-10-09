class Conta_corrente:
     def _init_(self,conta,nome,extras,saldo):
          self.numero_conta = conta
          self.nome = nome
          self.extras = extras
          self.saldo = saldo

def cadastrar(dicionario,conta,nome,extras,saldo):
     if dicionario.get(conta):
          return False
     c = Conta_corrente()
     c.conta = conta
     c.nome = nome
     c.extras = extras
     c.saldo = saldo
     dicionario[conta] = c
     return True

def consulte_saldo(dicionario):    #certo
     for chave in dicionario:
          if dicionario[chave].saldo<100:
               print("Menor que 100: %i"%chave)


def atualizar(dicionario):
     for chave in dicionario:
          if dicionario[chave].saldo<100:
               dicionario[chave].saldo+=200
     return dicionario

def remover(dicionario):
     apagar = []
     for chave in dicionario :
          if dicionario[chave].saldo>1000:
               #dicionario.pop(chave)
               apagar.append(chave)
               
     for i in range(len(apagar)):
          dicionario.pop(apagar[i])

     return dicionario

def atualizar_valor(dicionario):
     for chave in dicionario:
          if dicionario[chave].extras != 0:
               dicionario[chave].saldo -= 50
          else:
               dicionario[chave].saldo -= 10
     return dicionario

dicionario = {}
for i in range(2):
     conta = int(input("Digite o número da conta: "))
     nome = input("Digite seu nome: ")
     extras = int(input("Digite o serviço extras: "))
     saldo = float(input("Digite seu saldo: "))
     if cadastrar(dicionario,conta,nome,extras,saldo)==False:
          print("Erro")
     else:
          cadastrar(dicionario,conta,nome,extras,saldo)

consulte_saldo(dicionario)
dicionario = atualizar(dicionario)
dicionario = remover(dicionario)
dicionario = atualizar_valor(dicionario)
print()
for chave in dicionario:
     print(dicionario[chave].conta)
     print(dicionario[chave].nome)
     print(dicionario[chave].extras)
     print(dicionario[chave].saldo)
     print()
