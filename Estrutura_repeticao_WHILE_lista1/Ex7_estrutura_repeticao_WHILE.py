# Adivinhe o número secreto (de 1 a 10). O usuário deve tentar adivinhar um número até acertar. (Declare um valor e receba outro)

num_secreto = "8"

tentativa = input("Adivinhe qual o número secreto: ")

while tentativa != num_secreto:
    print("Não foi desta vez!")
    print()
    tentativa = input("Tente novamente: ")

print("Você acertou, Parabéns!!!")    