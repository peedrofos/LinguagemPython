# 11. Crie uma lista com 6 itens e verifique se existe uma palavra dentro dela, utilizando o operador in. Depois, verifique uma palavra que não existe dentro dela utilizando o
# operador not in.


lista = ["Corinthians", "Palmeiras", "Santos", "Sao Paulo", "Bragantino", "Mirassol"]


ver1 = "Corinthians"
ver2 = "Vasco"


if ver1 in lista:
      print(f"A palavra '{ver1}' está na lista.")
else:
      print(f"A palavra '{ver1}' não está na lista.")


if ver2 in lista:
      print(f"A palavra '{ver2}' está na lista.")
else:
      print(f"A palavra '{ver2}' não está na lista.")
