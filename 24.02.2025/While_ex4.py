# Escreva um programa que leia um número inteiro positivo e determine se ele é um número
# perfeito. Um número perfeito é aquele cuja soma dos seus divisores próprios (excluindo ele
# mesmo) é igual ao próprio número.

numero = int(input("Digite um número inteiro: "))
contador = 0

print()

for i in range (1,numero -1):
    if numero % i == 0:
        contador += i

if contador == numero:
            print("O número digitado é um número perfeito.")
else:
            print("O número digitado não é um número perfeito.")
