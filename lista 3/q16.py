salario = float(input("Digite seu salário: "))
conta = int(input("Quantas contas voce tem para pagar? "))
soma = 0
valor = 0

for i in range(conta):
     valor = int(input('Valor da conta'))
     soma = soma + valor

diferenca = salario-soma 
if  diferenca > salario:
     print("Você consegue pagar as contas\nDiferença:%.2f"%diferenca)
elif diferenca < 0:
     print("Você não consegue pagar as contas, reduza as despesas")
     print("Total das despesas: %i"%soma)
     
