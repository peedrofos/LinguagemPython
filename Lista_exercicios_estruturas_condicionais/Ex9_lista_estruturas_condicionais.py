# 9. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M matutino, V Vespertino ou N Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


turno = str(input("Em qual turno você estuda? Responda com M, V ou N. ")).upper()
match turno:
    case 'M':
        print("Bom dia!")
    case 'V':
        print("Boa tarde!")
    case 'N':
        print("Boa noite!")
    case _:
        print("Valor Inválido!")
