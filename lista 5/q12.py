def fatorial(a):
     mult = 0
     b = []
     for i in range(5):
          j = a[i]
          for j in range(j+1,1,-1):
               mult = mult*j
          b.append(mult)
     return b
#main
vetor_a = []
for i in range(5):
     n=int(input("Digite: "))
     vetor_a.append(n)
print(vetor_a)
print(fatorial(vetor_a))
