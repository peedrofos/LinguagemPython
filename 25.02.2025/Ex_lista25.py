# Criar uma lista com 5 elementos e verificar se um número específico está presente.

lista = [10, 20, 30, 40, 50]
print(f"A lista original é: {lista}")

numero = 10

for i in lista:
    if i == numero:
        print(f"O número {numero} está presente na lista")
        break
else:
    print(f"O número {numero} não está presente na lista")