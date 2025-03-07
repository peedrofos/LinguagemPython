# 5. Escreva um programa que leia a velocidade de um veículo e a classifique em:
# • "Baixa velocidade" para velocidades até 40 km/h;
# • "Velocidade moderada" para velocidades entre 41 e 80 km/h;
# • "Velocidade alta" para velocidades entre 81 e 120 km/h;
# • "Velocidade muito alta" para velocidades acima de 120 km/h.


Velocidade = float(input("Informe a velocidade do veiculo (em km): "))


if Velocidade < 40:
        print ("Baixa Velocidade")
if Velocidade >= 41 and Velocidade <= 80:
        print ("Velocidade Moderada")
if Velocidade >= 81 and Velocidade <= 120:
        print ("Velocidade Alta")
if Velocidade > 120:
        print ("Velocidade Muito Alta")
