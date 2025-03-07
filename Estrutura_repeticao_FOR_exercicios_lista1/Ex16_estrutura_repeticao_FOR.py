# 16. Exibir Números Ímpares
# Mostre todos os números ímpares de 1 a 20.


impares = 0


for numero in range (1, 21, 1):
   if numero % 2 != 0:
    impares += 1
    print(f"O número {numero} é ímpar.")  


print(f"O total de números ímpares é:  {impares}.")