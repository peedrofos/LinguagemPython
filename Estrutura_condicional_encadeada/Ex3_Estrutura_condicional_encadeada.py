# 3. Desenvolva um programa que calcule o IMC (Índice de Massa Corporal) de uma pessoa e classifique-a como:
# • "Abaixo do peso" se IMC < 18.5;
# • "Peso normal" se 18.5 ≤ IMC < 25;
# • "Sobrepeso" se 25 ≤ IMC < 30;
# • "Obesidade" se IMC ≥ 30.
# • Receba o peso (kg) e a altura (m) do usuário.


Peso = float(input("Informe o seu peso (em kg): "))
Altura = float(input("Informe a sua altura (em mt): "))
IMC = Peso/(Altura*Altura)    


if IMC < 18.5:
        print ("Abaixo do Peso")
if IMC >= 18.5 and IMC < 25:
        print ("Peso Normal")
if IMC >= 25 and IMC < 30:
        print ("Sobrepeso")
if IMC >= 30:
        print ("Obesidade")
