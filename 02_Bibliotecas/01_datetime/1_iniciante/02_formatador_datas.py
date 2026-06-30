"""
DESAFIO 02: Formatador de Datas Brasileiro

Nível: Iniciante (Bibliotecas - Datetime)
Objetivo: Transformar objetos datetime em strings formatadas para o padrão nacional.
Conceitos: Método strftime(), diretivas de formatação de tempo (%d, %m, %Y, %H, %M).

Enunciado:
    Escreva um programa que capture a data e hora atuais do sistema e a converta 
    para uma string legível no formato tradicional brasileiro: "DD/MM/AAAA às HH:MM".
    Exiba o resultado formatado.

Exemplo de Execução:
    --------------------------------------------------------
    > Data de Acesso: 02/02/2026 às 15:45
    --------------------------------------------------------
"""

# Desenvolva o seu código abaixo:

from datetime import datetime

l="-"*60
l_t="-"*20

print(f"""
{l_t} Simulando a Data de Acesso {l_t}
    [1] Opção 1: Sem formatar
    [2] Opção 2: Padrão Brasileiro""")


agora = datetime.now()
print(f"""
{l_t} Opção 1 {l_t}
Data de Acesso: {agora}""")

agora_formatado = agora.strftime("%d/%m/%Y às %H:%M")
print(f"""
{l_t} Opção 2 {l_t}
Data de Acesso: {agora_formatado}
{l}""")




""""
from datetime import datetime

agora = datetime.now()
data_formatada = agora.strftime("%d/%m/%Y às %H:%M")

print("-" * 56)
print(f"> Data de Acesso: {data_formatada}")
print("-" * 56)
"""