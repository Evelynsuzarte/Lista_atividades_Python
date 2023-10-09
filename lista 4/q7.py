def area(a,conversao):
    if conversao == 'p':
       return a*24200
    elif conversao == 'm':
       return a*48400
    elif conversao == 'b':
       return a*96800 

a = int(input ('Digite a medida:'))
c = input ('Como deseja converter?')
print(area (a,c))