def media (lista):
     mult = 0
     aux = 0
     soma = 0
     for i in range(5):
          mult = lista[i] * (i+1)
          aux = aux + mult
          soma = soma + (i+1)
     return aux/soma

lista = []
for i in range(5):
     item = int(input("Digite o numero %i: "%(i+1)))
     lista.append(item)
print("Media ponderada: %.2f"%media(lista))
