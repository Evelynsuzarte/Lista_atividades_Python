def raiz (n):
    sub = 1
    soma = 0
    while n!=0:
          n = n - sub
          soma += 1
          sub += 2
    return soma

num = int (input ('Digite um numero que deseja saber a raiz:\n'))
print (raiz (num))