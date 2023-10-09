def somatotal(n1,n2):
     soma = 0
     for i in range(n1,n2):
          soma = soma + i
     return soma+n2

num1 = int(input("Digite"))
num2 = int(input('Digite'))
print(somatotal(num1,num2))
