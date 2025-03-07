# 8. Pirâmide de Asteriscos
# Peça ao usuário um número e exiba um triângulo de asteriscos com essa altura.


numero = int(input("Digite um número: "))


for cont in range (1, numero + 1):
  print("*" * cont)
