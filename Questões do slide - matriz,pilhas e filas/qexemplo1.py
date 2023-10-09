#Programa que lê 3 notas de 5 alunos e as armazena em uma
#matriz de ordem 5 X 3 de números reais,
#e em seguida imprime os valores lidos.

alunos = []
for i in range(5):
     notas = []
     for j in range(3):
          nota = float(input("Digite a nota do aluno %i: "%(i+1)))
          notas.append(nota)
     alunos.append(notas)

print(alunos)
          
