soma = 0
contador = 0
raiz = int(input("De qual o numero voce quer saber a raiz?"))
for i in range(1,raiz,2):
     soma = soma+i
     contador +=1
     if soma == raiz:
          break
print("A raiz de %i é: %i"%(raiz,contador))
