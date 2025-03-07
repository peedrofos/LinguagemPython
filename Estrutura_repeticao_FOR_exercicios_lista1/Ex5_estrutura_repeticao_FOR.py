# 5. Média de Valores
# Solicite que o usuário digite 5 números e exiba a média aritmética deles.


media = 0


for cont in range(1, 6):
    numero = int(input(f"Digite o {cont}º número: "))
    media += numero


print("A média dos números digitados é: ", media / 5)
