class Pessoa:
     def _init_(self):
          self.nome = ''
          self.idade = 0
          self.sexo = ''
          self.salario = 0.0

def media_salario(pessoas):
     feminino = 0
     salario = 0
     for i in range(len(pessoas)):
          if pessoas[i].sexo == 'f':
               feminino += 1
               salario = salario + pessoas[i].salario
     return salario/feminino

def maior_salario(pessoas):
     maior = 0
     for i in range(len(pessoas)):
          if pessoas[i].salario > maior:
               maior = pessoas[i].salario
               nome = pessoas[i].nome
               idade = pessoas[i].idade
               sexo = pessoas[i].sexo
     return maior,nome,idade,sexo

pessoas = [] #lista para pessoa
for i in range(3):
     p = Pessoa()
     print("PESSOA %d:"%(i+1))
     p.nome = input("Digite seu nome: ")
     p.idade = int(input("Digite sua idade: "))
     p.sexo = input("Sexo: F - feminino\tM - masculino: ")
     p.salario = float(input("Digite o seu salário: "))
     pessoas.append(p)

print("Media do salario: %.2f"%media_salario(pessoas))
print("O maior salario é de : %.2f e pertence a: %s , idade: %i, sexo : %s"%maior_salario(pessoas))
