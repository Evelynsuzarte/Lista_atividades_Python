def ordem(n1,n2,n3):
     if n1<n2<n3:
          return 0
     elif n1>n2>n3:
          return 1

n1 = int(input())
n2 = int(input())
n3 = int(input())
print('0 = crescente e 1 = descescente')
print(ordem(n1,n2,n3))
