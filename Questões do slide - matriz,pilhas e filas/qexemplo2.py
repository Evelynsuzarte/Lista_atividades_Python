#Programa que leia duas matrizes inteiras 3 X 4 e obtenha
#uma terceira matriz resultado da soma
#das duas anteriores. Imprima a matriz resultante.

matriz_a = []
matriz_b = []
matriz_c = []


for i in range(3):
     matriz_a_coluna = []
     for j in range(4):
          item = int(input("Digite um valor para %i: "%(i+1)))
          matriz_a_coluna.append(item)
     matriz_a.append(matriz_a_coluna)

for i in range(3):
     matriz_b_coluna = []
     for j in range(4):
          item = int(input("Digite um valor para %i: "%(i+1)))
          matriz_b_coluna.append(item)
     matriz_b.append(matriz_b_coluna)

for i in range(3):
     matriz_c_coluna = []
     for j in range(4):
          soma = matriz_a[i][j] + matriz_b[i][j]
          matriz_c_coluna.append(soma)
     matriz_a.append(matriz_c_coluna)
'''
for i in range(3):
     for j in range(4):
          print("%i \n" %matriz_c[i][j])
     print()
'''
for i in range(3):
     for j in range(4):
          print('%i %i' % matriz_c[i][j], end = '') #erro
     print()
