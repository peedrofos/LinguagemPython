# Uma loja tem tem uma política de descontos de acordo com o valor da compra do cliente. 
# Os descontos começam acima dos R$500. A cada 100 reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até 25%.
# Por exemplo: R$500 = 1% || R$600,00 = 2% … etc…
# Faça um programa que exiba essa tabela de descontos no seguinte formato:
# Valordacompra – porcentagem de desconto – valor final

desconto = 0
valor_final = 0

print("Tabela de descontos da loja:")
print()
print("Valor da Compra - Porcentagem de Desconto - Valor Final de sua Compra")
print()

for compra in range (500,3100,100):
            desconto = (compra - 500) / 100 + 1
            valor_final = compra - (compra * (desconto/100))
            if desconto > 25:
                    desconto = 25
            else:
                print(f"   {compra}   -  {desconto}%   -   {valor_final}")

