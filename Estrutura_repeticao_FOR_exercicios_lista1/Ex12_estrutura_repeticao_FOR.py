# 12. Contar Vogais
# Peça ao usuário para digitar uma palavra e exiba quantas vogais ela contém.


palavra = input("Digite uma palavra qualquer: ").lower()
vogais = "aeiou"
qtd = 0


for letra in palavra:
  if letra in vogais:
    print(f"A letra {letra} é uma vogal")
    qtd += 1


print(f"A palavra {palavra} possui {qtd} vogais.")
