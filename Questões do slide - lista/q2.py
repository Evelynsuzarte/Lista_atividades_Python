numeros = []
maior = 0
menor = 0
divisiveis = 0
for i in range(15): #entrada de numeros
     num = int(input('Digite o número da posição %i:\n'%(i+1)))
     assert isinstance (num,int) and num>0
     numeros.append(num)
for i in range(15): #encontrar maior numero
     if numeros[i]> maior:
          maior = numeros[i]
menor = maior
for i in range(15): #encontrar menor numero
     if numeros[i]< menor:
          menor = numeros[i]
for i in range(15): #fazer divisão pelo menor
     if numeros[i]% menor == 0:   
          divisiveis = divisiveis + 1
print("\nVetor de números:\n")
print(numeros)
print("\nMenor valor da lista: %i"%menor)
print("\nQuantidade de números divisíveis pelo menor número: %i"%divisiveis)
     
