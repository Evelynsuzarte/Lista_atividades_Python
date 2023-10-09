def liquidos(unidade):
     pint= 0
     quarto = 0
     galao = 0
     aux = 0
     resto = 0
     if unidade >= 16:
          galao = unidade/16
          aux = unidade%16
          if aux > 0 and aux >= 4:
               quarto = aux/4
               aux = aux % 4
               if aux > 0 and aux >= 2:
                    pint = aux/2
     elif unidade >= 4 and unidade < 16:
          quarto = unidade/4
          aux = unidade%4
          if aux >= 2:
               pint = aux/2
     elif unidade >= 2 and unidade < 4:
          pint = unidade/2

     return galao,quarto,pint

unid = int(input("Digite a unidade de copos: "))
print("Galão = %i \nQuarto = %i \nPint = %i"%liquidos(unid))
