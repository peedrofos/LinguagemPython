# Crie uma função que recebe uma lista de números e retorna a quantidade de números positivos.

def numeros_positivos():

    lista = []
    contador = 0

    while True:

        numero = int(input("Digite um número (ou 0 para encerrar a lista): "))
        if numero == 0:
            break

        lista.append(numero)

        if numero > 0:
            contador += 1

    print(f"A lista original digitada é: {lista}")
    print(f"A quantidade de números positivos desta lista é: {contador}")

numeros_positivos()

    