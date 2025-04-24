from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import pandas as pd
import time
import re

# Caminho para o ChromeDriver
chrome_driver_path = "C:\\Program Files\\chromedriver-win64\\chromedriver.exe"

# Configuração do WebDriver
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(service=service, options=options)

# Acessar a página
url_base = 'https://www.kabum.com.br/busca/notebooks?page_number=1&page_size=20&facet_filters=eyJjYXRlZ29yeSI6WyJDb21wdXRhZG9yZXMiXSwicHJpY2UiOnsibWluIjoxMDAwLCJtYXgiOjM1NTU1LjU0fX0=&sort=most_searched&variant=null'
driver.get(url_base)
time.sleep(5)

# Dicionário de dados atualizado
dic_produtos = {
    'descricao': [],
    'preco': [],
    'marca': [],
    'processador': [],
    'ram': [],
    'ssd': [],
    'sistema': [],
    'tela': [],
    'cor': []
}

# Função para extrair informações específicas
def extrair_info(texto):
    texto = texto.lower()

    ram = re.search(r'(\d{1,2}\s?gb)(?!\s?(ssd|hd))', texto)
    ssd = re.search(r'((\d{3,4}\s?gb|\d\s?tb).{0,10}ssd|ssd.{0,10}(\d{3,4}\s?gb|\d\s?tb))', texto)
    processador = re.search(r'(intel\s(core\s)?i[3-9]|ryzen\s?[3-9]|apple\s?m1|celeron|pentium|athlon|intel\s?n\d{3,4})', texto)
    sistema = re.search(r'(windows\s?\d{0,2}|linux|ubuntu|macos|chromeos|macbook)', texto)
    marca = re.search(r'(lenovo|samsung|acer|asus|dell|hp|apple|avell|multilaser|positivo)', texto)
    tela = re.search(r'(\d{2}\.?\d{0,1})\s?(pol|")', texto)
    cor = re.search(r'(preto|cinza|prata|azul|vermelho|branco|rosa|dourado|verde|grafite|chumbo)', texto)

    return {
        'ram': ram.group(1).upper() if ram else 'Não informado',
        'ssd': ssd.group(0).upper() if ssd else 'Não informado',
        'processador': processador.group(1).title() if processador else 'Não informado',
        'sistema': sistema.group(1).capitalize() if sistema else 'Não informado',
        'marca': marca.group(1).capitalize() if marca else 'Não informado',
        'tela': tela.group(1) + '”' if tela else 'Não informado',
        'cor': cor.group(1).capitalize() if cor else 'Não informado'
    }

# Coleta dos dados
pagina = 1
while True:
    print(f"\nColetando dados da página {pagina}...")

    try:
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, "productCard"))
        )
        print("Elementos encontrados com sucesso.")
    except TimeoutException:
        print("Tempo de espera excedido")

    produtos = driver.find_elements(By.CLASS_NAME, "productCard")

    for produto in produtos:
        try:
            nome = produto.find_element(By.CLASS_NAME, "nameCard").text.strip()
            preco = produto.find_element(By.CLASS_NAME, "priceCard").text.strip()

            print(f"{nome} - {preco}")

            info = extrair_info(nome)

            dic_produtos["descricao"].append(nome)
            dic_produtos["preco"].append(preco)
            dic_produtos["marca"].append(info["marca"])
            dic_produtos["processador"].append(info["processador"])
            dic_produtos["ram"].append(info["ram"])
            dic_produtos["ssd"].append(info["ssd"])
            dic_produtos["sistema"].append(info["sistema"])
            dic_produtos["tela"].append(info["tela"])
            dic_produtos["cor"].append(info["cor"])

        except Exception as e:
            print("Erro ao coletar dados:", e)

    try:
        botao_proxima = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.CLASS_NAME, 'nextLink'))
        )
        if botao_proxima:
            driver.execute_script("arguments[0].scrollIntoView();", botao_proxima)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", botao_proxima)
            pagina += 1
            time.sleep(5)
        else:
            print("Você chegou na última página!")
            break

    except Exception as e:
        print("Erro ao tentar avançar para a próxima página", e)
        break

# Finalização
driver.quit()

# Criar DataFrame
df = pd.DataFrame(dic_produtos)

# Processar coluna de preço: limpar e converter
df['preco_num'] = df['preco'].str.replace('R$', '', regex=False)\
                             .str.replace('.', '', regex=False)\
                             .str.replace(',', '.', regex=False)\
                             .astype(float)

# Formatar valor no padrão brasileiro com vírgula
df['preco_formatado'] = df['preco_num'].map(lambda x: f"{x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

# Salvar no Excel com colunas finais
colunas_finais = ['descricao', 'preco_formatado', 'preco_num', 'marca', 'processador', 'ram', 'ssd', 'sistema', 'tela', 'cor']
df[colunas_finais].to_excel("Notebooks_Kabum_Completo.xlsx", index=False)

print(f"Arquivo Excel salvo com sucesso! ({len(df)}) produtos capturados")

