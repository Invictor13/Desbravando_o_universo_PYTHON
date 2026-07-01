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

l_t = "-"*20
l = "-"*60

print(f"""
{l_t} Tabela dos Dias {l_t}
Acionando a função 'weekday()', receberemos os valores inteiros:
{l}
[0] Segunda-Feira
[1] Terça-Feira
[2] Quarta-Feira
[3] Quinta-Feira
[4] Sexta-Feira
[5] Sábado
[6] Domingo""")

agora = datetime.now()
dias_corridos = agora
contador_uteis = 0  # Usamos um número inteiro no lugar da lista para contar

# Enquanto não atingirmos 5 dias úteis...
while contador_uteis < 5: 
    # 1. Avançamos 1 dia no calendário
    dias_corridos = dias_corridos + timedelta(days=1)
    
    # 2. Verificamos se esse NOVO dia é um dia útil (0 a 4)
    dia_semana = dias_corridos.weekday()
    if dia_semana < 5:
        contador_uteis += 1  # Se for útil, registramos na contagem

print(f"""
{l_t} Calculando {l_t}

[1] Primeiramente utilizamos uma variável 'agora', para pegar a data atual.
[2] A variável 'dias_corridos' percorreu o calendário dia após dia no laço.
[3] A condicional contabilizou apenas os dias úteis (ignorando 5 e 6).
{l}

Dia Atual: {agora.strftime("%d/%m/%Y")}
Pagamento: {dias_corridos.strftime("%d/%m/%Y")}
{l}""")
