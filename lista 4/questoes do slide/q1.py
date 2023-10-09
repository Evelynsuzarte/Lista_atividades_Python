def calcularTemperatura(f):
     celsius = (5/9)*(f-32)
     return celsius

temperatura = int(input('Digite os Celsius: '))
fah = calcularTemperatura(temperatura)
print('%.2f F'%fah)
