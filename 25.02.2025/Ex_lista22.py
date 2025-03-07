# Criar uma lista de frutas e verificar se banana está presente.

lista = ['maça', 'banana', 'laranja', 'pêssego', 'pêra', 'figo']
print(f"A lista original é: {lista}")

fruta = 'banana'

for i in lista:
    if i == fruta:
        break
    print("A palavra banana está na lista")


