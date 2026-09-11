import json
import re
import unicodedata
import pandas as pd

from .leitor import normalizar_nome_coluna

def remover_acentos(valor: str) -> str:
    texto = unicodedata.normalize("NFKD", str(valor))
    return "".join(c for c in texto if not unicodedata.combining(c))

def normalizar_texto(valor):
    if pd.isna(valor):
        return ""
    return " ".join(str(valor).strip().split())

def normalizar_cabecalhos(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [normalizar_nome_coluna(c) for c in df.columns]
    return df

def carregar_mapeamento(caminho: str) -> dict:
    with open(caminho, encoding="utf-8") as arquivo:
        return json.load(arquivo)

def localizar_coluna(df: pd.DataFrame, alternativas: list[str]):
    colunas = {remover_acentos(c).upper(): c for c in df.columns}
    for alternativa in alternativas:
        chave = remover_acentos(alternativa).upper()
        if chave in colunas:
            return colunas[chave]
    return None

def padronizar_cpf(valor):
    if pd.isna(valor):
        return ""
    return re.sub(r"\D", "", str(valor)).zfill(11)

def padronizar_dataframe(df: pd.DataFrame, modelo: list[str], mapeamento: dict):
    df = normalizar_cabecalhos(df)
    resultado = pd.DataFrame(index=df.index)
    origem = {}

    for destino in modelo:
        alternativas = mapeamento.get(destino, [destino])
        coluna = localizar_coluna(df, alternativas)
        origem[destino] = coluna
        if coluna is None:
            resultado[destino] = ""
        else:
            resultado[destino] = df[coluna].map(normalizar_texto)

    if "CPF" in resultado.columns:
        resultado["CPF"] = resultado["CPF"].map(padronizar_cpf)

    return resultado, origem

def gerar_diagnostico(origem: dict) -> pd.DataFrame:
    return pd.DataFrame([
        {
            "CAMPO PADRAO": campo,
            "COLUNA ENCONTRADA": coluna or "",
            "STATUS": "MAPEADO" if coluna else "NAO LOCALIZADO"
        }
        for campo, coluna in origem.items()
    ])
