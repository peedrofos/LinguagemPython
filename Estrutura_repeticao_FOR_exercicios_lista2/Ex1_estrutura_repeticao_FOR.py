# Faça um programa que leia 5 números e informe o maior número.

lista = []
for i in range (1,6):
    num = int(input(f"Digite o {i}º número: "))
    lista.append(num)

print("O maior número da lista é: ", max(lista))