def extremos(vetor_b):
     maior = 0
     p_m = 0
     menor = 0
     p_me = 0
     for i in range(5):
          if vetor_b[i] > maior:
               maior = vetor_b[i]
               p_m = i+1
     menor = maior
     for i in range(5):
          if vetor_b[i] < menor:
               menor = vetor_b[i]
               p_me = i+1
     return maior,p_m,menor,p_me

vetor = []
for i in range(5):
     elemento = int(input("Digite: "))
     vetor.append(elemento)

print('Maior: %i - Posição: %i\nMenor: %i - Posição: %i'%extremos(vetor))
