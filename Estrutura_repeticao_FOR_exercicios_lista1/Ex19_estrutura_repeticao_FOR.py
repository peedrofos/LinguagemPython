# 19. Contar uma Letra em uma Frase
# Solicite uma frase e uma letra ao usuário e exiba quantas vezes essa letra aparece na frase.


frase = input("Digite uma frase: ").lower()
letra = input("Digite uma letra a ser buscada: ").lower()


qtd = 0


for i in frase:
   if i == letra:
    qtd += 1


print(f"A letra {letra} aparece {qtd} vezes na frase")