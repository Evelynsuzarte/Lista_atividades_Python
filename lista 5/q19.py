def mat(matriz):
     for i in range(3):
          for j in range(3):
               if matriz[i][j] == 0 and matriz[i][i] == 1:
                    return 1
               else:
                    return 0

#main

m = []
for i in range(3):
     linha = []
     for j in range(3):
          n = int(input("Digite %i:%i : "%(i,j)))
          linha.append(n)
     m.append(linha)

for i in range(3):
          for j in range(3):
               print('%i'%m[i][j],end = '')
          print()

print("1 - identidade\n0 - não é identidade")
print(mat(m))

#nao está testando direito
