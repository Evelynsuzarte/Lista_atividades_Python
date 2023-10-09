def funcao(num):
     resultado = 2*num-7*num+3 
     if resultado == 0:
          return 0
     else:
          return 1

n = int(input("Digite um numero: "))
print("Se for o resultado da função aparecerá 0, caso contrário, aparecerá 1")
print(funcao(n))

