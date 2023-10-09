def div(n1,n2):
     if n1%n2 == 0:
          return True
     else:
          return False

n1 = int(input("Digite o numero 1: "))
n2 = int(input("Digite o numero 2: "))
print("True -  se num 1 for divisivel por num 2")
print("False - se num 1 não for divisivel por num 2\n")
print(div(n1,n2))
