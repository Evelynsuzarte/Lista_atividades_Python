def area(numero,tipo):
     if tipo == 'p':
          return numero*24200
     elif tipo == 'm':
          return numero*48400
     elif tipo == 'b':
          return numero*96800

a = int(input("Digite a quantidade de alqueiros: "))
t = input("p - paulista\nm - mineiro\nb - baiano\n")
print(area(a,t))
