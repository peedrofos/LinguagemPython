# Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.

numero = int(input("Digite um número: "))

for i in range (1,numero+1,1):
    print(f"{numero} x {i} = {numero * i}")