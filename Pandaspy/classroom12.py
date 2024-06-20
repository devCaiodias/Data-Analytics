import pandas as pd
import numpy as np
import pyarrow
from pathlib import Path
import zipfile
import requests 
from io import BytesIO

TIPO_DADOS = 'amostra'

LINK_DADOS = {
    "amostra" : {
        "escola.parquet" : "C:\\Users\\caio\\Data Analytics\\Pandaspy\\dados\\amostra\\aquisicao\\escola.parquet",
        "ideb.parquet" : "C:\\Users\\caio\\Data Analytics\\Pandaspy\\dados\\amostra\\aquisicao\\ideb.parquet",
        "turma.parquet" : "C:\\Users\\caio\\Data Analytics\\Pandaspy\\dados\\amostra\\aquisicao\\turma.parquet"
    }, 
    "completo" : {
        "escola.parquet" : "C:\\Users\\caio\\Data Analytics\\Pandaspy\\dados\\completo\\aquisicao\\escola.parquet",
        "ideb.parquet" : "C:\\Users\\caio\\Data Analytics\\Pandaspy\\dados\\completo\\aquisicao\\ideb.parquet",
        "turma.parquet" : "C:\\Users\\caio\\Data Analytics\\Pandaspy\\dados\\completo\\aquisicao\\turma.parquet"
    }
}

vPATH_DADOS = Path(f"C:\\Users\\caio\\Data Analytics\\Pandaspy\\dados\\{TIPO_DADOS}")

def carrega_parent(nome: str, pasta: str, **kwargs) -> pd.DataFrame:
    return pd.read_parquet(vPATH_DADOS / f"{pasta}\\{nome}.parquet", **kwargs)


df1 = carrega_parent("escola", "aquisicao", engine='pyarrow', filters=[("ANO", "=", 2020)])
df2 = carrega_parent("turma", "aquisicao", engine='pyarrow', filters=[("ANO", "=", 2020)])
df3 = carrega_parent("ideb", "aquisicao", engine='pyarrow')

print(df1)

print(pd.read_csv("C:\\Users\\caio\\Data Analytics\\Pandaspy\\gestor.CSV",sep="|", encoding="latin-1", decimal="."))


with zipfile.ZipFile("C:\\Users\\caio\\Data Analytics\\Pandaspy\\gestor.zip") as zfile:
    df = pd.read_csv(zfile.open("gestor.CSV"), sep="|", encoding="latin-1", decimal=".")
    print(df)

reposta = requests.get("https://drive.google.com/uc?id=1ZyawTjY0fbiCwk6fsF0urF5YfNxP6Gjc&export-download")
Buffer = BytesIO(initial_bytes=reposta.content)
with zipfile.ZipFile(Buffer) as zfile:
    df = pd.read_csv(zfile.open("gestor.CSV"), sep="|", encoding="latin-1", decimal=".")
    print(df)


print(pd.DataFrame(
    data=np.random.randint(low=0, high=10, size=(5,5)),
    columns=[f"coluns{i}" for i in range(5)],
    index=range(5)
))

exam_data = {
    "nome": ["João", "Maria", "Pedro", "Ana", "Luiz"],
    "nota": [10, np.nan, 4, np.nan, 8],
    "tentativas": [1, 2, 3, 5, 8],
    "qualidade": ["yes", "no", "yes", "no", "yes"]
}
labels = list("abcde")
print(pd.DataFrame(data=exam_data, index=labels))