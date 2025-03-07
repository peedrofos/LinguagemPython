# Implemente um sistema de caixa registradora onde o usuário insere valores dos produtos.
# A entrada de 0 indica o fim da compra. Exiba o total da compra, peça o valor pago e exiba o troco. 
# Após isso, o programa deve reiniciar para um novo cliente.


while True:
    print("Seja bem-vindo!")
    valor = 1
    lista = []

    while valor != 0:
            valor = float(input("Digite o valor do produto (ou zero para finalizar a compra): "))
            lista.append(valor)
            
    print()
    print(f"O valor total da compra foi de: R$ {sum(lista)}")
    print()

    while valor == 0:
            pagamento = int(input("Qual o valor do pagamento? "))
            if pagamento > sum(lista):
                  print()
                  print(f"O seu troco é de R$ {pagamento - sum(lista)}.")
                  break
            elif pagamento == sum(lista):
                  print()
                  print("Você não terá troco, agradecemos a preferência.")
                  break
            else:
                  print()
                  print("O valor digitado é menor do que o total da compra.")
                  break          
            
    