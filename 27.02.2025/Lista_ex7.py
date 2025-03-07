# Crie uma função que receba uma lista de números e retorne o maior número dessa lista.

def maior_lista(lista):
        if lista == 0:  
            return "A lista está vazia. Não é possível exibir o maior."

        return max(lista)


lista = []
num = 1

while num != 0:
    num = int(input("Digite um número para a lista (ou 0 para parar): "))
    lista.append(num)

print(f"A lista completa é: {lista}")
print(f"O maior dos números inseridos na lista é: {maior_lista(lista)}")