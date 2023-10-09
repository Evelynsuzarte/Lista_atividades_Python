class Conta:
     def _init(self):
          self.nome_usuario = ''
          self.email = ''
          self.senha = ''

def buscar(contas,chave):
     for i in range(len(contas)):
          if contas[i].email == chave:
               return i
          else:
               return -1

def cadastrar(contas,nome,email,senha):
     if buscar(contas,nome) == -1:
          c = Conta(nome,email,senha)
          contas.append(c)
          return contas
     else:
          return False
contas = []
nova = []
while True:
     print("CADASTRE")
     c = Conta()
     c.conta_usuario = input("Digite seu nome de usuario: ")
     c.email = input("Digite o endereço de email: ")
     c.senha = input("Crie uma senha: ")
     if cadastrar(contas,c.conta_usuario,c.email,c.senha) != False:
          print("Cadastro feito")
     else:
          print("Email existente")
     print(cadastrar(contas,c.conta_usuario,c.email,c.senha))
          
#corrigir
     
