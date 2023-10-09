desconto = int(input("Digite o desconto"))
valor = int(input('digite o valor total'))
total = valor - ((desconto*valor)/100)
print("Valor do desconto = %i\nValor total = %.2f"%(desconto,total))
