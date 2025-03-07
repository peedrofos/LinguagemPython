# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input("Digite o Primeiro número: "))
n2 = int(input("Digite o Segundo número: "))
lista = []

for i in range (n1+1,n2,1):
    if i > n1 and i < n2:
        lista.append(i)

print(f"O intervalo de números entre o número {n1} e {n2} é: ", lista)