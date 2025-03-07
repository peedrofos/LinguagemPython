# 2. Crie um programa que leia a idade de uma pessoa e imprima:
# "Criança" se a idade for menor que 12;
# "Adolescente" se estiver entre 12 e 17;
# "Adulto" se estiver entre 18 e 64;
# "Idoso" se for 65 ou mais.


Idade = int(input("Informe a sua idade: "))
   
if Idade < 12:
        print ("Criança")
if Idade >= 12 and Idade <= 17:
        print ("Adolescente")
if Idade >= 18 and Idade <= 64:
        print ("Adulto")
if Idade >= 65:
        print ("Idoso")
