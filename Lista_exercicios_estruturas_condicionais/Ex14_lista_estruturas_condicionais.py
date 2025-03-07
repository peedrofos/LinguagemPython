# 14. Faça um programa que receba a idade de uma pessoa e imprima sua condição (obrigatória, optativa ou proibida), em relação ao ato de votar, conforme apresentado abaixo:
# Pessoas com idade menor que 16 anos são proibidas de votar (proibido);
# Pessoas com idade igual a 16 e menor que 18 anos não são obrigadas a votar (optativo);
# Pessoas com idade igual a 18 e menor que 65 anos são obrigadas a votar (obrigatório);
# Pessoas com idade igual ou maior a 65 anos não são obrigadas a votar (optativo).


idade = int(input("Digite a sua idade: "))


if idade < 16:
    print ("PROIBIDO! Você não está habilitado a votar.")
if idade >= 16 and idade < 18:
    print ("OPTATIVO! Você está habilitado a votar mas seu voto não é obrigatório.")
if idade >= 18 and idade < 65:
    print ("OBRIGATÓRIO! Você está habilitado a votar e seu voto é obrigatório.")
if idade >= 65:
    print ("OPTATIVO! Você está habilitado a votar mas seu voto não é obrigatório.")
