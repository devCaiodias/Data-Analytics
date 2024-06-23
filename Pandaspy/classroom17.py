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

# print(df1["QT_SALAS_UTILIZADAS_ACESSIVEIS"] / df1["QT_SALAS_UTILIZADAS"])
# print(df1["PCT_SALAS_ACESSIVEIS"])
df1["PCT_SALAS_ACESSIVEIS"] = df1["QT_SALAS_UTILIZADAS_ACESSIVEIS"] / df1["QT_SALAS_UTILIZADAS"]

df1["PCT_SALAS_ACESSIVEIS"] = 1
pattern = np.tile([1, 2, 3], int(np.ceil(df1.shape[0] / 3)))
df1["PCT_SALAS_ACESSIVEIS"] = pattern[:df1.shape[0]]
# print(df1["PCT_SALAS_ACESSIVEIS"])
df1["PCT_SALAS_ACESSIVEIS"] = df1["QT_SALAS_UTILIZADAS_ACESSIVEIS"] / df1["QT_SALAS_UTILIZADAS"].values
# print(df1["PCT_SALAS_ACESSIVEIS"])

v = df1.loc[:10]
# print(v["PCT_SALAS_ACESSIVEIS"])
v["PCT_SALAS_ACESSIVEIS"] = -1
# print(v["PCT_SALAS_ACESSIVEIS"])
v = df1.loc[:10, "PCT_SALAS_ACESSIVEIS"]
# print(v)

v1 = df1.loc[lambda f: f["QT_SALAS_UTILIZADAS"] == 1, "PCT_SALAS_ACESSIVEIS"] = -1
# print(v1)
v1 = df1.loc[lambda f: f["QT_SALAS_UTILIZADAS"] == 1, "PCT_SALAS_ACESSIVEIS"]
# print(v1)

df4 = df1.assign(
    PCT_SALAS_ACESSIVEIS = lambda f: np.where(
        f["QT_SALAS_UTILIZADAS"] == 1,
        -1,
        (f["QT_SALAS_UTILIZADAS_ACESSIVEIS"] / f["QT_SALAS_UTILIZADAS"])
    )
)

# print(id(df4))
# print(id(df1))


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


# print(pd.concat([df1["ID_ESCOLA"], df1["PCT_SALAS_ACESSIVEIS"]], axis="columns"))
# print(pd.concat([df1[["ID_ESCOLA", "CO_MUNICIPIO"]], df1["PCT_SALAS_ACESSIVEIS"]], axis="columns"))
# print(pd.concat([df1[["ID_ESCOLA", "CO_MUNICIPIO"]], df1[["QT_SALAS_UTILIZADAS","PCT_SALAS_ACESSIVEIS"]]], axis="columns"))
# print(pd.concat([df1["ID_ESCOLA"], df1["CO_MUNICIPIO"], df1["PCT_SALAS_ACESSIVEIS"]], axis="columns"))
# print(pd.concat([df1["ID_ESCOLA"], df1["CO_MUNICIPIO"], df1["PCT_SALAS_ACESSIVEIS"]], axis="rows"))
# print(pd.concat([df1[["ID_ESCOLA", "CO_MUNICIPIO"]], df1[["QT_SALAS_UTILIZADAS","PCT_SALAS_ACESSIVEIS"]]], axis="rows"))


print(df1[["ID_ESCOLA", "CO_MUNICIPIO"]].rename(columns={"CO_MUNICIPIO": "CO"}))
print(df1[["ID_ESCOLA", "CO_MUNICIPIO"]].rename(index={4: "CO"}))