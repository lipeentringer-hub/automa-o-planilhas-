# Automação de Limpeza e Consolidação de Dados (RPA)

Script em Python desenvolvido para automatizar o tratamento de planilhas e arquivos CSV corporativos, eliminando o trabalho manual de higienização de dados.

## O que ele faz:
- Lê arquivos CSV brutos e desorganizados.
- Detecta campos nulos, vazios ou inválidos (`N/A`).
- Substitui automaticamente por tags de revisão (`PENDENTE_REVISAO`).
- Gera um relatório final limpo, auditado e pronto para a diretoria.

## Como rodar:
```bash
python automacao_planilhas.py