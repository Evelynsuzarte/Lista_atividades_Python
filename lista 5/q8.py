def ordem(vetor,tamanho):
     for i in range(tamanho):
          if vetor[i]< vetor[i+1]:
               return 0
          elif vetor[i]>vetor[i+i]:
               return 1

lista = []
t = int(input("Qual o tamanho do vetor? "))
for i in range(t):
     n = int(input("Digite o numero: "))
     lista.append(n)
print("Ordem: 0 - crescente e 1 - decrescente:\n %i"%ordem(lista,t))

