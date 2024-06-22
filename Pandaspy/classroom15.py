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

# print(df1[["QT_DESKTOP_ALUNO", "IN_INTERNET"]] > 0)
# print(df1[["QT_DESKTOP_ALUNO", "IN_INTERNET"]].isnull())
# print(df1[["QT_DESKTOP_ALUNO", "IN_INTERNET"]].notnull())
# print(df1[["QT_DESKTOP_ALUNO", "IN_INTERNET"]].isin([0, 1]))

# print(df1[df1["QT_DESKTOP_ALUNO"] > 0])
# print(df1[(df1["QT_DESKTOP_ALUNO"] > 0) | (df1["IN_INTERNET"] > 0)])
# print((df1["QT_DESKTOP_ALUNO"] > 0).all())
# print((df1[["QT_DESKTOP_ALUNO", "IN_INTERNET"]] > 0).all())
# print((df1[["QT_DESKTOP_ALUNO", "IN_INTERNET"]] > 0).all(axis="columns"))
# print((df1[["QT_DESKTOP_ALUNO", "IN_INTERNET"]] > 0).all(axis=1))
# print(df1[(df1[["QT_DESKTOP_ALUNO", "IN_INTERNET"]] > 0).all(axis=1)])
# print(df1.loc[(df1[["QT_DESKTOP_ALUNO", "IN_INTERNET"]] > 0).all(axis=1)])
print(df1.loc[(df1[["QT_DESKTOP_ALUNO", "IN_INTERNET"]] > 0).all(axis=1), ["ID_ESCOLA", "QT_DESKTOP_ALUNO", "IN_INTERNET"]])
print(
    df1.loc[lambda f: (f[["QT_DESKTOP_ALUNO", "IN_INTERNET"]] > 0).all(axis=1), 
    ["ID_ESCOLA", "QT_DESKTOP_ALUNO", "IN_INTERNET"]
])