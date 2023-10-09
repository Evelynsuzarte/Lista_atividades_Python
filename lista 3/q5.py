num = int(input("Digite"))
maior = num
menor = num
while True:
     num = int(input("Digite"))
     if num == 0:
          break
     elif num > maior: 
          maior = num    
     elif num < maior: 
          if menor < maior :
                    menor = num
print("O maior é: %i\nO menor é: %i"%(maior,menor))
