# 16. O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve  ser classificada como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como “Assassino “. Caso contrário, ele será classificado como “Inocente “.


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


respostas = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5]
contador = respostas.count('SIM')


match (contador == 2, contador >= 3 and contador <= 4, contador == 5):
        case (True, False, False):
            print("Classificação: SUSPEITO")
        case (False, True, False):
            print("Classificação: CÚMPLICE")
        case (False, False, True):
            print("Classificação: ASSASSINO")
        case (False, False, True):
            print("Classificação: INOCENTE")
