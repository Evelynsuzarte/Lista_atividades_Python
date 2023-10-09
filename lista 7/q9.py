'''def zero_repetido(lista):
     q = len(lista)
     contador = 0
     j=0
     i=0
     h=0
     repetidos = []
     #for i in range(q):
     while i!=q:
          rept = lista[i]
          for j in range(q):
               if lista[j]==rept:
                    contador+=1
          while h!=contador:
               lista[i] = 0
               h+=1
          q = len(lista)
          i+=1
          
     #for i in range(contador):     #loop para rodar apenas em quantas vezes tem 0
          #lista.remove(repetidos)
     
     return lista

#main
lista = [5,8,0,3,2,0,10,9,2,5,0,0]
print(lista)
print(zero_repetido(lista))
'''
def zero_repetidos(lista):
    listaR=[]
    for elemento in  lista:
        if elemento not in listaR:
            listaR.append(elemento)        
    return listaR
 
lista = [1,1,1,1,2,3,4,5,6,7,8,9,10,10,10,10,22,22,22]

print(zero_repetidos(lista))
