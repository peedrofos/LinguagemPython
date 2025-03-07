# 1. Escreva um programa que leia a nota de um aluno (de 0 a 100) e classifique-a como:


# "A" se nota ≥ 90;
# "B" se 80 ≤ nota < 90;
# "C" se 70 ≤ nota < 80;
# "D" se 60 ≤ nota < 70;
# "F" se nota < 60.


Nota = int(input("Informe a sua nota de 0 a 100: "))
   
if Nota >= 90:
        print ("Parabens, você alcançou nota A")
if 80 <= Nota and Nota < 90:
        print ("Você alcançou nota B")
if 70 <= Nota and Nota < 80:
        print ("Você alcançou nota C")
if 60 <= Nota and Nota < 70:
        print ("Você alcançou nota D")
if Nota < 60:
        print ("Cuidado, você alcançou apenas a nota F")
