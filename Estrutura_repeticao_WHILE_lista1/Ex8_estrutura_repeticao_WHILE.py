# Encontrando o maior número inserido pelo usuário. Peça números ao usuário e, ao digitar 0, exiba o maior número inserido.

maior = 0

num = int(input("Digite um número: "))
maior = num

while num != 0:
            print()
            num = int(input("Digite outro número: "))
            print()
            if num > maior:
                  maior = num
                
print(f"O maior número digitado foi: {maior}")        
