import pandas as pd

def comparar_por_cpf(empresa: pd.DataFrame, operadora: pd.DataFrame) -> pd.DataFrame:
    campos = ["NOME", "SEXO", "DATA NASCIMENTO", "PARENTESCO",
              "MATRICULA EMPRESA", "PLANO"]

    emp = empresa.copy()
    op = operadora.copy()
    emp = emp[emp["CPF"].ne("")].drop_duplicates("CPF")
    op = op[op["CPF"].ne("")].drop_duplicates("CPF")

    resultado = emp[["CPF"]].copy()
    resultado["LOCALIZADO OPERADORA"] = resultado["CPF"].isin(op["CPF"])

    op_idx = op.set_index("CPF")

    for campo in campos:
        if campo in emp.columns and campo in op.columns:
            resultado[f"{campo} - STATUS"] = resultado.apply(
                lambda row: (
                    "NAO LOCALIZADO"
                    if not row["LOCALIZADO OPERADORA"]
                    else "OK"
                    if str(emp.loc[emp["CPF"].eq(row["CPF"]), campo].iloc[0]).strip()
                    == str(op_idx.loc[row["CPF"], campo]).strip()
                    else "DIVERGENCIA"
                ),
                axis=1,
            )
    return resultado
