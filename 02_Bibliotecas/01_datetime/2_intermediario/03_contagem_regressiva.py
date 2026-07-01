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

from datetime import datetime, timedelta

l="-"*60
l_t="-"*20

agora = datetime.now()
fim_de_ano = datetime(agora.year,12,31)
diferenca = fim_de_ano - agora

print(f"""
{l_t} Contagem Regressiva - Fim Do Ano {l_t}

[1] Utilizamos uma variável 'agora' para armazenar a data/hora atual.
[2] Em seguida, criamos uma variável 'fim_de_ano', para coletar o ultimo dia do ano.
[3] Realziamos uma subtração entre as duas variáveis criadas.

Data Atual: {agora.strftime("%d/%m/%Y")}
Final do Ano: {fim_de_ano.strftime("%d/%m/%Y")}

{l_t} Saída {l_t}

Faltam exatamente {diferenca.days} dias para o fim de {agora.year}

{l}""")

