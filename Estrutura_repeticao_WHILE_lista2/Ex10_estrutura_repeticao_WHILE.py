# Implemente um sistema de votação onde o usuário pode votar em candidatos (1 a 4), nulo (5) ou branco (6). 
# O programa deve exibir o total de votos de cada tipo e a porcentagem de votos nulos e brancos. A entrada 0 encerra a votação.

candidato_1 = []
candidato_2 = []
candidato_3 = []
candidato_4 = []
nulo_5 = []
branco_6 = []
voto = 1
total = 0

print()
print("Legenda: ")
print("Candidato A = 1")
print("Candidato B = 2")
print("Candidato C = 3")
print("Candidato D = 4")
print("Nulo = 5")
print("Branco = 6")
print()

while voto != 0:

    print()
    voto = int(input("Digite o seu voto: "))
    if voto == 1:
        candidato_1.append(voto)
    elif voto == 2:
        candidato_2.append(voto)
    elif voto == 3:
        candidato_3.append(voto)
    elif voto == 4:
        candidato_4.append(voto)
    elif voto == 5:
        nulo_5.append(voto)
    elif voto == 6:
        branco_6.append(voto)

total = len(candidato_1) + len(candidato_2) + len(candidato_3) + len(candidato_4) + len(nulo_5) + len(branco_6)

if len(candidato_1) > len(candidato_2) and len(candidato_1) > len(candidato_3) and len(candidato_1) > len(candidato_4) and len(candidato_1) > len(nulo_5) and len(candidato_1) > len(branco_6):
    print(f"O candidato A foi eleito com {len(candidato_1)} votos.") 
elif len(candidato_2) > len(candidato_1) and len(candidato_2) > len(candidato_3) and len(candidato_2) > len(candidato_4) and len(candidato_2) > len(nulo_5) and len(candidato_2) > len(branco_6):
    print(f"O candidato B foi eleito com {len(candidato_2)} votos.")
elif len(candidato_3) > len(candidato_1) and len(candidato_3) > len(candidato_2) and len(candidato_3) > len(candidato_4) and len(candidato_3) > len(nulo_5) and len(candidato_3) > len(branco_6):
    print(f"O candidato C foi eleito com {len(candidato_3)} votos.")
elif len(candidato_4) > len(candidato_1) and len(candidato_4) > len(candidato_2) and len(candidato_4) > len(candidato_3) and len(candidato_4) > len(nulo_5) and len(nulo_5) > len(branco_6):
    print(f"O candidato D foi eleito com {len(candidato_4)} votos.")
elif len(nulo_5) > len(candidato_1) and len(nulo_5) > len(candidato_2) and len(nulo_5) > len(candidato_3) and len(nulo_5) > len(candidato_4) and len(nulo_5) > len(branco_6):
    print(f"A votação teve maioria de votos nulos: {len(nulo_5)}.")
elif len(branco_6) > len(candidato_1) and len(branco_6) > len(candidato_2) and len(branco_6) > len(candidato_3) and len(branco_6) > len(candidato_4) and len(branco_6) > len(nulo_5):
    print(f"A votação teve maioria de votos brancos: {len(branco_6)}.")
    
print()
print(f"O percentual de votos nulos em relação ao total de votos foi de: {((len(nulo_5))*100)/total:.2f}.")    
print(f"O percentual de votos em branco em relação ao total de votos foi de: {(len(branco_6)*100)/total:.2f}.")