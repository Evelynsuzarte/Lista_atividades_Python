def retan(b,h):
     return b*h

base = int(input("Digite a base: "))
altura = int(input("Digite a altura: "))
print(retan(base,altura))
while base>0 and altura>0:
     base = int(input("Digite a base: "))
     altura = int(input("Digite a altura: "))
     print(retan(base,altura))
