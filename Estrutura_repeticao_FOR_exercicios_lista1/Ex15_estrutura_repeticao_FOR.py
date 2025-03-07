# 15. Inverter uma Palavra
# Peça ao usuário para digitar uma palavra e exiba essa palavra invertida.


palavra = input("Digite uma palavra qualquer: ").lower()
inverter = 0


for letra in palavra:
  inverter = palavra [::-1]
  print(f"{inverter}")
