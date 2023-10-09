def mistura(s1,s2):
     s3 = []
     listas1 = list(s1)
     listas2 = list(s2)
     c1 = len(s1)
     c2 = len(s2)
     if c1>c2:
          for i in range(c1):
               if i != c2:
                    s3.append(s1[i])
                    s3.append(s2[i])
               else:
                    s3.append(s1[i])
     elif c1<c2:
          for i in range(c2):
               if i != c1:
                    s3.append(s1[i])
                    s3.append(s2[i])
               else:
                    s3.append(s2[i])

     s3 = ''.join(s3)
     return s3

#main
s1 = input("Digite uma palavra: ")
s2 = input("Digite uma segunda palavra: ")
print(mistura(s1,s2))


#metade funcionando
