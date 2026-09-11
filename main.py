import argparse
import json
from pathlib import Path

from .leitor import ler_excel
from .padronizador import carregar_mapeamento, padronizar_dataframe, gerar_diagnostico
from .validadores import validar_base
from .exportador import exportar_excel, exportar_diagnostico

BASE = Path(__file__).resolve().parent.parent
MODELO = BASE / "config" / "modelo_padrao.json"
MAPEAMENTO = BASE / "config" / "mapeamento_colunas.json"

def main():
    parser = argparse.ArgumentParser(description="Padronizador de bases de beneficiarios.")
    parser.add_argument("--input", required=True, help="Caminho do Excel de entrada.")
    parser.add_argument("--output", default="saida/BASE_PADRONIZADA.xlsx")
    args = parser.parse_args()

    with open(MODELO, encoding="utf-8") as arquivo:
        modelo = json.load(arquivo)["colunas"]

    df = ler_excel(args.input)
    mapeamento = carregar_mapeamento(MAPEAMENTO)
    padronizada, origem = padronizar_dataframe(df, modelo, mapeamento)
    padronizada = validar_base(padronizada)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    exportar_excel(padronizada, str(output))
    exportar_diagnostico(gerar_diagnostico(origem),
                         str(output.with_name("DIAGNOSTICO_MAPEAMENTO.xlsx")))

    print(f"Base processada: {output}")
    print(f"Linhas processadas: {len(padronizada)}")

if __name__ == "__main__":
    main()
