# 11. Criar uma Sequência Numérica
# Solicite ao usuário um número e exiba os 10 primeiros múltiplos desse número.


numero = int(input("Digite um número: "))


print(f"Os 10 primeiros múltiplos de {numero} são:")
for cont in range(1, 11):
    print(f"{numero} x {cont} = {numero * cont}")