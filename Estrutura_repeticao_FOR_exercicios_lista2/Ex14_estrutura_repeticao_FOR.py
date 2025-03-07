# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue 
# pedindo até que o usuário informe um valor válido.

for i in range(1, 10):
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if 0 <= nota and nota <= 10:
        print("Nota registrada com Sucesso!")
        break
    else:
        print("A nota informada não é válida. Digite um valor entre 0 e 10!")
