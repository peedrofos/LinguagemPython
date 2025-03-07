# 1. Leia dois números, faça a soma e apresente caso seja maior que 15.


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2


if soma > 15:
    print ("A soma dos números é igual a: ",soma)
else:
    print ("A soma dos números é menor do que 15")
