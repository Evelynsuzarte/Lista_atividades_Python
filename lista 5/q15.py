def minimax(matriz):
     menor = 0
     maior = 0
     i_m = 0
     j_m = 0
     for i in range(5):
          for j in range(5):
               if matriz[i][j]>maior:
                    maior = matriz[i][j]
                    i_m = i
                    j_m = j
     menor = maior
     for j in range(5):
          if matriz[i_m][j]<menor:
               menor = matriz[i_m][j]

     return maior,menor

m = []
for i in range(5):
     linha = []
     for j in range(5):
          n = int(input("Digite %i:%i "%(i,j)))
          linha.append(n)
     m.append(linha)

print(minimax(m))
