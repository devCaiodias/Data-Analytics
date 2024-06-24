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

# print(df1[["QT_COMP_PORTATIL_ALUNO", "QT_DESKTOP_ALUNO"]].apply(lambda x: (x - x.min()) / (x.max() - x.min()) ))
# print(df1[["QT_COMP_PORTATIL_ALUNO", "QT_DESKTOP_ALUNO"]].apply(lambda x: print(x.name) ))
# print(df1[["QT_COMP_PORTATIL_ALUNO", "QT_DESKTOP_ALUNO"]].apply(lambda x: x.mean() ))

print(
    (
        df1[["QT_COMP_PORTATIL_ALUNO", "QT_DESKTOP_ALUNO"]]
        .head(3)
    )
)

print(
    (
        df1.head(3)
        .apply(lambda x: x[["QT_COMP_PORTATIL_ALUNO", "QT_DESKTOP_ALUNO"]].max(), axis="columns")
    )
)

print(df1[["QT_COMP_PORTATIL_ALUNO", "QT_DESKTOP_ALUNO"]].applymap(lambda x: len(str(x)), na_action="ignore" ))
print(df1[["QT_COMP_PORTATIL_ALUNO", "QT_DESKTOP_ALUNO"]].transform("sqrt"))
print(df1[["QT_COMP_PORTATIL_ALUNO", "QT_DESKTOP_ALUNO"]].apply(np.sqrt))

print(df1.transform({
    "QT_COMP_PORTATIL_ALUNO": lambda x: (x - x.min()) / (x.max() - x.min()),
    "QT_DESKTOP_ALUNO": "sqrt"
}))

