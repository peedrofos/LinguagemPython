# 13. Divisíveis por 5
# Mostre todos os números divisíveis por 5 no intervalo de 1 a 50.


for cont in range (5, 51, 1):
  if cont % 5 == 0:
    print(f"O número {cont} é divisível por 5")
