# 13. Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit, e que, a
# partir da resposta do usuário, faça a devida conversão.


pergunta1 = str(input("Você gostaria de converter uma temperatura em Celsius para Fahrenheit? Responda com SIM ou NÃO. ")).upper()
if pergunta1 == 'SIM':
    temperatura = float(input("Digite a temperatura em graus Celsius: "))
    temperatura = (temperatura * 1.8) + 32  # Correção na fórmula aqui também!
    print("Essa temperatura equivale a:", temperatura, "graus Fahrenheit")


elif pergunta1 == 'NÃO':
    pergunta2 = str(input("Você gostaria de converter uma temperatura em Fahrenheit para Celsius? Responda com SIM ou NÃO. ")).upper()
    if pergunta2 == 'SIM':
        temperatura = float(input("Digite a temperatura em graus Fahrenheit: "))
        temperatura = (temperatura - 32) / 1.8  # Correção na fórmula aqui também!
        print("Essa temperatura equivale a:", temperatura, "graus Celsius")
    else:
        print("Responda apenas com SIM ou NÃO")


else:
    print("Responda apenas com SIM ou NÃO")