eng = 0
comp = 0
mate = 0
maior = 0
curso = 0
#cursom = 0
seng = 0
scomp = 0
smate = 0
ieng = 0
icomp = 0
imate = 0

for i in range(10):
     alunos = int(input("Qual o seu curso?\n1-engenharia\n2-computação\n3-matemárica\n "))
     idade = int(input("Sua idade: "))
     if alunos == 1 :
          eng +=1
          seng = seng + idade
     elif alunos == 2:
          comp += 1
          scomp = scomp + idade
     elif alunos == 3:
          mate += 1
          smate = smate + idade
          
     if alunos == 1 and 25<=idade<=25 :
          ieng += 1
     elif alunos == 2 and 25<=idade<=25:
          icomp += 1
     elif alunos == 3 and 25<=idade<=25:
          imate += 1
          
     if idade > maior:
          maior = idade
          curso = alunos

media1 = seng/eng
media2 = scomp/comp
media3 = smate/mate 

if media1<media2 and media1<media3:
     cursom = 1
elif media2<media1 and media2<media3:
     cursom = 2
elif media3<media1 and media3<media2:
     cursom = 3

print("\nNumero de alunos por curso")
print("Engenharia:%i\nComputação:%i\nMatemática:%i\n"%(eng,comp,mate))
print("Alunos com idade entre 20 e 25 anos:")
print("Engenharia:%i\nComputação:%i\nMatemática:%i\n"%(ieng,icomp,imate))
print("O curso com o aluno mais velho e a idade deste aluno")
print("1. Engenharia\n2. Computação\n3. Matemática\nIdade: %i\tCurso: %i"%(maior,curso))
print("\nO curso com menor média de idade")
print("1. Engenharia\n2. Computação\n3. Matemática\nCurso: %i"%cursom)


     
    
     
     
          
