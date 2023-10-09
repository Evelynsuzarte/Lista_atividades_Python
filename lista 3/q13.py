quantidade = 1
n = int(input("Digite: "))
soma = n
while soma<=100:
     n = int(input("Digite: "))
     soma = soma + n
     quantidade +=1
media = soma/quantidade
print("Soma = %i\nMedia = %.2f"%(soma,media))
     
