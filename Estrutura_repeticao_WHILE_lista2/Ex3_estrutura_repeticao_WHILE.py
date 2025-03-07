# Peça ao usuário que insira notas (valores numéricos). 
# A entrada deve continuar até que o usuário digite -1. Em seguida, exiba a média das notas.

media = []
nota = 1

while nota != -1:
    nota = float(input("Digite uma nota: "))
    if nota != -1:
        media.append(nota)
    else:
        print(f"A notas digitadas foram: {media}.")
        print(f"A média das notas digitadas foi: {sum(media)/len(media)}")