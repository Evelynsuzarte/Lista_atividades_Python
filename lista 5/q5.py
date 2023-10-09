def voltas(quant,vetor):
     melhor = 0
     soma = 0
     m_tempo = 0
     for i in range(quant):
          if vetor[i] > melhor:
               melhor = vetor[i]
               m_tempo = i+1
     for i in range(quant):
          soma = soma + vetor[i]

     return m_tempo,melhor,soma/quant

vetor = []
quant = int(input("Quantas voltas? "))
for i in range(quant):
     v = int(input("Digite o tempo %i: "%(i+1)))
     assert isinstance(v,int) and v > 0
     vetor.append(v)
     
print("Melhor volta = %i - %i minutos\nMedia de tempo: %.2f"%voltas(quant,vetor))
