nota = 1
while nota>0 and nota<10:
     nota = int(input("Digite a nota: "))
     if nota>=7:
          print("Aprovado")
     elif 4<=nota<7:
          print("Em exame")
     elif nota<4:
          print("Reprovado")
