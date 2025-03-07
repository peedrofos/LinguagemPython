# 10. Ano bissexto
# Se o ano informado for divisível por 4, exiba Ano bissexto.


ano = float(input("Informe o ano: "))
if ano % 4 == 0:
        print ("Ano BISSEXTO")
else:
        print ("Ano Comum")
