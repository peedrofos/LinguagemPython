# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

par = []
impar = []

for i in range (1,11,1):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print()
print(f"Quantidade de números pares: {len(par)}. Relação de números: {par}")
print()
print(f"Quantidade de números pares: {len(impar)}. Relação de números: {impar}")
