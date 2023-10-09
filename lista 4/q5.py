def fct(idade,freq):
     FCT = freq+0.6*((220-idade)-freq)
     return FCT

idade = int(input("Digite a idade: "))
freq = int(input("Digite a frequencia cardiaca: "))
print(fct(idade,freq))
while idade>0:
     idade = int(input("Digite a idade: "))
     freq = int(input("Digite a frequencia cardiaca: "))
     print(fct(idade,freq))
