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

# print(df1["ID_ESCOLA"])
# print(df1[["ID_ESCOLA","CO_MUNICIPIO"]])
# print(df1[["ID_ESCOLA"]])

# print(df1.iloc[[1,2,3]])
# print(df1.iloc[:5])
# print(df1.iloc[0])
# print(df1.iloc[[0]])
# print(df1.iloc[:, [2,3]])
# print(df1.iloc[1:4, :4])

print(df1.loc[1:4, ["ID_ESCOLA", "CO_MUNICIPIO", "TP_DEPENDENCIA", "TP_CATEGORIA_ESCOLA_PRIVADA"]])
print(df1.loc[:, "ID_ESCOLA": "DT_ANO_LETIVO_TERMINO": 2])

print(df1.reindex(index=[0, 1, 2, "N existe"]))