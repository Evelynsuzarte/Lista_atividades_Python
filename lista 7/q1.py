def fib_interativo(n):
     if n == 1 or n == 0:
          return n
     else:
          return fib_interativo(n-1)+fib_interativo(n-2)
    
print(fib_interativo(8))
