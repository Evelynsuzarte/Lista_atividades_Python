horas = int(input("horas: "))
faltas = int(input("falta: "))
pontos = horas -(2/3)*faltas
if pontos>40:
     print("5000.00")
elif pontos>30 and pontos <=40:
     print("4000.00")
elif pontos>20 and pontos<=30:
     print("2000.00")
elif pontos<=10:
     print("1000.00")
