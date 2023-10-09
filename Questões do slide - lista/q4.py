lista_a = []
for i in range(5):
     num = int(input("Digite um numero %i:\n"%(i+1)))
     lista_a.append(num)

buscar = int(input("Qual número deseja buscar?"))

for i in range(5):
     if lista_a == buscar:
         posicao = lista_a.remove(buscar)
         print("Achamos o número desejado!! Está na posição %i\n"%posicao)
         
     elif lista_a != buscar:
          nao_achou = "Não achamos o número desejado!!"

print(nao_achou)
#corrigir cod

