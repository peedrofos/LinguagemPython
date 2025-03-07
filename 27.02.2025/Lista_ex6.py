# Crie uma função que receba uma string e retorne True se ela for um palíndromo 
# (uma palavra ou frase que se lê da mesma forma de trás para frente) e False caso contrário.

def eh_palindromo (palavra):
    return palavra == palavra [::-1]

palavra = input("Digite uma palavra: ")

if eh_palindromo(palavra):
    print("Esta palavra é um palíndromo")
else:
    print("Esta palavra não é um palíndrono")
    


