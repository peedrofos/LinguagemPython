# Somar números até o usuário digitar 0. Peça números ao usuário e some-os até que ele digite 0.

soma = 0

num = int(input("Digite um número: "))

while num != 0:
    soma += num
    num = int(input("Digite outro número: "))

print(f"A soma dos números digitados é: {soma}")    