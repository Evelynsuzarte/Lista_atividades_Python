def buscar(lista,numero):
     for i in range(len(lista)):
          if lista[i] == numero:
               return i
     return -1

def delete(lista,numero):
     if buscar(lista,numero) == -1:
          print("Erro")
          print(lista)

     else:
          lista.remove(numero)
          print("Removido: ")
          print(lista)

lista = [5,6,7,8,9,10,20,30,50,60]
apagar = int(input("Qual deseja apagar? "))
delete(lista,apagar)
          
