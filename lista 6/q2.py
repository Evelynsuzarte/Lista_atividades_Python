def plural(palavra):
     p = []
     p = list(palavra)
     quant = len(p)
     if p[quant-1] == 'l':
          p.pop()
          p.append('i')
          p.append('s')
     elif p[quant-1] == 's' or p[quant-1] == 'r' or p[quant-1] == 'z':
          p.append('e')
          p.append('s')
     elif p[quant-1] == 'm':
          p.pop()
          p.append('n')
          p.append('s')
     else:
          p.append('s')

     p = ''.join(p)
     return p

#main
palavra = input("Digite uma palavra: ")
print(plural(palavra))
          
