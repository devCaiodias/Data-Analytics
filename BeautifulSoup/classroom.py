from bs4 import BeautifulSoup
import requests

link = "https://search.brave.com/search?q=dolar+hoje"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

requisicao = requests.get(link, headers=header)
print(requisicao)
# print(requisicao.text)
site = BeautifulSoup(requisicao.text, "html.parser")
# print(site.prettify())

title = site.find("title")
print(title)

# pesquisa = site.find_all("input")
# print(pesquisa[0])

pesquisa2 = site.find("input", class_="desktop-large-regular")
print(pesquisa2)

dolar = site.find("span", class_="t-primary")
print(dolar.get_text())