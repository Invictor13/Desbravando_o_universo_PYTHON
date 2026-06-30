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

hoje = datetime.now()
vencimento = hoje + timedelta(days=7)

print("-" * 56)
print(f"> Data da Compra: {hoje.strftime('%d/%m/%Y')}")
print(f"> O boleto vence no dia: {vencimento.strftime('%d/%m/%Y')}")
print("-" * 56)