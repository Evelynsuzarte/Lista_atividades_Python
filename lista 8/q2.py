class Pessoa:
     def _init_(self):
          self.nome = ''
          self.idade = 0
          self.sexo = ''
          self.salario = 0.0

def media_salario(pessoas):
     feminino = 0
     salario = 0
     for chave in pessoas:
          if pessoas[chave].sexo == 'f':
               feminino += 1
               salario = salario + pessoas[chave].salario
     return salario/feminino

def maior_salario(pessoas):
     maior = 0
     for chave in pessoas:
          if pessoas[chave].salario > maior:
               maior = pessoas[chave].salario
               nome = pessoas[chave].nome
               idade = pessoas[chave].idade
               sexo = pessoas[chave].sexo
     return maior,nome,idade,sexo

pessoas = {} #lista para pessoa
for i in range(3):
     p = Pessoa()
     print("PESSOA %d:"%(i+1))
     p.nome = input("Digite seu nome: ")
     p.idade = int(input("Digite sua idade: "))
     p.sexo = input("Sexo: F - feminino\tM - masculino: ")
     p.salario = float(input("Digite o seu salário: "))
     pessoas[p.nome] = p

print("Media do salario: %.2f"%media_salario(pessoas))
print("O maior salario é de : %.2f e pertence a: %s , idade: %i, sexo : %s"%maior_salario(pessoas))
