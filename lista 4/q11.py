def calcula(n1,sinal,n2):
     if sinal == '+':
          return n1+n2
     elif sinal == '-':
          return n1-n2
     elif sinal == '*':
          return n1*n2
     elif sinal == '/':
          if n1/n2 > 0:
               return n1/n2
          elif n1/n2 == 0:
               return 0

num1 = int(input("Digite"))
op = input()
num2 = int(input())
total = calcula(num1,op,num2)
print(total)
