# 16. Faça um programa que receba a idade de 15 pessoas e que calcule e mostre:
# a) A quantidade de pessoas em cada faixa etária;
# b) A percentagem de pessoas na primeira e na última faixa etária, com relação ao total de pessoas:
# - Até 15 anos
# - De 16 a 30 anos
# - De 31 a 45 anos
# - De 46 a 60 anos
# - Acima de 61 anos

g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0
total = 0
pg1 = 0
pg5 = 0

for i in range (1,16,1):
    idade =  int(input("Digite a sua idade: "))

    if idade <= 15:
        g1 += 1
    elif idade > 15 and idade <= 30:
        g2 += 1 
    elif idade > 30 and idade <= 45:
        g3 += 1 
    elif idade > 45 and idade <= 60:
        g4 += 1
    elif idade >= 61:
        g5 += 1

total = g1 + g2 + g3 + g4 + g5
pg1 = (g1 * 100) / total
pg5 = (g5 * 100) / total

print()
print(f"A quantidade de pessoas em cada faixa etária é: ")
print()
print(f"Até 15 anos: {g1}.")
print(f"De 16 a 30 anos: {g2}.")
print(f"De 31 a 45 anos: {g3}.")
print(f"De 46 a 60 anos: {g4}.")
print(f"Acima de 61 anos: {g5}.")
print()
print(f"A porcentagem de pessoas na 1ª faixa etária em relação ao total é: {pg1}% ")
print(f"A porcentagem de pessoas na últimna faixa etária em relação ao total é: {pg5}% ")


