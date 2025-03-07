# Crie uma função que receba um número e retorne Par; se o número for par ou Ímpar se o número for ímpar.

par_impar = int(input("Digite um número: "))

def verifica(par_impar):
    if par_impar % 2 == 0:
        return 'O número é PAR'
    else:
        return 'O número é ÍMPAR'
    
print(f"O número é {verifica(par_impar)}")    