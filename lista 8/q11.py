class Pet:
     def _init(self,nome,raca,peso,dono):
          self.nome = nome
          self.raca = raca
          self.peso = peso
          self.dono = dono

def ordenar(dicionario):
     dicionario.sort()
     return dicionario

#main
dicionario = {}
for i in range(3):
     c = Pet()
     c.nome = input("Nome do doguinho: ")
     c.raca = input("Raça do doguinho: ")
     c.peso = float(input("Peso do doguinho: "))
     c.dono = input("Nome do dono do doguinho: ")
     dicionario[c.dono] = c

print(ordenar(dicionario))
