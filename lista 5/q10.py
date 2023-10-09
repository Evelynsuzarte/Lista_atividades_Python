def vezes(lista,n):
     contador = 0
     for i in range(10):
          if lista[i] == n:
               contador += 1
          return contador
vetor = []
ult = 0
for i in range(10):
     n = int(input("Digite: "))
     vetor.append(n)
     if i == 9:
          ult = n
print('O numero %d aparece %d vezes' %vezes(vetor,ult))

#TypeError: not enough arguments for format string
