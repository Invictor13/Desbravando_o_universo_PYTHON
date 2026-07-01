"""
DESAFIO 09: Globalização e Fusos Horários (Timezones)

Nível: Avançado (Bibliotecas - Datetime)
Objetivo: Compreender a diferença entre datas 'naive' (ingênuas) e 'aware' (conscientes de fuso).
Conceitos: Biblioteca nativa zoneinfo, objetos timezone, conversão UTC.

Enunciado:
    A partir do Python 3.9, a biblioteca 'zoneinfo' facilita lidar com fusos horários globais.
    Crie um script que obtenha a data/hora atual no fuso horário local de 'America/Sao_Paulo'
    e depois converta esse mesmo momento exato para o fuso de Tóquio ('Asia/Tokyo').
    Exiba as duas horas lado a lado para comparação.

Exemplo de Execução:
    --------------------------------------------------------
    > Relógio Global Sincronizado:
    > Horário em São Paulo (Brasil): 15:30
    > Horário em Tóquio (Japão): 03:30 (do dia seguinte)
    --------------------------------------------------------
"""
from datetime import datetime
from zoneinfo import ZoneInfo

l = "-"*60
l_t = "-"*20

horario_sp = datetime.now(ZoneInfo("America/Sao_Paulo"))
print(f"""{l_t}Horário de São Paulo{l_t}
Horário Atual: {horario_sp.strftime("%H:%M - %d/%m/%Y")}
{l}""")

horario_tokyo = datetime.now(ZoneInfo("Asia/Tokyo"))
print(f"""{l_t}Horário de Tokyo{l_t}
Horário Atual: {horario_tokyo.strftime("%H:%M - %d/%m/%Y")}
{l}""")