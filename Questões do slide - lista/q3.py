v = []
a = []
b = []

for i in range(10):
     num = int(input("Digite o numero %i:\n"%(i+1)))
     v.append(num)

for i in range(1,10,2):
     a.append(v[i])

for i in range(0,10,2):
     b.append(v[i])
     
print(v)
print(a)
print(b)
