import requests
from bs4 import BeautifulSoup

# http:// -> 80
# https:// -> 443
url = "https://search.brave.com/search?q=lofi"
header = {"User_Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

requisicao = requests.get(url=url, headers=header)
print(requisicao.status_code)
# print(requisicao.content)
# print(requisicao.text)
# print(requisicao.reason)

site = BeautifulSoup(requisicao.text, "html.parser")
# print(site.prettify())

pesquisa = site.find("input", class_="desktop-large-regular")
print(pesquisa.get_text())

decricao = site.find("section", class_="svelte-eog7cz")
print(decricao.text)

title = site.find("title")
print(title.text)

youtube = site.find("div", class_="title")
print(youtube.text)

wikipedia = site.find("div", class_="svelte-fgmafh")
print(wikipedia.text)
print(wikipedia.parent)