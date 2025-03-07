# Misturando MAX / MIN em listas

programadores = ['Victor', 'Ana', 'Ada', 'Juliana', 'Henrique', 'Caio', 'Luana']

menor_palavra = min(programadores, key=len)
maior_palavra = max(programadores, key=len)

print(menor_palavra)
print(maior_palavra)