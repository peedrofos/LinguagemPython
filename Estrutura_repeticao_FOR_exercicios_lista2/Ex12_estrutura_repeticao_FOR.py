# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidato_a = []
candidato_b = []
candidato_c = []

total = int(input("Digite o colégio eleitoral do seu território: "))

print()
print("Legenda: ")
print("Candidato A = 10")
print("Candidato B = 20")
print("Candidato C = 30")
print()

for i in range (1,total + 1):
    print()
    voto = int(input("Digite o seu voto: "))
    if voto == 10:
        candidato_a.append(voto)
    elif voto == 20:
        candidato_b.append(voto)
    elif voto == 30:
        candidato_c.append(voto)
    else:
        print("Você não digitou um candidato válido.")

if len(candidato_a) > len(candidato_b) and len(candidato_a) > len(candidato_c):
    print(f"O candidato A foi eleito com {len(candidato_a)} votos.") 
elif len(candidato_b) > len(candidato_a) and len(candidato_b) > len(candidato_c):
    print(f"O candidato B foi eleito com {len(candidato_b)} votos.")
else:
    print(f"O candidato C foi eleito com {len(candidato_c)} votos.")