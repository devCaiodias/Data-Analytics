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

# print(df1.groupby(["TP_DEPENDENCIA"])["QT_DESKTOP_ALUNO"].mean())

index = list()
values = list()
for tp in df1["TP_DEPENDENCIA"].unique():
    group = df1.loc[lambda f: f["TP_DEPENDENCIA"] == tp]
    agg = np.mean(group["QT_DESKTOP_ALUNO"])
    index.append(tp)
    values.append(agg)

print(pd.Series(index=index, data=values, name="QT_DESKTOP_ALUNO")) 

# Multiplas chaves

print(df1.groupby(["TP_REDE_LOCAL","TP_DEPENDENCIA"])["QT_DESKTOP_ALUNO"].mean())

# Multiplos compos

print(df1.groupby(["TP_REDE_LOCAL","TP_DEPENDENCIA"])[["QT_COMP_PORTATIL_ALUNO","QT_DESKTOP_ALUNO"]].mean())

# Tramformaçoes especificas 

print(df1.groupby(["TP_REDE_LOCAL","TP_DEPENDENCIA"])[["QT_COMP_PORTATIL_ALUNO","QT_DESKTOP_ALUNO"]].apply(lambda x: x.max() - x.min()))

# Aplicar Tramformaçoes especificas por colunas

print(df1.groupby(["TP_REDE_LOCAL","TP_DEPENDENCIA"]).agg({
    "QT_COMP_PORTATIL_ALUNO" : "mean",
    "QT_DESKTOP_ALUNO": lambda x: x.max() - x.min()
}))

# Aplicar multiplas transformações ao mesmo tempo

print(df1.groupby(["TP_REDE_LOCAL","TP_DEPENDENCIA"]).agg({
    "QT_COMP_PORTATIL_ALUNO" : [
        "count", "mean", "std", "min", lambda x: x.quantile(0.25), "median", lambda x: x.quantile(0.75), "max"
        ],
    "QT_DESKTOP_ALUNO": [
        "count", "mean", "std", "min", lambda x: x.quantile(0.25), "median", lambda x: x.quantile(0.75), "max"
        ],
}))

# Aplicar transformações nomeadas

print(df1.groupby(["TP_REDE_LOCAL","TP_DEPENDENCIA"]).agg(
    QT_COMP_PORTATIL_ALUNO_COUNT = pd.NamedAgg("QT_COMP_PORTATIL_ALUNO", "count"),
    QT_COMP_PORTATIL_ALUNO_MEAN = pd.NamedAgg("QT_COMP_PORTATIL_ALUNO", "mean"),
    QT_COMP_PORTATIL_ALUNO_STD = pd.NamedAgg("QT_COMP_PORTATIL_ALUNO", "std"),
    QT_COMP_PORTATIL_ALUNO_MIN = pd.NamedAgg("QT_COMP_PORTATIL_ALUNO", "min"),
    QT_COMP_PORTATIL_ALUNO_Q1 = pd.NamedAgg("QT_COMP_PORTATIL_ALUNO", lambda x: x.quantile(0.25)),
    QT_COMP_PORTATIL_ALUNO_Q2 = pd.NamedAgg("QT_COMP_PORTATIL_ALUNO", "median"),
    QT_COMP_PORTATIL_ALUNO_Q3 = pd.NamedAgg("QT_COMP_PORTATIL_ALUNO", lambda x: x.quantile(0.75)),
    QT_COMP_PORTATIL_ALUNO_MAX = pd.NamedAgg("QT_COMP_PORTATIL_ALUNO", "max"),
))


# Agrupamentos (Pivot Table)

print(df1.pivot_table(
    index=["TP_REDE_LOCAL","TP_DEPENDENCIA"],
    columns=["IN_ALIMENTACAO","IN_EXAME_SELECAO"],
    values=["QT_DESKTOP_ALUNO", "QT_COMP_PORTATIL_ALUNO"],
    # aggfunc={"QT_DESKTOP_ALUNO" :"mean", "QT_COMP_PORTATIL_ALUNO": "median"}
    aggfunc={"QT_DESKTOP_ALUNO" :"mean", "QT_COMP_PORTATIL_ALUNO": lambda x: x.max() - x.min()}
))


