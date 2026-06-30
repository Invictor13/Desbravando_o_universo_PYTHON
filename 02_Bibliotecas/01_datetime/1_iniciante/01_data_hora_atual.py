"""
DESAFIO 01: Relógio do Sistema

Nível: Iniciante (Bibliotecas - Datetime)
Objetivo: Importar a biblioteca e acessar a data e hora atuais do sistema.
Conceitos: Importação de módulos, datetime.now(), extração de atributos (dia, mês, ano).

Enunciado:
    Crie um script que importe o módulo datetime. Obtenha a data e a hora exatas 
    do momento da execução e exiba na tela o dia, mês e ano em linhas separadas, 
    seguidos da hora e minuto atuais.

Exemplo de Execução:
    --------------------------------------------------------
    > Dia atual: 2
    > Mês atual: 2
    > Ano atual: 2026
    > Horário: 15:30
    --------------------------------------------------------
"""
# Desenvolva o seu código abaixo:

from datetime import date, datetime
agora = datetime.now()

l = "-"*60
l_t = "-"*20

print(f"""
{l_t} Armazenando a Data {l_t}
Dia Atual: {agora.day}
Mês Atual: {agora.month}
Ano Atual: {agora.year}
{l_t} Armazenando as Horas {l_t}
Horário atual: {agora.hour}:{agora.minute}:{agora.second}
{l}""")




