# O usuário deve digitar a senha correta (1234). Enquanto errar, o programa deve pedir novamente.

senha = "1234"

tentativa = input("Digite a senha de acesso: ")

while tentativa != senha:
    print("Acesso Negado - Senha Incorreta")
    print()
    tentativa = input("Digite a senha de acesso: ")

print()
print("Acesso concedido - Senha Correta")    