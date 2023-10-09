'''
def temperatura(msg):
     while True:
          try:
               t1 = float(input("Digite uma temperatura"))
               tipo = input("Digite um tipo para converter\nc - celsius\tf - fahrenheit ")
          except t1<-273.15 and t1<-459.67 :
               print('Você digitou errado')
     if tipo == 'f':
          print('Temperatura em Fahrenheit: %.2f'%1.8*t1+32)
     elif tipo == 'c':
          print('Temperatura em Celsius: %.2f'%(t1-32)/1.8)

mensagem = 'Calculadora de temperatura'
temperatura(mensagem)
'''

def temperatura(msg):
     while True:
          try:
               tipo = input("Digite um tipo para converter\nc - celsius\tf - fahrenheit ")
               if tipo == 'f':
                     t1 = float(input("Digite uma temperatura"))
                     print('Temperatura em Fahrenheit: %.2f'%1.8*t1+32)
          except t1<-459.67 :
                          print('Você digitou errado')

          try:
               tipo = input("Digite um tipo para converter\nc - celsius\tf - fahrenheit ")
               if tipo == 'C':
                     t1 = float(input("Digite uma temperatura"))
                     print('Temperatura em Fahrenheit: %.2f'%1.8*t1+32)
          except t1<-273.15:
                          print('Você digitou errado')

mensagem = 'Calculadora de temperatura'
temperatura(mensagem)

#Use TDD para desenvolver uma função que recebe dois parâmetros: o primeiro é um número inteiro
#ou float que indica uma temperatura, o segundo é um caractere ‘F’ ou ‘C’ para indicar Fahrenheit ou Celsius.
#A função deve retornar a temperatura correspondente convertida para a outra escala.
#A função deve rejeitar temperaturas abaixo do zero absoluto (-273,15 ºC ou -459,67 ºF).
#As fórmulas de conversão são:
#C = (F – 32) / 1.8
#F = 1.8 C + 32
