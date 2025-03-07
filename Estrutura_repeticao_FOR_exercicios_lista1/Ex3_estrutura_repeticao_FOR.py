# 3. Tabuada
# Peça para o usuário digitar um número e exiba a sua tabuada de 1 a 10.


num =  int(input("Digite um número: "))
for cont in range (1,11):
    print (f"{num} x {cont} = {num*cont}")