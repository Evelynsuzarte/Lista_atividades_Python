def palindromo(palavra):
     q = len(palavra)
     if palavra == palavra[::-1]:
          return 1
     else:
          return 0
          
palavra = input("Digite uma palavra: ")
if palindromo(palavra) == 1:
     print("É um palíndromo")
elif palindromo(palavra) == 0:
     print("Não é um palíndromo")
