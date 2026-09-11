# Base Unificadora

Projeto em Python para **padronizar bases de beneficiários**, validar dados e, em uma segunda etapa, comparar bases de empresa e operadora para encontrar divergências.

## Objetivo

Receber planilhas com estruturas diferentes e transformar os dados em um **modelo único**, facilitando:

- padronização de colunas;
- normalização de CPF, nomes, datas e outros campos;
- validação de dados;
- identificação de campos não localizados;
- comparação Empresa × Operadora;
- geração de relatório de divergências.

## Arquitetura

```text
Excel de entrada
      |
      v
  leitor.py
      |
      v
padronizador.py
      |
      +----> modelo_padrao.json
      |
      +----> mapeamento_colunas.json
      |
      v
 validadores.py
      |
      v
  Excel padrão
      |
      v
  comparador.py
      |
      v
relatório de divergências
```

## Estrutura

```text
base-unificadora/
├── app/
│   ├── main.py
│   ├── leitor.py
│   ├── padronizador.py
│   ├── validadores.py
│   ├── comparador.py
│   └── exportador.py
├── config/
│   ├── modelo_padrao.json
│   └── mapeamento_colunas.json
├── entrada/
├── saida/
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```

## Instalação

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Depois:

```bash
pip install -r requirements.txt
```

## Primeiro uso

Coloque uma planilha em `entrada/` e execute:

```bash
python -m app.main --input entrada/minha_base.xlsx
```

O programa gera:

```text
saida/
├── BASE_PADRONIZADA.xlsx
└── DIAGNOSTICO_MAPEAMENTO.xlsx
```

## Próximas versões

### V0.1
- leitura de Excel;
- mapeamento de colunas;
- modelo padrão;
- normalização básica;
- validação de CPF;
- diagnóstico de campos.

### V0.2
- comparação Empresa × Operadora;
- divergência de CPF;
- divergência de matrícula;
- divergência de nome;
- não localizados;
- duplicidades.

### V0.3
- comparação inteligente de nomes;
- score de similaridade;
- regras configuráveis;
- relatório executivo.

### V1.0
- interface web;
- upload de arquivos;
- dashboard;
- histórico de processamentos;
- API.

## Segurança

**Não coloque bases reais de beneficiários no GitHub.**

Dados de produção devem ficar fora do repositório. O `.gitignore` já bloqueia arquivos Excel nas pastas `entrada/` e `saida/`.

## Tecnologias

- Python
- Pandas
- OpenPyXL
- Pytest

## Status

Em desenvolvimento.
