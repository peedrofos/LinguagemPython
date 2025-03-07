# Crie uma função chamada tabuada que recebe um número e imprime sua tabuada do 1 ao 10.

numero = int(input("Digite um número: "))
tabuada = 0

def calcular_tabuada (tabuada):
    for i in range(1, 11):
        tabuada = numero * i
        print(f"{numero} x {i} = {tabuada}")

calcular_tabuada (tabuada)