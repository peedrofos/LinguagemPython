# Solicite ao usuário números indefinidamente. O programa deve parar quando o usuário digitar um número igual ao anterior. 
# Em seguida, exiba quantos números foram inseridos.

ultimo = 0
contador = 0  

while True:
    numero = int(input("Digite um número qualquer: "))
    
    if numero == ultimo:
        break

    ultimo = numero
    contador += 1  

print(f"Foram inseridos {contador + 1} números, sendo o número {ultimo} digitado 2X.")
