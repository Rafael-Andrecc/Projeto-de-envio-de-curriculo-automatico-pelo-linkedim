

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Palavras-chave usadas para busca de vagas
palavras_chave_vagas = [
"estágio", "trainee", "júnior", "vaga para iniciantes", "programador iniciante",
"desenvolvedor júnior", "tecnologia da informação", "TI", "logística",
"desenvolvimento web", "desenvolvimento de software", "back-end", "front-end",
"análise de dados", "data analysis", "banco de dados", "data science", "automação",
"python", "javascript", "html", "css", "bootstrap", "sql", "postgresql", "mysql",
"sqlite", "mongodb", "pandasql", "git", "github", "visual studio code", "vs code",
"criatividade", "trabalho em equipe", "proatividade", "resolução de problemas",
"aprendizado rápido", "comunicação", "flexibilidade", "jovem aprendiz tecnológico",
"remoto", "home office", "presencial", "híbrido", "horário flexível"
]

perguntas_respostas = {
    "Qual sua pretensão salarial?": "R$ 3.000,00",
    "Qual sua área de interesse?": "Tecnologia da Informação e Logística",
    "Qual seu nível de inglês?": "Avançado (certificado pela Wise Up)",
    "Qual seu nível de espanhol?": "Básico",
    "Está disposto a trabalhar presencialmente?": "Sim, inclusive em outras cidades",
    "Tem disponibilidade para trabalho remoto?": "Sim",
    "Você possui experiência profissional anterior?": "Sim, como gestor de envios na Manda Mais Encomendas desde 2021",
    "Possui experiência com programação?": "Sim, com Python, JavaScript e SQL",
    "Possui experiência com desenvolvimento web?": "Sim, com HTML, CSS e Bootstrap",
    "Quais dias da semana você está disponível para trabalhar?": "Segunda a sexta-feira",
    "Qual seu nível de conhecimento em Python?": "Intermediário",
    "Você está matriculado em alguma instituição de ensino?": "Sim, sou estudante de Ciência da Computação na FEI",
    "Qual período do curso você está cursando?": "1º período (início em 2025)",
    "Você está cursando ensino superior?": "Sim, Bacharelado em Ciência da Computação",
    "Possui experiência com bancos de dados?": "Sim, PostgreSQL, MySQL, SQLite e MongoDB",
    "Possui disponibilidade para início imediato?": "Sim",
    "Qual sua disponibilidade de horário?": "Período integral ou flexível, dependendo da necessidade",
    "Por que você quer trabalhar conosco?": "Estou buscando oportunidades para aplicar meus conhecimentos técnicos, crescer profissionalmente e contribuir com soluções criativas",
    "Você tem conhecimento em ferramentas de versionamento como Git?": "Sim, conhecimento básico com Git e GitHub",
    "Está disposto a aprender novas tecnologias?": "Sim, estou sempre buscando evoluir e aprender continuamente",
    "Você está cursando Graduação com formação A PARTIR DE Dezembro/2026": "Sim",
    "Qual é a sua pretensão salarial?": "2000"
}

# Palavras-chave que, se estiverem na pergunta, marcam "Sim" em selects
palavras_chave_sim = [
    "disponível", "presencial", "remoto", "experiência", "viagem", "mudança", "pronto", "trabalhar", "turno", "imediato", "horário", "flexível", "domingo"
]


# Configuração do Chrome com perfil clonado
def candidatura_simp():
    print('entrando na candidatura simples')
    try:
        butao_candidatar = driver.find_element(By.ID, "jobs-apply-button-id")  
        butao_candidatar.click()
    except: 
        print('botao para se candidatar na localizado')
        
    try: 
        butao_avançar = driver.find_element(By.ID, '/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button')
        butao_avançar.click()
    except: 
        print('Impossivel avançar')
        
        
options = Options()
options.add_argument("user-data-dir=/Users/rafaelandre/selenium-profile")  # Perfil isolado só para o Selenium
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("detach", True)  # Mantém o navegador aberto após o script

driver = webdriver.Chrome(options=options)

driver.maximize_window()

# Acessa página inicial (LinkedIn ou outro link de vagas)
driver.get("https://www.linkedin.com/jobs")

# Se quiser continuar login automático com preenchimento (pode ser desnecessário com perfil logado)
usuario = "rafaelandre2103@gmail.com"
senha = "Cirojuliana12345"
Tipo_de_vaga = 'Estagio Desenvolvedor'
wait = WebDriverWait(driver, 10)


def busca_estagio():
    try:
        campo_busca = driver.find_element(By.XPATH, '/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]')
        campo_busca.send_keys(Tipo_de_vaga)
        campo_busca.send_keys(Keys.RETURN)
    except:
        print("❌ Campo de busca não localizado.")
busca_estagio()

def Clik_candidatura_simples():
    # Realiza o clik no butao de candidatura simplificada
    try:
        buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.search-reusables__filter-pill-button'))
        )
        for btn in buttons:
            if "Candidatura simplificada" in btn.text:
                driver.execute_script("arguments[0].scrollIntoView(true);", btn)
                btn.click()
                print("Botão clicado com sucesso!")
                break
    except Exception as e:
        print("Erro ao clicar no botão:", e)
    
Clik_candidatura_simples()
def nivel_experiencia():
    # seleciona nivel de experiencia como estagio 
    try:
        time.sleep(2)
        buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.search-reusables__filter-pill-button'))
        )
        for btn in buttons:
            if "Nível de experiência" in btn.text:
                driver.execute_script("arguments[0].scrollIntoView(true);", btn)
                btn.click()
                estagio_lvl = driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[5]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[1]/label/p/span[1]').click()
                time.sleep(2)
                aplicar_filtro = driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[5]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]').click()
                print("Botão clicado com sucesso!")
                
               
                break
    except Exception as e:
        print("Erro ao clicar no botão:", e)
nivel_experiencia()
    
def Clik_vagas():
  

    try:
        # Seletor para os links das vagas de emprego
        vagas_abertas = driver.find_elements(By.CSS_SELECTOR, 'a.job-card-container__link')
        
        print(f"Encontradas {len(vagas_abertas)} vagas")
        
        for i, vaga in enumerate(vagas_abertas):
            try:
                # Scroll até o elemento para garantir que está visível
                driver.execute_script("arguments[0].scrollIntoView(true);", vaga)
                
                # Pequena pausa para garantir que o elemento está carregado
                time.sleep(1)
                
                # Clica na vaga
                vaga.click()
                print(f"Clicou na vaga {i+1}")
                
                # Pausa entre cliques (opcional, para evitar sobrecarga)
                time.sleep(2)
                
            except Exception as e:
                print(f"Erro ao clicar na vaga {i+1}: {e}")
                continue
                
    except Exception as e:
        print(f'Erro ao encontrar vagas: {e}')

    # Alternativa mais específica (caso a primeira não funcione):
    try:
        # Seletor alternativo usando múltiplas classes
        vagas_abertas = driver.find_elements(By.CSS_SELECTOR, 'a[class*="job-card-container__link"][class*="job-card-list__title--link"]')
        
        print(f"Encontradas {len(vagas_abertas)} vagas (método alternativo)")
        
        for i, vaga in enumerate(vagas_abertas):
            try:
                # Verifica se o elemento é clicável
                if vaga.is_enabled() and vaga.is_displayed():
                    driver.execute_script("arguments[0].scrollIntoView(true);", vaga)
                    time.sleep(1)
                    vaga.click()
                    print(f"Clicou na vaga {i+1}")
                    time.sleep(2)
                else:
                    print(f"Vaga {i+1} não está clicável")
                    
            except Exception as e:
                print(f"Erro ao clicar na vaga {i+1}: {e}")
                continue
                
    except Exception as e:
        print(f'Nenhuma vaga encontrada (método alternativo): {e}')

# Clik_vagas()

def candidatar():
    time.sleep(2)
    try:

       aplicacao_empregos = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'jobs-apply-button-id'))
    )
       aplicacao_empregos.click()

        
        
    except:
        print('aplicao de vaga n localizada, erro na linha 149')
    time.sleep(2)

    try:
        progresso = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div[1]/span')

        while progresso.text != '100%':
            print(f"Progresso atual: {progresso.text}")

            labels = driver.find_elements(By.TAG_NAME, "label")
            for label in labels:
                try:
                    texto_pergunta = label.text.strip().lower()
                    if not texto_pergunta:
                        continue

                    # Busca o campo relacionado
                    campo = label.find_element(By.XPATH, "..//input | ..//textarea | ..//select")
                    tag_name = campo.tag_name.lower()
                    preenchido = campo.get_attribute("value")

                    if preenchido and preenchido.strip() != "":
                        print(f"[Ignorado] Campo já preenchido: {texto_pergunta}")
                        continue

                    # Caso seja SELECT com Sim/Não
                    if tag_name == "select":
                        marcar_sim = any(palavra in texto_pergunta for palavra in palavras_chave_sim)
                        if marcar_sim:
                            for option in campo.find_elements(By.TAG_NAME, "option"):
                                if "sim" in option.text.strip().lower() or "yes" in option.text.strip().lower():
                                    option.click()
                                    print(f"[SELECT] '{texto_pergunta}' → Marcado: Sim")
                                    break
                        elif "não" in option.text.strip().lower() or "no" in option.text.strip().lower():
                                    option.click()
                                    print(f"[SELECT] '{texto_pergunta}' → Marcado: Sim")
                                    break


                    # Caso seja campo de texto/input/textarea
                    elif tag_name in ["input", "textarea"]:
                        resposta_encontrada = None
                        for palavra, resposta in perguntas_respostas.items():
                            if palavra in texto_pergunta:
                                resposta_encontrada = resposta
                                break
                        if resposta_encontrada:
                            campo.clear()
                            campo.send_keys(resposta_encontrada)
                            print(f"[TEXTO] '{texto_pergunta}' → Respondido com: {resposta_encontrada}")
                        else:
                            campo.clear()
                            campo.send_keys("3")  # valor genérico padrão
                            print(f"[TEXTO] '{texto_pergunta}' → Nenhuma correspondência. Preenchido com valor genérico.")

                except Exception as e:
                    print(f"[ERRO] Falha ao processar pergunta '{label.text.strip()}': {e}")

            time.sleep(2)

            avancar = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view'))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", avancar)
            avancar.click()
            time.sleep(1)

            progresso = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div[1]/span')

    except Exception as e:
        print('Não foi possível avançar. Erro na linha 159:', e)
                    

    time.sleep(2)
    try:
            # Espera o botão "Avançar" ficar clicável
            avancar1 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view'))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", avancar1)
            avancar1.click()
            time.sleep(1)  # Espera o próximo formulário carregar

            # Atualiza o progresso após o clique
            progresso = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div[1]/span')

    except Exception as e:
        print('Não foi possível avançar. Erro na linha 159:', e)

candidatar()

time.sleep(100)
driver.close()