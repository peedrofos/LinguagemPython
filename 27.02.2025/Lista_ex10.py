# Crie uma função que receba uma lista de números e retorne essa lista ordenada em ordem crescente.

def ordenar_lista(lista):
        if lista == 0:  
            return "A lista está vazia. Não é possível ordenar os números."

        lista.sort()
        return lista


lista = []
num = 1

while num != 0:
    num = int(input("Digite um número para a lista (ou 0 para parar): "))
    lista.append(num)

print(f"A lista original é: {lista}")
print(f"A lista ordenada é: {ordenar_lista(lista)}")