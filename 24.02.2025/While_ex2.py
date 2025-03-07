# Escreva um programa que leia um número inteiro positivo e determine se ele é um
# palíndromo (ou seja, se lido de trás para frente continua igual).

numero = int(input("Digite um número inteiro: "))

if str(numero) == str(numero) [::-1]:
    print("O número é palíndromo")

else:
    print("O número não é palíndromo")


