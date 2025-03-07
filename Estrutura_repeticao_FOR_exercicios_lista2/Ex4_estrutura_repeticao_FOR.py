# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
cont = 0

for i in range (1,6):
   numeros = int(input(f"Digite o {i}º número: "))
   soma += numeros
   cont = cont + 1
    
print()
print(f"A soma dos números digitados é: {soma}.")
print()
print(f"A média dos números digitados é: {soma/cont}")
