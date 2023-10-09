def quadrante (n):
    if 0 < n < 90:
       return 1
    elif 90 < n < 180:
       return 2
    elif 180 < n < 270:
       return 3
    elif 270 < n < 360:
        return 4
    elif n==0 or n==90 or n==180 or n==360:
        print('Não reside em nenhum quadrante')
    elif n <0 or n > 360:
        return -1 

angulo = int (input ('Digite um angulo'))
print(quadrante (angulo))
