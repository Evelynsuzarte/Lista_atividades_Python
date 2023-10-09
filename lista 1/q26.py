valor = int(input("Digite o valor"))
promo = valor - ((valor*25)/100)
arre = (80*80)/100*promo
arre2 = (80*50)/100*valor
dif = arre - arre2
print("diaria promocional : %.2f\ntotal arrecadado com 80 : %.2f\ntotal arrecadado com 50 : %.2f\ndiferencia entre os dois : %.2f" %(promo,arre,arre2,dif))
