def compara(matriz1,matriz2):
     for i in range(5):
          for j in range(3):
               if matriz1[i][j] == matriz2[i][j]:
                    return 1
               else:
                    return 0

#função principal
matriz1 = []
matriz2 = []
for i in range(5):
     lista1 = []
     for i in range(3):
          item = int(input("Complete a matriz 1: "))
          lista1.append(item)
     matriz1.append(lista1)

for i in range(5):
     lista2 = []
     for i in range(3):
          item = int(input("Complete a matriz 2: "))
          lista2.append(item)
     matriz2.append(lista2)

if compara(matriz1,matriz2) == 1:
     print("As matrizes são iguais")
else:
     print("As matrizes são diferentes")
         
