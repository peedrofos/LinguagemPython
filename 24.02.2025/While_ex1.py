# Escreva um programa que leia um número N e imprima todos os termos da sequência de
# Fibonacci até que o maior termo seja menor ou igual a N.

sequencia = 0
numero = int(input("Digite um número: "))

if numero == 0:
    lista = [0]

else:
    lista = [0,1]

while sequencia <= numero:
        sequencia = lista[-1] + lista[-2]
        lista.append(sequencia)
        if sequencia > numero:
            break

print(f"A sequência Fibonacci do número digitado é: {lista[:-1]}")    

