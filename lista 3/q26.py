pos = 0
neg = 0
while True:
     num = int(input('Digite'))
     if num<0 and num!=0:
          neg+=1
     elif num>0 and num!=0:
          pos+=1
     elif num == 0:
          break
print("negativo:%i\npositivo:%i"%(neg,pos))
