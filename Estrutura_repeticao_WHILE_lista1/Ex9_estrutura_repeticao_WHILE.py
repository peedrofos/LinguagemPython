# Contar quantos números pares o usuário digitar. O programa deve contar quantos números pares o usuário inseriu. 
# O usuário para digitando -1.

pares = 0

num = int(input("Digite um número: "))
if num % 2 == 0:
    pares += 1

    while num != -1:
        num = int(input("Digite outro número: "))
        if num % 2 == 0:
            pares += 1

print(f"Foram digitados {pares} números pares")

