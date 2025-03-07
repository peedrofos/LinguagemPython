# Solicite ao usuário um número inteiro positivo e exiba apenas os números pares de 2 até esse número.

pares = []

num = int(input("Digite um número inteiro positivo: "))
if num <2:
    print()
    print("Por gentileza, digite um número maior do que 2.")

cont = 2
while cont <= num:
    cont % 2 == 0
    pares.append(cont)
    cont += 2 

print()
print(f"Os números pares de 2 até o número {num} são: {pares}")    