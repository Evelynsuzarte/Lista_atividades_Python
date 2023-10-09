quant = int(input("Quantidade: "))
valor = float(input("Digite o valor: "))
imposto = int(input("Digite o valor do imposto: "))
c = quant*valor
i = (c*imposto)/100
print("Imposto: %.2f"%i)
