"""
DESAFIO 05: Conversor de Strings para Datas

Nível: Intermediário (Bibliotecas - Datetime)
Objetivo: Extrair dados temporais de textos comuns digitados por usuários.
Conceitos: Método strptime(), conversão de string para datetime, extração de ano.

Enunciado:
    Crie um programa que solicite ao usuário uma data no formato string exato "DD/MM/AAAA".
    Use o método 'strptime' para converter essa string de texto em um objeto datetime real.
    Em seguida, extraia e mostre apenas o ano digitado para provar a conversão.

Exemplo de Execução:
    Digite uma data (DD/MM/AAAA): 25/12/2026
    --------------------------------------------------------
    > Conversão bem-sucedida!
    > O ano informado no texto foi: 2026
    --------------------------------------------------------
"""

# Desenvolva o seu código abaixo:
from datetime import datetime

texto_data = input("Digite uma data (DD/MM/AAAA): ")

try:
    data_convertida = datetime.strptime(texto_data, "%d/%m/%Y")
    print("-" * 56)
    print("> Conversão bem-sucedida!")
    print(f"> O ano informado no texto foi: {data_convertida.year}")
    print("-" * 56)
except ValueError:
    print("> Formato inválido! Tente novamente respeitando o padrão DD/MM/AAAA.")