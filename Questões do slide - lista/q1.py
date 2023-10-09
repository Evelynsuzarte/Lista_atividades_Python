vetor_a = []   #lista a
vetor_b = []   #lista b
vetor_c = []   #lista c - soma de a e b
print("Vetor A\n")
for i in range(10): #loop para adicionar em a
     num = int(input('Digite um numero:\n'))
     vetor_a.append(num)
     
print("Vetor B\n")     
for i in range(10): #loop para adicionar em b
     num = int(input('Digite um numero:\n'))
     vetor_b.append(num)
     
for i in range(10): #loop para soma e adicionar em c
     vetor_c.append(vetor_a[i]+vetor_b[i])

print("\nVetor C\n")
for i in range(10): #vetor de print de c
     print("%i"%vetor_c[i])
