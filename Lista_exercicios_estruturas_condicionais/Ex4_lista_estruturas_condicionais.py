# 4. Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na tela dizendo se está “quente”, “frio” ou “agradável”.


temp = float(input("Digite a temperatura: "))


if temp < 18:
    print ("O clima está frio")
if temp > 18 and temp <= 25:
    print ("O clima está agradável")
if temp > 25:
    print ("O clima está quente")
