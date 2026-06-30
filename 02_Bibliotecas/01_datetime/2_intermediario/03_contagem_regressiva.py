"""
DESAFIO 06: Contagem Regressiva para o Fim de Ano

Nível: Intermediário (Bibliotecas - Datetime)
Objetivo: Calcular a diferença exata entre duas datas distintas.
Conceitos: Subtração de objetos datetime, extração do atributo .days.

Enunciado:
    Escreva um script que calcule quantos dias faltam para o último dia do ano atual.
    Descubra o ano em que estamos dinamicamente, crie uma data representando o dia 
    31 de dezembro desse mesmo ano, subtraia a data de hoje e exiba a quantidade de dias restantes.

Exemplo de Execução:
    --------------------------------------------------------
    > Status: Faltam 332 dias para acabar o ano!
    --------------------------------------------------------
"""

# Desenvolva o seu código abaixo:
from datetime import datetime

hoje = datetime.now()
fim_de_ano = datetime(hoje.year, 12, 31)

diferenca = fim_de_ano - hoje

print("-" * 56)
print(f"> Status: Faltam {diferenca.days} dias para acabar o ano!")
print("-" * 56)