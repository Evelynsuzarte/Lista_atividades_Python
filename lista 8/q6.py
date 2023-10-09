def buscar(lista,chave):
     return lista.get(chave)

def update(lista,chave,novo):
     buscado = buscar(lista,chave)
     if lista[chave] == buscado:
               lista[chave] = novo
               return lista[chave]
     else:
          return 0

#main
lista = {'cedo':'manha','xícara':'rosa','9':'aniversario','15':'salario','casa':'perto','6500':'dinheiro'}
chave = input("O que você quer mudar? ")
novo = input("Alteração: ")
print(buscar(lista,chave))
if update(lista,chave,novo) == 0:
     print('Erro')
     print(update(lista,chave,novo))

else:
     print("Objeto atualizado")
     print(update(lista,chave,novo))

