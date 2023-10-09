class Conta:
     def _init(self):
          self.nome_usuario = ''
          self.email = ''
          self.senha = ''

def cadastrar(contas,nome,email,senha):
     if contas.get(email):
          return False
     ct = Conta(nome, email, senha)
     contas[email] = ct
     return True
contas = {}
print("CADASTRE")
for i in range(3):
     c = Conta()
     c.conta_usuario = input("Digite seu nome de usuario: ")     
     c.email = input("Digite o endereço de email: ")
     c.senha = input("Crie uma senha: ")
     if cadastrar(contas,c.conta_usuario,c.email,c.senha) == True:
          print("Cadastro feito")
     else:
          print("Email existente")
     print(contas)
     
