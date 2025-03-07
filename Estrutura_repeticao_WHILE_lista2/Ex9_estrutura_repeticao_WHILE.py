# Implemente um sistema onde o usuário insere o código e a quantidade dos produtos desejados. 
# O programa deve calcular o valor total e permitir que o usuário finalize o pedido digitando 0.

print("Produto       - Valor   - Código")
print("Big Mac       - 30,00   - 1000")
print("Macflury      - 15,00   - 2000")
print("Free Refill   - 10,00   - 3000")
print()

qtd_1000 = 0
qtd_2000 = 0
qtd_3000 = 0

codigo = 1  

while codigo != 0:
    codigo = int(input("Digite o código do produto (ou 0 para finalizar o pedido): "))

    if codigo == 0:
        break 

    elif codigo == 1000:
        quantidade = int(input("Digite a quantidade desejada: "))
        qtd_1000 += quantidade  

    elif codigo == 2000:
        quantidade = int(input("Digite a quantidade desejada: "))
        qtd_2000 += quantidade

    elif codigo == 3000:
        quantidade = int(input("Digite a quantidade desejada: "))
        qtd_3000 += quantidade

    else:
        print("Código inválido! Tente novamente.")

preco_1000 = 30.00
preco_2000 = 15.00
preco_3000 = 10.00

valor_final = (qtd_1000 * preco_1000) + (qtd_2000 * preco_2000) + (qtd_3000 * preco_3000)

print(f"\nO valor final da compra é de R$ {valor_final:.2f}")

        
