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

print(df1[["QT_COMP_PORTATIL_ALUNO", "QT_DESKTOP_ALUNO"]].cumsum())
print(df1[["QT_COMP_PORTATIL_ALUNO", "QT_DESKTOP_ALUNO"]].diff())
print(df1[["QT_COMP_PORTATIL_ALUNO", "QT_DESKTOP_ALUNO"]].mean())
print(df1[["QT_COMP_PORTATIL_ALUNO", "QT_DESKTOP_ALUNO"]].sum(axis=1))
print(df1[["QT_COMP_PORTATIL_ALUNO", "QT_DESKTOP_ALUNO"]].sum(axis="columns"))

print(df1.sort_values(by=["QT_COMP_PORTATIL_ALUNO", "QT_DESKTOP_ALUNO"], ascending=[True, False])[["QT_COMP_PORTATIL_ALUNO", "QT_DESKTOP_ALUNO"]])

print(df1[["QT_COMP_PORTATIL_ALUNO", "QT_DESKTOP_ALUNO"]].replace({0: "!"}))