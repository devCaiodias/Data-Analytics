import pandas as pd
import numpy as np
import pyarrow
from pathlib import Path

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

exportar = df3.reindex(columns=["ID_ESCOLA", "ANO", "IDEB_AI"]).dropna()
print(exportar)

exportar.to_csv("C:\\Users\\caio\\Data Analytics\\Pandaspy\\dados\\dados.csv", index=False)
print(exportar)

# CSV

# exportar.to_csv("dados.csv", sep=",", decimal=",", encoding="utf-8")

# exportar.to_csv("dados.zip", compression="zip")

# # EXCEL

# exportar.to_excel("dados.xlsx", sheet_name="IDEB_AI", index=False)

# with pd.ExcelWriter("dados.xlsx") as write:
#     exportar.to_excel(write, sheet_name="IDEB_AI", index=False)

# # PICKLE

# exportar.to_pickle("dados.pkl")

# # PARQUET

# exportar.to_parquet("dado.parquet",  partition_cols=["ANO"])


