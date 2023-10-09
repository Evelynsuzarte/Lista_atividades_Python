def substring(palavra,pi,pf):
     nova = palavra[pi-1:pf]
     return nova

palavra = input("Digite uma palavra: ")
pi = int(input("Ponto inicial: "))
pf = int(input("Ponto final: "))
print(substring(palavra,pi,pf))
