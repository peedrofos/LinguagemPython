# Crie uma função que recebe uma lista de palavras e retorna a palavra com mais letras.

def maior_palavra(lista_de_palavras):
    maior = ""  
    
    for palavra in lista_de_palavras:  
        if len(palavra) > len(maior):
             maior = palavra  
    
    return (maior)  

lista_de_palavras = []
palavra = 'entrar'

while palavra != 'sair':
    palavra = input("Digite uma lista de palavras (ou sair para encerrar): ")
    lista_de_palavras.append(palavra)

lista_de_palavras.pop(-1)

print(f"A maior palavra da sua lista é: {maior_palavra(lista_de_palavras)}")  