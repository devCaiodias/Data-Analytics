from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Passo 1:
navegador.get("https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M")

# Passo 2
navegador.find_element(
    'xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input'
    ).send_keys("Yuta")

navegador.find_element(
    'xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input'
    ).send_keys("caiodiasmartins12@gmail.com")

navegador.find_element(
    'xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input'
    ).send_keys(5566984279053)

# Passo 3:
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button').click()

# Passo 4:
navegador.find_element('xpath', '//*[@id="popup-container"]/div/div/a[1]').click()

navegador.find_element('xpath', '//*[@id="close-popup"]').click()



while True:
    time.sleep(10)