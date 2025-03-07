# Criar uma lista de 5 números e multiplicar cada número por 3.

lista = [10, 20, 30, 40, 50]
print("A lista origianl é: ", lista)

multiplicado = 0
lista2 = []

for i in lista:
    multiplicado = i * 3
    lista2.append(multiplicado)

print(f"Os elementos da lista original multiplicados por 3 são: {lista2}")    

