# 18. Calcular o Fatorial
# Peça para o usuário digitar um número e exiba o fatorial desse número.


numero = int(input("Digite um número para calcular o fatorial: "))


fatorial = 1
for cont in range(numero, 0, -1):  
    fatorial = fatorial * cont
    print(fatorial)


print(f"O fatorial de {numero} é {fatorial}")
