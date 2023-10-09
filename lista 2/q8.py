resp = input("pense em um numero entre 1 e 4\nele é maior que 3?\nS - sim ou N - não\n")
if resp == 's':
     resp = input("é maior que 3?\n")
     if resp == 's':
          print('4')
     elif resp == 'n':
          print('3')
elif resp == 'n':
     resp = input("é maior que 1?\n")
     if resp == 's':
          print('2')
     elif resp == 'n':
          print('1')
