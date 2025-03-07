# Crie uma função que recebe duas palavras e retorna True se forem anagramas uma da outra.

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

def sao_anagramas(palavra1, palavra2):

    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()

    if len(palavra1) != len(palavra2):
        return False
    
    contagem_letras = {}

    for letra in palavra1:
        if letra in contagem_letras:
            contagem_letras[letra] += 1
        else:
            contagem_letras[letra] = 1

    for letra in palavra2:
        if letra in contagem_letras:
            contagem_letras[letra] -= 1
        else:
            return False
        
    for valor in contagem_letras.values():
        if valor != 0:
            return False

print(f"sao_anagramas({palavra1, palavra2})")