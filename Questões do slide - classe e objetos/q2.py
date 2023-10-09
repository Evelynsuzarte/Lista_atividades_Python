class Banco:
     def _init_(self):
          self.conta = 0
          self.agencia = 0
          self.nome = ''
          self.saldo = 0.0

def media_saldos(banco):
     quant = len(banco)
     somador = 0
     for chave in banco:
          somador = somador + banco[chave].saldo
     media = somador/quant
     return media

def maior_menor(banco):
     maior = 0
     menor = 0
     for chave in banco:
          if banco[chave].saldo > maior:
               maior = banco[chave].saldo
               c_maior = chave
               a_maior = banco[chave].agencia
     menor = maior
     for chave in banco:
          if banco[chave].saldo < menor:
               menor = banco[chave].saldo
               c_menor = chave
               a_menor = banco[chave].agencia
     return c_maior,a_maior,c_menor,a_menor

def menor_de_1000(banco):
     quant = 0
     for chave in banco:
          if banco[chave].saldo < 1000.00:
               quant += 1
     porcentagem = quant/len(banco)*100
     return porcentagem


#main
banco = {}
for i in range(4):
     b = Banco()
     print("Complete com seus dados: ")
     b.conta = int(input("Digite o número da conta: "))
     b.agencia = int(input("Digite o número da sua agência: "))
     b.nome = input("Digite o seu nome: ")
     b.saldo = float(input("Digite o seu saldo atual: RS "))
     banco[b.conta] = b
     print("\n")
print()
print("Media salarial dos clientes: ",media_saldos(banco))
print("Maior saldo e menor saldo:\nAgencia e conta do maior saldo: %i - %i\nAgencia e conta do menor saldo: %i - %i"%maior_menor(banco))
print("Porcentagem de saldo menor que R$1000: %.2f"%menor_de_1000(banco))

