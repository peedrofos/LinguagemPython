# Crie uma função que receba uma lista de notas e retorne a média das notas.

def media_notas(lista):
        if lista == 0:  
            return "A lista está vazia. Não é possível exibir a média."

        return sum(lista) / len(lista)


lista = []
nota = 1

while nota != 0:
    nota = int(input("Digite uma nota para a lista (ou 0 para parar): "))
    lista.append(nota)

print(f"A lista completa é: {lista}")
print(f"O maior dos números inseridos na lista é: {media_notas(lista):.2f}")