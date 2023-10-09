def maior(matriz):
     k = 0
     lin = 0
     col = 0
     for i in range(5):
          for j in range(3):
               if matriz[i][j] > k:
                    k = matriz[i][j]
                    lin = i
                    col = j
     for i in range(5):
          for j in range(3):
               if matriz[i][j] == k and i!= lin and j!= col:
                    k = matriz[i][j]
                    lin = i
                    col = j
     return k,lin+1,col+1

#principal
m = []
for i in range(5):
     linha = []
     for j in range(3):
          n = int(input("Digite o numero %i:%i - "%((i+1,j+1))))
          linha.append(n)
     m.append(linha)

print("Nº - linha - coluna:\n%i - %i - %i"%maior(m))
