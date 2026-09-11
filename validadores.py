import pandas as pd

def validar_cpf(cpf: str) -> bool:
    if not cpf or len(cpf) != 11 or not cpf.isdigit():
        return False
    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    digito1 = 0 if resto == 10 else resto
    if digito1 != int(cpf[9]):
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    digito2 = 0 if resto == 10 else resto
    return digito2 == int(cpf[10])

def validar_base(df: pd.DataFrame) -> pd.DataFrame:
    resultado = df.copy()
    if "CPF" in resultado.columns:
        resultado["CPF VALIDO"] = resultado["CPF"].map(validar_cpf)
    if "NOME" in resultado.columns:
        resultado["NOME PREENCHIDO"] = resultado["NOME"].ne("")
    if "TIPO" in resultado.columns:
        resultado["TIPO PREENCHIDO"] = resultado["TIPO"].ne("")
    return resultado
