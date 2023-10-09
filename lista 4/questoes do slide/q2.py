def divisivel(n1,n2):
     div = n1/n2
     if div >=0:
          return True
     elif div < 0:
          return False

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
if divisivel(n1,n2) == True:
     print("O primeiro numero é divisivel pelo segundo")
elif divisivel(n1,n2) == False:
     print("O primeiro numero nao é divisivel pelo segundo")
          
