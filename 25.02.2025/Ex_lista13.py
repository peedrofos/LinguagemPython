# Criar uma lista de números e imprimir apenas os números ímpares.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impar = []

for num in lista:
    if num % 2 != 0:
        impar.append(num)

print(f"Lista Completa: {lista}")
print(f"A nova lista contendo apenas os números ímpares: {impar}")