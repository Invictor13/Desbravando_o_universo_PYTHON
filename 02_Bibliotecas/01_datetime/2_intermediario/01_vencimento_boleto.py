"""
DESAFIO 04: Calculadora de Vencimento de Boletos

Nível: Intermediário (Bibliotecas - Datetime)
Objetivo: Realizar operações matemáticas com datas para descobrir dias futuros.
Conceitos: Módulo timedelta, soma de tempo, formatação de saída.

Enunciado:
    Um e-commerce gera um boleto no exato momento da compra e dá ao cliente 
    um prazo de 7 dias para pagamento. Crie um script que pegue a data de hoje, 
    adicione 7 dias usando a classe 'timedelta' e exiba a data de vencimento formatada.

Exemplo de Execução:
    --------------------------------------------------------
    > Data da Compra: 02/02/2026
    > O boleto vence no dia: 09/02/2026
    --------------------------------------------------------
"""

# Desenvolva o seu código abaixo:

from datetime import datetime, timedelta

l="-"*60
l_t="-"*25

agora = datetime.now()
vencimento = agora + timedelta(days=7)


print(f"""
{l_t} Calculando Data de Pagemento {l_t}
Neste exercicio, ensinaremos a manipular datas

{l_t} O código armazenará a data atual {l_t}

Data Atual: {agora.strftime('%d/%m/%Y')}

{l_t} Adicionando +7 dias {l_t}

Data de Vencimento: {vencimento.strftime('%d/%m/%Y')}

{l}""")
