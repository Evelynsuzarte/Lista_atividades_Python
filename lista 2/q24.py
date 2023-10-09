d = int(input('quilometros: '))
if 0<=d<=3:
     total = 4+(d*0.50)
elif 3<d<=6:
     total = 4+(d*0.75)
elif d>6:
     total = 4+(d*1.00)
print(total)
