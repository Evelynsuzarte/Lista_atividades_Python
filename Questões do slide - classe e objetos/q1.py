class Entrevistado:
     def _init_(self):
          self.nome = ' '
          self.idade = 0
          self.sexo = ' '
          self.filhos = 0
          self.salario = 0.0

def media_salarial(soma_salario):
     media = soma_salario/5
     return media

def menos_de(entrevistas):
     total = 0
     for nome in entrevistas:
          if idade < 30 and filho > 5 and salario < 1000.00:
               total = total + total
     return total

def alto_baixo_salario(entrevistas):
     alto = 0
     baixo = alto
     for nome in entrevistas:
          if salario > alto:
               alto = salario
               sx_a = sexo
     for nome in entrevistas:
          if salario < alto:
               baixo = salario
               sx_b = sexo
     return alto, baixo

#main
entrevistas = {}
soma_salario = 0
print("Bem vindo ao sistema de entrevistas")
for i in range(5):
     print("Entrevista %i"%(i+1)
     e = Entrevistado()
     e.nome = input("Digite seu nome: ")
     e.idade = int(input("Qual sua idade? "))
     e.sexo = input("Digite F para Feminino e M para Masculino: ")
     e.filhos = int(input("Quantos filhos você tem? "))
     e.salario = float(input("Qual o valor do seu salário? "))
     entrevistas[nome] = e
     soma_salario = soma_salario + e.salario

print("Media salarial: %.2f "%media_salarial(entrevistados))
print("Sexo com mais alto salario: %f\nSexo com mais baixo salário: %f"%alto_baixo_salario))
print

