# Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja A foi superior a loja B (faturamento = 54000). 
# Se o faturamento atingir esse valor mostre na tela uma mensagem contendo em quanto foi superado o faturamento.

faturamento_a = []
faturamento_b = 54000
compra = 0
diferenca = 0

for i in range (1,6):
    compra = float(input(f"Digite o valor da compra do {i}º cliente: "))
    faturamento_a.append(compra)


if sum(faturamento_a) > faturamento_b:
    diferenca = sum(faturamento_a) - faturamento_b
    print(f"O faturamento da loja A foi MAIOR que o da loja b por: {diferenca:.2f}")
else:
    print("O faturamento da loja a NÃO superou o faturamento da loja b")