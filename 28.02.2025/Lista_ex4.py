# Crie uma função que recebe uma lista de palavras e junta tudo em uma única frase.

def juntar_palavras(lista):
    frase = ""  
    
    for palavra in lista:  
        frase += palavra + " "  
    
    return frase.strip()  

lista = []
palavras = 0

while palavras != 'sair':
    palavras = input("Digite uma lista de palavras (ou sair para encerrar): ")
    lista.append(palavras)

if palavras == 'sair':
        lista.pop(-1)


frase_final = juntar_palavras(lista)
print(frase_final)  