# 17. Criar um Triângulo Numérico
# Solicite um número ao usuário e exiba um triângulo numérico crescente.


numero = int(input("Digite um número: "))


for cont in range (1, numero + 1):
    for cont2 in range (1, cont + 1):
      print(cont2, end=" ")
    print()
