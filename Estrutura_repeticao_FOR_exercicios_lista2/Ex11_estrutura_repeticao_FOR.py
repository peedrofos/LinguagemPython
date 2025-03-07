# Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de idade da turma varia 
# entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

turma = []
idade = 0
media = 0

for i in range (1,11):
    idade = int(input("Digite a sua idade: "))
    turma.append(idade)

media = sum(turma)/len(turma)

if media <= 0 and media <= 25:
    print(f"A média da turma ({media}) a qualifica como uma turma JOVEM")
elif media <= 26 and media <= 60:
    print(f"A média da turma ({media}) a qualifica como uma turma ADULTA")
else:
    print(f"A média da turma ({media}) a qualifica como uma turma IDOSA")