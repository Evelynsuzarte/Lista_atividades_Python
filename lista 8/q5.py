def consultar(lista,chave):
     for c in lista:
          if c == chave:
               return c
     return 0

lista = {'a':'maca','b':'banana','c':'coco'}
buscar = input('buscar por: ')
if consultar(lista,buscar) == 0:
     print('Erro')
else:
     print(lista[consultar(lista,buscar)])
