def operacoes(n1,n2):
     soma = n1+n2
     diferenca = n1-n2
     produto = n1*n2
     return soma,diferenca,produto

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
print("Soma: %i \nDiferenca: %i \nProduto: %i"%operacoes(n1,n2))
