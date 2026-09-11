import pandas as pd

def exportar_excel(df: pd.DataFrame, caminho: str, aba="BASE PADRONIZADA"):
    with pd.ExcelWriter(caminho, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name=aba)

def exportar_diagnostico(df: pd.DataFrame, caminho: str):
    with pd.ExcelWriter(caminho, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="MAPEAMENTO")
