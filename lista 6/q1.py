def vogais(frase):
     v = 0
     lista = []
     lista = list(frase)
     for i in range(0,len(lista)):
          if lista[i] == 'a':
               v = v + 1
          elif lista[i] == 'e':
               v = v + 1
          elif lista[i] == 'i':
               v = v + 1
          elif lista[i] == 'o':
               v = v + 1
          elif lista[i] == 'u':
               v = v + 1
     return v

frase = input("Digite uma frase: ")
print("A frase tem %i vogais"%vogais(frase))
