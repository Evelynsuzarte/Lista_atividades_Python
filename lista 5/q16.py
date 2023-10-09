def organize(a,b):
     lista= []
     for i in range(5):
          if a[i]>b[i]:
               lista.append(b[i])
               lista.append(a[i])
               if i == 4:
                    if a[i]<b[i]:
                     lista.append(b[i])
                     lista.append(a[i])
          elif a[i]<b[i]:
               lista.append(a[i])
               lista.append(b[i])
               if i == 4:
                    if a[i]>b[i]:
                         lista.append(a[i])
                         lista.append(b[i])
     return lista

#main

v_a = []
v_b = []
print("Preencha o vetor A:")
for i in range(5):
     n=int(input())
     v_a.append(n)
print("Preencha o vetor B:")
for i in range(5):
     n = int(input())
     v_b.append(n)

print(organize(v_a,v_b))
