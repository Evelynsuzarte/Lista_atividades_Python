resid = 0
comer = 0
indus = 0
sresid = 0
scomer = 0
sindus = 0
for i in range(0,10):
     tipo = int(input("Digite o tipo: "))
     quant = int(input("Digite a quantidade"))
     if tipo == 1:
          resid += 1
          sresid += quant
     elif tipo == 2:
          comer += 1
          scomer += quant
     elif tipo == 3:
          indus += 1
          sindus += quant
media1 = sresid/resid
media2 = scomer/comer
media3 = sindus/indus
total = resid+comer+indus
print("Media:\nresidencial:%.2f\ncomercial:%.2f\nindustrial:%.2f\nTOTAL:%i"%(media1,media2,media3,total))
