# Crie uma função que calcule o fatorial de um número.

numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

def calcular_fatorial(fatorial):
    for i in range(numero, 0, -1):  
        fatorial = fatorial * i
        print(f"{fatorial}")


print(f"O fatorial de {numero} é: {fatorial}")

calcular_fatorial(fatorial)