# 15. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.


# As perguntas são:
# “Telefonou para a vítima?"
# “Esteve no local do crime?”
# “Mora perto da vítima?“
# “Devia para a vítima?“
# “Já trabalhou com a vítima?“


pergunta1 = str(input("Você telefonou para a vítima? Responda com SIM ou NÃO. ")).upper()
pergunta2 = str(input("Você esteve no local do crime? Responda com SIM ou NÃO. ")).upper()
pergunta3 = str(input("Você mora perto da vítima? Responda com SIM ou NÃO. ")).upper()
pergunta4 = str(input("Você devia para a vítima? Responda com SIM ou NÃO. ")).upper()
pergunta5 = str(input("Você já trabalhou para a vítima? Responda com SIM ou NÃO. ")).upper()
print("Segue o resumo do questionário:")
print("Você telefonou para a vítima? ", pergunta1)
print("Você esteve no local do crime? ", pergunta2)
print("Você mora perto da vítima? ", pergunta3)
print("Você devia para a vítima? ", pergunta4)
print("Você já trabalhou para a vítima? ", pergunta5)