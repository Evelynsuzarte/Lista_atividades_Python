def conta(idade,card):
     fct = card + 0.6 *((220-idade)-card)
     return fct

idade = int(input("Digite sua idade"))
card = int(input("Digite a frequencia cardiaca"))
total = conta(idade,card)
print(total)
while idade > 0:
     idade = int(input("Digite sua idade"))
     card = int(input("Digite a frequencia cardiaca"))
     print(total)

