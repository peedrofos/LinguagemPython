# Criar uma lista de nomes e exibir apenas os nomes que começam com a letra A

lista = ['Amanda', 'Claudia', 'Analice', 'Ariel', 'Pedro', 'Paulo', 'Levi', 'Helena', 'Arlequina']
print(f"A lista original completa é: {lista}")

a = []

for i in lista:
    if i.startswith("A"):
        a.append(i)

print()
print(f"Os nomes da lista que iniciam com a letra A são: {a}")