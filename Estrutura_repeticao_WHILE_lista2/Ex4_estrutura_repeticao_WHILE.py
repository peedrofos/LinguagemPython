# Solicite ao usuário que insira números. O programa deve continuar até que um número negativo seja inserido. 
# No final, exiba o maior número informado.

lista = []
numero = 1
maior = 0

while numero > 0:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    if numero > maior:
        maior = numero

print()
print(f"O maior número digitado foi {maior}")        
print()
print(f"A lista de números digitados foi: {lista}")        
        