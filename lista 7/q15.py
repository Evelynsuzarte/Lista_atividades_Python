def buscar(dicionario,valor):
     for chave in dicionario:
          if dicionario[chave] == valor:
               return chave
     return -1

dic = {'cor':'amarelo','casa':'grande','fruta':'maça'}
valor = input("O que voce quer buscar? cor, casa ou fruta?")
if buscar(dic,valor) == -1:
     print("Não encontrado")
else:
     print("Chave",buscar(dic,valor))
