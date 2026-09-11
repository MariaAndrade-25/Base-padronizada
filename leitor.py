import pandas as pd

def ler_excel(caminho: str) -> pd.DataFrame:
    return pd.read_excel(caminho, dtype=str)

def normalizar_nome_coluna(nome: str) -> str:
    return " ".join(str(nome).strip().upper().split())
