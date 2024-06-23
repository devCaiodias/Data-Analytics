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

df1["PCT_SALAS_ACESSIVEIS"] = df1["QT_SALAS_UTILIZADAS_ACESSIVEIS"] / df1["QT_SALAS_UTILIZADAS"]
df1["PCT_SALAS_ACESSIVEIS"] = 1
pattern = np.tile([1, 2, 3], int(np.ceil(df1.shape[0] / 3)))
df1["PCT_SALAS_ACESSIVEIS"] = pattern[:df1.shape[0]]
# print(df1["PCT_SALAS_ACESSIVEIS"])

df4 = df1.assign(
    PCT_SALAS_ACESSIVEIS = lambda f: np.where(
        f["QT_SALAS_UTILIZADAS"] == 1,
        -1,
        (f["QT_SALAS_UTILIZADAS_ACESSIVEIS"] / f["QT_SALAS_UTILIZADAS"])
    )
)

for l in range(1, 6):
    df4 = df4.assign( 
        **{
            f"PCT_SALAS_ACESSIVEIS_{l}": lambda f: np.where(
                f["QT_SALAS_UTILIZADAS"] == 1,
                -1,
                (f["QT_SALAS_UTILIZADAS_ACESSIVEIS"] / f["QT_SALAS_UTILIZADAS"])
        )}
    )

# print(df4.columns)

# print(df1.drop(index=[1,2,3]))

df4.drop(
    columns=[
        "PCT_SALAS_ACESSIVEIS_1",
        "PCT_SALAS_ACESSIVEIS_2",
        "PCT_SALAS_ACESSIVEIS_3",
        "PCT_SALAS_ACESSIVEIS_4",
        "PCT_SALAS_ACESSIVEIS_5",
    ],
    inplace=True
    )
# print(df4.columns)

# print(df4.drop("PCT_SALAS_ACESSIVEIa", axis=1, errors="ignore"))

print(df4.shape)
print(df4.drop_duplicates())
print(df4.drop_duplicates(subset=["CO_MUNICIPIO", "CO_ESCOLA_SEDE_VINCULADA"]))
print(df4.drop_duplicates(subset=["CO_MUNICIPIO"], keep="last")) # inplace = True se quiser modificar real mesmo

print(df1.dropna())
print(df1.dropna(axis="columns"))
print(df1.dropna(axis="columns", how="all"))
print(df1.dropna(axis="rows", how="any", subset=["CO_ESCOLA_SEDE_VINCULADA"]))

