# 4. Crie um programa que calcule o bônus de um funcionário com base no tempo de serviço:
# Sem bônus para menos de 1 ano;
# Bônus de 5% para 1 a 3 anos;
# Bônus de 10% para 3 a 5 anos;
# Bônus de 15% para mais de 5 anos.
# Solicite o salário e o tempo de serviço, e exiba o salário final com bônus (se aplicável).


Tempo = float(input("Informe o seu tempo de serviço (em anos): "))
Salario = float(input("Informe o seu salário (em R$): "))


if Tempo < 1:
        print ("Você não tem direito a bônus")
if Tempo >= 1 and Tempo <= 3:
        Salario_final = Salario + (Salario * 0.05)
        print ("Seu salario com bonus de 5% e de: ", Salario_final)
if Tempo >= 3 and Tempo <= 5:
        Salario_final = Salario + (Salario * 0.10)
        print ("Seu salario com bonus de 10% e de: ", Salario_final)
if Tempo >5:
        Salario_final = Salario + (Salario * 0.15)
        print ("Seu salario com bonus de 15% e de: ", Salario_final)