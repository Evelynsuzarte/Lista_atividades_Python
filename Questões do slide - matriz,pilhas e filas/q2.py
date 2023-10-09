'''
Escreva um programa que simule o controle de uma pista de decolagem
de aviões em um aeroporto. Neste programa, o usuário deve ser capaz de
realizar as seguintes tarefas:
a) Listar o número de aviões aguardando
na fila de decolagem;
b) Autorizar a decolagem do primeiro avião da fila;
c) Adicionar um avião à fila de espera;
d) Listar todos os aviões na fila de espera;
e) Listar as características do primeiro avião da fila.
Considere que os aviões possuem um nome e um número inteiro como identificador.
Adicione outras características conforme achar necessário.
'''
aviao = 0
fila = []
avioes = {'gol':001, 'tam':002, 'azul':003, 'boing':004, 'air france':005}
while avioes == '\0':
     if avioes == '' :
          aviao =+1

print('Aviões para decolagem:\n')
for i in range(aviao):
     fila.append(avioes(i))
decolagem = fila 
