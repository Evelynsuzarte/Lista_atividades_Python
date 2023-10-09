from random import randint

def aleatorio(lista):
     n = randint(0,10)
     print('Numero gerado: %i'%n)
     for i in lista:
          if lista[i] == n:
               return i
     return 1000

#main
lista = [2,4,6,7,8,24,23,12,34,17,35,15]

for i in range(15):
     if aleatorio(lista) == 1000:
          print("Não encontrado")
     else:
          print(aleatorio(lista))
