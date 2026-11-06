# language: Python, file: automacao_planilhas.py, target: Windows/Linux, Python 3.8+
# *Consolidates raw messy CSV logs, cleans missing fields, standardizes formats, and outputs a clean audit report*
import os
import csv
from datetime import datetime

def process_raw_data(input_file, output_file):
    print(f"[*] Lendo dados brutos de: {input_file}...")
    
    cleaned_rows = []
    total_processed = 0
    errors_fixed = 0

    try:
        with open(input_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            
            if not fieldnames:
                print("[-] Erro: O arquivo está vazio ou sem cabeçalho válido.")
                return False

            for row in reader:
                total_processed += 1
                
                # Validação e limpeza de dados nulos/vazios
                cleaned_row = {}
                row_has_error = False
                
                for key, value in row.items():
                    if value is None or value.strip() == "" or value.strip().lower() == "n/a":
                        cleaned_row[key] = "PENDENTE_REVISAO"
                        row_has_error = True
                    else:
                        # Padroniza strings removendo espaços extras
                        cleaned_row[key] = value.strip()
                
                if row_has_error:
                    errors_fixed += 1
                    
                cleaned_rows.append(cleaned_row)

        # Escreve o resultado tratado no arquivo de saída
        with open(output_file, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(cleaned_rows)

        print(f"[+] Sucesso! Total lido: {total_processed} registros.")
        print(f"[+] Linhas com campos ajustados/corrigidos: {errors_fixed}")
        print(f"[+] Relatório limpo salvo com sucesso em: {output_file}")
        return True

    except FileNotFoundError:
        print(f"[-] Erro: O arquivo '{input_file}' não foi encontrado no diretório.")
        return False
    except Exception as e:
        print(f"[-] Erro inesperado durante o processamento: {e}")
        return False

if __name__ == "__main__":
    # Teste local simulado
    input_sample = "dados_brutos.csv"
    output_sample = "relatorio_consolidado.csv"
    
    # Cria um arquivo CSV de exemplo se ele não existir para teste imediato
    if not os.path.exists(input_sample):
        with open(input_sample, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Cliente", "Valor", "Status"])
            writer.writerow(["101", "Empresa A", "1500.00", "Ativo"])
            writer.writerow(["102", "Empresa B", "", "Pendente"])  # Dado ausente simulado
            writer.writerow(["103", "Empresa C", "3200.50", "N/A"])    # Dado inválido simulado
        print(f"[*] Arquivo de demonstração '{input_sample}' gerado para teste.")

    print(f"--- Iniciando Script de Automação [{datetime.now().strftime('%H:%M:%S')}] ---")
    process_raw_data(input_sample, output_sample)