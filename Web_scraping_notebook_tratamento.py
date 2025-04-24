import pandas as pd
import numpy as np
import re

# Caminho do arquivo Excel
caminho = "Notebooks_Kabum.xlsx"

# 1. Ler o arquivo Excel
df = pd.read_excel(caminho)

# 2. Remover entradas que não comecem com "notebook"
df = df[df['descricao'].str.lower().str.startswith('notebook')]

# 3. Tratar valores "Não informado" como ausentes
df.replace('Não informado', np.nan, inplace=True)

# 4. Extrair RAM (GB)
df['ram_gb'] = df['ram'].str.extract(r'(\d{1,2})').astype(float)

# 5. Extrair SSD (convertendo TB para GB quando necessário)
def converter_ssd(valor):
    if pd.isnull(valor):
        return np.nan
    valor = valor.lower()
    if 'tb' in valor:
        num = re.search(r'(\d)', valor)
        return float(num.group(1)) * 1024 if num else np.nan
    elif 'gb' in valor:
        num = re.search(r'(\d{3,4})', valor)
        return float(num.group(1)) if num else np.nan
    return np.nan

df['ssd_gb'] = df['ssd'].apply(converter_ssd)

# 6. Extrair CPU score básico (i3=3, i5=5, etc.)
df['cpu_score'] = df['processador'].str.extract(r'(\d)').astype(float)

# 7. Criar pontuação técnica personalizada
df['pontuacao'] = (
    df['ram_gb'].fillna(0) * 2 +
    df['ssd_gb'].fillna(0) * 0.1 +
    df['cpu_score'].fillna(0) * 3
)

# 8. Converter preco_formatado em número (float)
df['preco'] = df['preco_formatado'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)

# 9. Calcular custo-benefício
df['custo_beneficio'] = df['pontuacao'] / df['preco']

# 10. Corrigir faixa de preco (inclui valores acima de 10 mil)
df['faixa_preco'] = pd.cut(df['preco'], 
                           bins=[0, 2500, 4000, 6000, 10000, float('inf')],
                           labels=['até R$2500', 'R$2501-4000', 'R$4001-6000', 'R$6001-10000', 'acima de R$10000'])

# 11. Ranking de custo-benefício (1 = melhor)
df['ranking_custo_beneficio'] = df['custo_beneficio'].rank(ascending=False, method='min').astype(int)

# 12. Agrupamentos para entender impacto no preco médio
agrupamentos = {
    'Por RAM (GB)': df.groupby('ram_gb')['preco'].mean(),
    'Por SSD (GB)': df.groupby('ssd_gb')['preco'].mean(),
    'Por Processador': df.groupby('processador')['preco'].mean(),
    'Por Marca': df.groupby('marca')['preco'].mean(),
    'Por Tela': df.groupby('tela')['preco'].mean(),
}

# 13. Salvar base tratada e análises em abas separadas
with pd.ExcelWriter("Notebooks_Tratados_Analise.xlsx", engine='xlsxwriter') as writer:
    df.drop(columns=['preco_num'], errors='ignore').to_excel(writer, sheet_name='Avaliação', index=False)
    agrupamentos_df = pd.concat(agrupamentos, axis=1)
    agrupamentos_df.to_excel(writer, sheet_name='Análises')

# 14. Mostrar agrupamentos no console
for titulo, dados in agrupamentos.items():
    print(f"\n===== {titulo} =====")
    print(dados.sort_values())