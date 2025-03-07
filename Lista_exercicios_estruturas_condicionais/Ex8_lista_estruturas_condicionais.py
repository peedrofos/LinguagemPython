# 8. Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols de cada time) e informe se o resultado foi um empate, se a vitória
# foi do primeiro time ou do segundo time.


timea = int(input("Digite a quantidade de gols da primeira equipe: "))
timeb = int(input("Digite a quantidade de gols da segunda equipe: "))


match (timea == timeb, timea > timeb, timea < timeb):
        case (True, False, False):
            print("O resultado do jogo foi EMPATE")
        case (False, True, False):
            print("Vencedor da partida: PRIMEIRA EQUIPE")
        case (False, False, True):
            print("Vencedor da partida: SEGUNDA EQUIPE")