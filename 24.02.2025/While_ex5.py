
# Escreva um programa que leia um número inteiro positivo e determine se ele é um
# quadrado perfeito (ou seja, se existe um número inteiro x tal que x² = n).

num = int(input("Digite um número inteiro positivo: "))

if num < 0:
    print("O número deve ser positivo.")
else:
    raiz = 0
    quadrado = 0
    
    while raiz * raiz <= num:
        if raiz * raiz == num:
            quadrado = raiz
            break
        raiz += 1
    
    if quadrado == raiz:
        print(f"{num} é um quadrado perfeito.")
    else:
        print(f"{num} não é um quadrado perfeito.")
