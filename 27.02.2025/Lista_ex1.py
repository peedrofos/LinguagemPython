# Crie uma função que receba dois números como parâmetros e retorne a soma deles.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

def soma_numeros (a, b):
    return a + b

print(f"A soma dos números digitados é: {soma_numeros(a, b)}")