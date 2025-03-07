# 14. Contar Números Pares em uma Lista
# Dada uma lista de números, conte e exiba quantos são pares.


lista = [-4, 5, 2, 1, -9, -10, -11, -15, -20, 3, 5, 4, 7, -50]


pares = 0


for numero in lista:
   if numero % 2 == 0:
    pares += 1
    print(f"O número {numero} é par")  


print(f"O total de números pares é:  {pares}.")
