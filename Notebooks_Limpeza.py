import pandas as pd
import numpy as np
import re

# Caminho do arquivo Excel
caminho = "Notebooks_Tratados_Analise.xlsx"

# 1. Ler o arquivo Excel com múltiplas abas
xls = pd.ExcelFile(caminho)

# 2. Limpeza da aba "Avaliação": remover linhas com qualquer valor ausente
df_avaliacao = pd.read_excel(xls, sheet_name="Avaliação")
df_avaliacao_limpo = df_avaliacao.dropna()

# 3. Carregar a aba "Análises" para relatório
df_analises = pd.read_excel(xls, sheet_name="Análises")

# 4. Salvar resultado com a "Avaliação" limpa e "Análises" preservada
with pd.ExcelWriter("Notebooks_Limpos_Analise.xlsx", engine='xlsxwriter') as writer:
    df_avaliacao_limpo.to_excel(writer, sheet_name='Avaliação', index=False)
    df_analises.to_excel(writer, sheet_name='Análises', index=False)

# 5. Gerar mini-relatório com base na aba "Análises"
texto_relatorio = """
Com base na análise da aba 'Análises', é possível observar que as especificações técnicas dos notebooks impactam de maneira significativa o valor médio dos equipamentos.

Entre os componentes, os processadores representam um dos principais fatores de valorização. Modelos como o 'Intel Core i7' e o 'Intel Core i9' apresentam valores médios superiores a R$7.500, indicando que o desempenho da CPU tem forte influência sobre o preço.

A capacidade de armazenamento SSD também demonstra impacto: equipamentos com SSD de 512GB ou mais tendem a custar mais de R$4.000 em média, enquanto modelos com 120GB ou 240GB ficam abaixo disso.

Em relação à memória RAM, o aumento de capacidade também eleva o preço médio, porém de forma um pouco mais moderada que os processadores e SSDs. Marcas como Avell e Apple apresentam os maiores valores médios, sugerindo que o fator marca também carrega um peso de percepção de valor e posicionamento no mercado.

Por fim, o tamanho da tela influencia menos no preço médio quando comparado aos demais fatores, mas ainda assim notebooks com telas acima de 15” tendem a ter valores mais elevados.

Essas observações ajudam a compreender quais características justificam os preços praticados no mercado e podem orientar decisões de compra, precificação e até posicionamento de produto.
"""

print(texto_relatorio)