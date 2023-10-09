maior7 = 0
porc7 = 0
maior4 = 0
porc4 = 0
menor4 = 0
porcm4 = 0
media = 0
soma = 0
total = 0

for i in range(10):
     nota = int(input("Digite a nota:"))
     if nota>=7:
          maior7+=1
          total = total+nota
     elif nota>=4 and nota<7:
          maior4+=1
          total = total+nota
     elif nota<4:
          menor4+=1
          total = total+nota
          
soma = maior7+maior4+menor4
porc7 = (soma*maior7)/100
porc4 = (soma*maior4)/100
porcm4 = (soma*menor4)/100
media = total/soma

print("Notas maiores que 7: %i"%maior7)
print("Notas maiores ou igual a 4 ou igual a 7: %i"%maior4)
print("Notas menores que 4: %i"%menor4)
print("Porcetagem: maiores que 7: %f "%porc7)
print("Porcetagem: maiores ou igual a 4 ou igual a 7: %f  "%porc4)
print("Porcetagem: menores que 4: %f "%porcm4)
print("Media: %f "%media)
