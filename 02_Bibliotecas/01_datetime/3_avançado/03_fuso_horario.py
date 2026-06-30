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

# Desenvolva o seu código abaixo:
from datetime import datetime
from zoneinfo import ZoneInfo

# Pega o momento exato e atrela ao fuso horário brasileiro
hora_sp = datetime.now(ZoneInfo("America/Sao_Paulo"))

# Converte o mesmo momento para o fuso do Japão
hora_tokyo = hora_sp.astimezone(ZoneInfo("Asia/Tokyo"))

print("-" * 56)
print("> Relógio Global Sincronizado:")
print(f"> Horário em São Paulo (Brasil): {hora_sp.strftime('%H:%M - %d/%m/%Y')}")
print(f"> Horário em Tóquio (Japão): {hora_tokyo.strftime('%H:%M - %d/%m/%Y')}")
print("-" * 56)