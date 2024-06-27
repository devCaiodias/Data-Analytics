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

# 1. LEFT JOIN: Mantem-se a estrutura da tabela "esquerda" e adiciona os dados comuns da tabela "direita" 
# 2. RIGHT JOIN: Mantem-se a estrutura da tabela "direita" e adiciona os dados comuns da tabela "esquerda"
# 3. INNER JOIN: Mantem-se apenas os dados onde há intersecção entre as duas tabelas
# 4. OUTER JOIN: Cria-se uma tabela com os dados das duas tabelas

# print(df1.merge(
#     df3.loc[lambda f: f["ANO"] == 2019, ["ID_ESCOLA", "IDEB_AI"]],
#     left_on=["ID_ESCOLA"],
#     right_on=["ID_ESCOLA"],
#     how="left"
# ))

# print(df1.sample(100).merge(
#     df3.loc[lambda f: f["ANO"] == 2019, ["ID_ESCOLA", "IDEB_AI"]],
#     on=["ID_ESCOLA"],
#     how="left",
#     sort=True
# ))

# print(df1.merge(
#     df3.loc[lambda f: f["ANO"] == 2019, ["ID_ESCOLA", "IDEB_AI"]],
#     on=["ID_ESCOLA"],
#     how="left", 
# ).merge(
#     df3.loc[lambda f: f["ANO"] == 2019, ["ID_ESCOLA", "IDEB_AI"]],
#     on=["ID_ESCOLA"],
#     how="left", 
#     suffixes=("", "_Novo")
# )
# )

# print(
#     df1.merge(
#         df3.loc[lambda f: f["ANO"] == 2019, ["ID_ESCOLA", "IDEB_AI"]],
#         on=["ID_ESCOLA"],
#         how="left",
#         indicator=True
#     )["_merge"].value_counts()
# )

# print(
#     df2.merge(
#         df1.reindex(columns=["ID_ESCOLA", "CO_MUNICIPIO"]),
#         how="left",
#         validate="m:1"
#     )
#     )

# print(
#     df1.reindex(columns=["ID_ESCOLA", "CO_MUNICIPIO"]).merge(
#         df2.reindex(columns=["ID_ESCOLA", "ID_TURMA"]),
#         how="left",
#         validate="1:m"
#     )
#     )


print(df3.reindex(columns=["ID_ESCOLA", "ANO", "IDEB_AI", "IDEB_AF"]))


print((
    df3.reindex(columns=["ID_ESCOLA", "ANO", "IDEB_AI", "IDEB_AF"])
    .rolling(2)
    .mean()
))

print((
    df3.reindex(columns=["ID_ESCOLA", "ANO", "IDEB_AI", "IDEB_AF"])
    .rolling(2, axis=1)
    .mean()
))

print((
    df3.reindex(columns=["ID_ESCOLA", "ANO", "IDEB_AI", "IDEB_AF"])
    .interpolate()
))

print((
    df3.reindex(columns=["ID_ESCOLA", "ANO", "IDEB_AI", "IDEB_AF"])
    .groupby(["ID_ESCOLA"])["IDEB_AI"].apply(
        lambda x: x.interpolate()
    )
))

# print(
#     (
#     df3.reindex(columns=["ID_ESCOLA", "ANO", "IDEB_AI", "IDEB_AF"])
#     .sort_values(by=["ID_ESCOLA", "ANO"])
#     .reset_index(drop=True)
#     .assign(IDEB_AI=lambda f: f.groupby(["ID_ESCOLA"])["IDEB_AI"].apply(lambda x: x.interpolate()))
#     )
#     )

print(
    df3.loc[lambda f: f["ANO"] == 2021].count
)

print(df3.reindex(columns=["ID_ESCOLA", "ANO", "IDEB_AI", "IDEB_META_AI"]))

def gera_novo_df(df: pd.DataFrame) -> pd.DataFrame:
    for m in ["AI", "AF", "EM"]:
        df[f"IDEB_{m}"] - df[f"IDEB_{m}"].interpolate()
    
    if (
        df["IDEB_AI"].count() == 0
        and df["IDEB_AF"].count() == 0
        and df["IDEB_EM"].count() == 0
    ):
        df["TIPO"] = "SEM COLETA DE IDEB"
    elif(
        df["IDEB_AI"].count() > 0
        and df["IDEB_AF"].count() == 0
        and df["IDEB_EM"].count() == 0
    ):
        df["TIPO"] = "ANOS INICIASIS"
    elif(
        df["IDEB_AI"].count() == 0
        and df["IDEB_AF"].count() > 0
        and df["IDEB_EM"].count() == 0
    ):
        df["TIPO"] = "ANOS FINAIS"
    elif(
        df["IDEB_AI"].count() == 0
        and df["IDEB_AF"].count() == 0
        and df["IDEB_EM"].count() > 0
    ):
        df["TIPO"] = "ENCINO MEDIO"
    else : 
        df["TIPO"] = "MULTIPLOS"
        
    return df.reindex(columns=["ID_ESCOLA", "ANO", "IDEB_AI", "IDEB_AF", "IDEB_EM", "TIPO"])
    
print(df3.head(52).groupby(["ID_ESCOLA"]).apply(gera_novo_df))
