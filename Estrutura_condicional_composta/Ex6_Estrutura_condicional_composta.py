# 6. Acesso ao Wi-Fi
# Peça a senha do Wi-Fi ao usuário. Se for senha123, exiba Conectado, caso contrário, exiba Senha incorreta.


senha = str(input("Informe a senha de rede: "))


if senha == 'senha123':
        print ("CONECTADO")
else:
        print ("SENHA INCORRETA")