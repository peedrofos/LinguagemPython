# 11. Uma empresa resolveu dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça
# um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:


# salários até R$ 280,00 (incluindo): aumento de 20%
# salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
# salários de R$ 1500,00 em diante: aumento de 5%


# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.


salario = float(input("Digite o seu salário atual: "))
salarior = salario
aumento = salario


if salario <= 280:
    salarior = salario + (salario * 0.20)
    aumento = salario * 0.20
    print ("Seu salário antes do reajuste era de: ", salario)
    print ("Seu percentual de aumento foi de 20%")
    print ("O valor do seu aumento foi de: ", aumento)
    print ("Seu novo salário reajustado será de: ", salarior)
if salario >= 280 and salario <= 700:
    salarior = salario + (salario * 0.15)
    aumento = salario * 0.15
    print ("Seu salário antes do reajuste era de: ", salario)
    print ("Seu percentual de aumento foi de 15%")
    print ("O valor do seu aumento foi de: ", aumento)
    print ("Seu novo salário reajustado será de: ", salarior)
if salario >= 700 and salario <= 1.500:
    salarior = salario + (salario * 0.10)
    aumento = salario * 0.10
    print ("Seu salário antes do reajuste era de: ", salario)
    print ("Seu percentual de aumento foi de 10%")
    print ("O valor do seu aumento foi de: ", aumento)
    print ("Seu novo salário reajustado será de: ", salarior)
if salario > 1.500:
    salarior = salario + (salario * 0.05)
    aumento = salario * 0.05
    print ("Seu salário antes do reajuste era de: ", salario)
    print ("Seu percentual de aumento foi de 5%")
    print ("O valor do seu aumento foi de: ", aumento)
    print ("Seu novo salário reajustado será de: ", salarior)