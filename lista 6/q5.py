def ler(str,c,ind):
     lista = list(str)
     lista.insert(ind,c)
     nova = ''.join(lista)
     return nova

#main
str = input("Digite uma palavra: ")
c = input("Digite um caracter: ")
ind = int(input("Digite um indice: "))

print(ler(str,c,ind))
