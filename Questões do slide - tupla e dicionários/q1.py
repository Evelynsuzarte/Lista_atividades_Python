particulas = {}
maior = 0
menor = 0
menor2 = 0
def dic(particulas):
     lista = []
     for p in particulas:
          if particulas[p] > maior:
                maior = p
                menor = maior
     for p in particulas:
          if particulas[p] < menor:
                    menor = p
     for p in particulas:        
          if particulas[p] == menor:
                    menor == p

     lista.append(menor)
     lista.append(menor2)
     return lista

while True:
     p = input('Digite o nome da partícula: ')
     particulas[p] = float(input("Digite a probabilidade da partícula: "))
     if p == 0:
          break


print(dic(particulas))


