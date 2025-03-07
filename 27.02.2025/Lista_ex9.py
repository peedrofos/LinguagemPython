# Crie uma função que conte quantas vogais existem em uma string fornecida.

def contar_vogais(frase):
    vogais = "aeiouAEIOU"  
    contador = 0

    for i in frase:  
        if i in vogais:  
            contador += 1  

    return contador  


frase = input("Digite uma palavra ou frase: ")
quantidade = contar_vogais(frase)

print(f"A quantidade de vogais na string é: {quantidade}")