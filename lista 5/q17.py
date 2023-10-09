def quadrado(matriz):
     linha = 0
     coluna = 0
     diagonal = 0
     diagonal2 = 0
     linha_v = []
     coluna_v = []

     for i in range(3):
          for j in range(3):
               linha = linha+matriz[i][j]
          linha_v.append(linha)
          linha  = 0

     for j in range(3):
          for i in range(3):
               coluna = coluna + matriz[i][j]
          coluna_v.append(coluna)
          coluna = 0

     for i in range(3):
          diagonal = diagonal+matriz[i][i]

     j = 2
     for i in range(3):
          diagonal2 = diagonal2+matriz[i][j]
          j = j - 1

     print(linha_v)
     print(coluna_v)
     print("%i, %i"%(diagonal,diagonal2))

     if linha_v == coluna_v:
          if diagonal == diagonal2:
               return 1
     else:
          return 0

#main

vetor  = []
for i in range(3):
     linha = []
     for j in range(3):
          elemento = int(input("Digite %i:%i: "%(i+1,j+i)))
          linha.append(elemento)
     vetor.append(linha)

print("1 - quadrado perfeito\n 0 - não forma quadrado perfeito")
print(quadrado(vetor))
