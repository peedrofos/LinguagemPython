# Solicite ao usuário uma nota entre 0 e 10. Caso o valor seja inválido, peça novamente até que o usuário informe um valor válido.

while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if nota < 0 or nota > 10:
        print("Por favor, digite um valor válido!")
        print()
    else:
        print("Nota validada com sucesso!")
        break

