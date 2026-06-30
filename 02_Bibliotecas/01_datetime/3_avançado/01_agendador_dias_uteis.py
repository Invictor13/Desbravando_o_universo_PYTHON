"""
DESAFIO 07: Agendador Corporativo (Pulo de Finais de Semana)

Nível: Avançado (Bibliotecas - Datetime)
Objetivo: Iterar e validar datas utilizando lógicas de calendário.
Conceitos: Método weekday(), laços de repetição com datas, timedelta condicional.

Enunciado:
    Um sistema precisa agendar uma entrega para exatamente 5 dias úteis a partir de hoje 
    (ignorando sábados e domingos). Crie um script que adicione 1 dia de cada vez a partir 
    da data atual. Se o dia cair no fim de semana (weekday() == 5 ou 6), não conte como dia útil.
    Exiba a data final da entrega.

Exemplo de Execução:
    --------------------------------------------------------
    > Calculando prazo de 5 dias úteis...
    > A entrega será realizada no dia: 09/02/2026 (Segunda-feira)
    --------------------------------------------------------
"""

# Desenvolva o seu código abaixo:
from datetime import datetime, timedelta

data_atual = datetime.now()
dias_uteis_adicionados = 0

while dias_uteis_adicionados < 5:
    data_atual += timedelta(days=1)
    # 0 = Segunda, 1 = Terça... 5 = Sábado, 6 = Domingo
    if data_atual.weekday() < 5: 
        dias_uteis_adicionados += 1

print("-" * 56)
print("> Calculando prazo de 5 dias úteis...")
print(f"> A entrega será realizada no dia: {data_atual.strftime('%d/%m/%Y')}")
print("-" * 56)