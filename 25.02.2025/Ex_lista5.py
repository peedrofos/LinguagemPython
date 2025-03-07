# Criar uma lista de números e imprimir apenas os números pares.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for num in lista:
    if num % 2 == 0:
        pares.append(num)

print(f"Lista Completa: {lista}")
print(f"A nova lista contendo apenas os números pares: {pares}")
