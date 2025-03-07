# Criar uma lista de strings e verificar quantas vezes uma palavra específica aparece.

lista = ['Pedro', 'Carlos', 'Felipe', 'Claudia', 'Analice', 'Pedro', 'Carlos', 'Felipe', 'Pedro', 'Carlos', 'Felipe']

palavra = 'Pedro'
quantidade = 0  

for item in lista:
    if item == palavra:
        quantidade += 1  
        
print(f"A palavra '{palavra}' aparece {quantidade} vezes na lista.")
