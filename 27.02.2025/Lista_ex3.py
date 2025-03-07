# Crie uma função chamada media_lista que recebe uma lista de números e retorna a média deles.

def media_lista(lista):
        if lista == 0:  
            return "A lista está vazia. Não é possível calcular a média."

        return sum(lista) / len(lista)


lista = []
num = 1

while num != 0:
    num = int(input("Digite um número para a lista (ou 0 para parar): "))
    lista.append(num)

print(f"A lista completa é: {lista}")
print(f"A média dos números inseridos na lista é: {media_lista(lista)}")

