velocidade = int(input("Digite a velocidade do veiculo: "))
permitida = int(input("Digite a velocidade permitida: "))
porc = (20*permitida)/100
if velocidade == permitida:
     print("Não paga multa")
elif velocidade+porc<permitida:
     print("Paga R$250,00")
elif velocidade+porc>permitida:
     print("Paga R$700,00")
