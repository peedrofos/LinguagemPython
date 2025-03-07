# 5. Cálculo de gorjeta
# Peça o valor da conta. Se for maior que R$100,00, adicione uma gorjeta de 10% e exiba o total a pagar. Caso contrário, adicione uma gorjeta de 5%.


valor = float(input("Informe o valor da conta: "))


if valor > 100:
        valor = valor + (valor *0.010)
        print ("Valor total a pagar de ", valor)
else:
        valor = valor + (valor *0.05)
        print ("Valor total a pagar de ", valor)
