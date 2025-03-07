# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input("Digite um número: "))
contador = 0

if num <= 1:
    print(f" O número {num} não é um número primo!")
else:
    for i in range (1,num+1):
        if num % i == 0:
            contador += 1
        
if contador == 2:
    print(f"O número {num} é primo.")
else:
    print(f"O número {num} não é um número primo!")    
