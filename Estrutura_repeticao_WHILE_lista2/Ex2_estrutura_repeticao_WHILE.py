# Solicite ao usuário que insira uma senha e continue pedindo até que ele insira a senha correta definida previamente.

senha = 'corinthians'
tentativa = input("Digite uma senha: ")

while tentativa != senha:
    print("Senha incorreta!")
    tentativa = input("Tente novamente: ")
    
print()
print("Parabéns, acesso concedido!")    