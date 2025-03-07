# 7. Contar Números Negativos
# Dada uma lista de números, conte e exiba quantos são negativos.


lista = [-4, 5, 2, 1, -9, -10, -11, -15, -20, 3, 5, 4, 7, -50]


qtd = 0
for numero in lista:
    if numero < 0:
       print("Número: ", numero)
       qtd += 1
print(f"São {qtd} números negativos")
