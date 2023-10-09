total = float(input('total'))
din = float(input('din'))
if din>total:
     troco = din-total
     print("%.2f"%troco)
else:
     print("dinheiro insuficiente")
