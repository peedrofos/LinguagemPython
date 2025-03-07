# 6. Múltiplos de 3
# Mostre todos os números que são múltiplos de 3 até 30.


for cont in range(3, 31, 1):
      if cont % 3 == 0:
         print(cont, "É múltiplo de 3.")
