def potencia(b,e):
     if b == 1 and c == 1:
          return 1
     elif b == 0 and c == 0:
          return 0
     else:
          return b ** potencia(b,e)

print(potencia(2,2))
