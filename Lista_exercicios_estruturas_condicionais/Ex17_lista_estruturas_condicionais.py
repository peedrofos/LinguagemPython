# 17. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


produto1 = float(input("Qual o valor do primeiro produto? "))
produto2 = float(input("Qual o valor do segundo produto?"))
produto3 = float(input("Qual o valor do terceiro produto?"))


if produto1 <= produto2 and produto1 <= produto3:
    print("Você deve comprar o primeiro produto, pois ele é o mais barato.")
elif produto2 <= produto1 and produto2 <= produto3:
    print("Você deve comprar o segundo produto, pois ele é o mais barato.")
else:
    print("Você deve comprar o terceiro produto, pois ele é o mais barato.")
