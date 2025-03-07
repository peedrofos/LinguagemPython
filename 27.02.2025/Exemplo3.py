# Número para ou ímpar

numero = int(input("Digite um número para saber se ele é par ou ímpar: "))

def par_impar (numero):
    if numero % 2 == 0:
        return 'PAR'
    else:
        return 'ÍMPAR'
    
print(f"O número é {par_impar(numero)}")    