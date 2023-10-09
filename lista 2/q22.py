salario = float(input('seu salario'))
if salario < 500:
     total = ((15*salario)/100)+salario
elif salario>=500 and salario<1000:
     total = ((8*salario)/100)+salario
elif salario>=1000:
     total = ((3*salario)/100)+salario
print(total)
     
