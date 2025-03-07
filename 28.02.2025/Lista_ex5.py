# Crie uma função que recebe uma lista de números e substitui os números negativos por zero.

def substituir_negativos():

    lista = [-1, 2, -5, -6, 3, 4, 5, 10, -20, -8, 6]
    listanova = []

    for i in lista:
        if i < 0:
            listanova.append(0)
        else:
            listanova.append(i)

    print(f"A lista original é: {lista}")
    print()
    print(f"A nova lista com números negativos substituídos por zero é: {listanova}")

substituir_negativos()

