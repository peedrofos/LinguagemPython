# 9. Desconto em compras por valor mínimo
# Se o valor da compra for maior que R$150,00, aplique um desconto de R$20,00. Caso contrário, não aplique desconto.


valor = float(input("Informe o valor de sua compra: "))


if valor > 150:
        valor = valor - 20.00
        print ("Você ganhou R$ 20,00 de desconto. O valor final de sua compra é: ", valor)
else:
        print ("Você não ganhou desconto em suas compras")
