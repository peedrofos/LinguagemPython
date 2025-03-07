# 8. Verificação de múltiplo de 5
# Peça um número ao usuário e verifique se ele é múltiplo de 5. Se for,exiba Múltiplo de 5, senão exiba Não é múltiplo de 5.


numero = float(input("Informe um numero: "))


if numero % 5 == 0:
        print ("Este numero é múltiplo de 5")
else:
        print ("Este numero NÃO é múltiplo de 5")
