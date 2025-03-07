# 10. Substituir Negativos
# Dada uma lista de números, substitua os números negativos por zero e exiba a nova lista.


lista = [-4, 5, 2, 1, -9, -10, -11, -15, -20, 3, 5, 4, 7, -50]
novalista = []


for numero in lista:
    if numero < 0:
       novalista.append(0)
    else:
       novalista.append(numero)


print(novalista)
