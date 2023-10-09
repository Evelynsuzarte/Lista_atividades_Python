def fibonacci(n):
     fib = 0
     if n == 0:
          return 0
     elif n == 1:
          return 1
     elif n > 1:
          fib = (n-1)+(n-2)
          return fib

n = int(input("Digite um numero "))
print(fibonacci(n))

#erro
