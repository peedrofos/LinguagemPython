# Crie uma função que recebe uma lista de números e retorna a soma apenas dos números pares.

def soma_pares():

    lista = []
    contador = 0
    numero = 1

    while numero != 0:

        numero = int(input("Digite um número (ou 0 para encerrar a lista): "))
        print()

        lista.append(numero)

        if numero % 2 == 0:
            contador += numero

    lista.pop(-1)

    print(f"A lista original digitada é: {lista}")
    print(f"A soma dos números pares desta lista é: {contador}")

soma_pares()