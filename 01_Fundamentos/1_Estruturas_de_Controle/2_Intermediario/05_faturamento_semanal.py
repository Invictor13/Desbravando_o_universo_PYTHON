"""
DESAFIO 05: Analisador de Faturamento Semanal

Nível: Intermediário (Estruturas de Controle)
Objetivo: Alimentar uma lista dinamicamente através de iterações e realizar cálculos estatísticos básicos sobre ela.
Conceitos: Laço for com range(1, 8), inputs dinâmicos, funções matemáticas de listas (sum, len), condicional para filtros.

Enunciado:
    Escreva um programa que auxilie uma loja a analisar o seu faturamento diário durante uma semana completa (7 dias).
    Utilizando o laço 'for' e a função 'range()', peça para o usuário digitar o faturamento de cada dia (Dia 1, Dia 2, ... Dia 7) 
    e guarde esses valores dentro de uma lista chamada 'faturamentos'.
    Após coletar todos os dados, o programa deve calcular e exibir:
    1. O faturamento total da semana.
    2. A média diária de faturamento.
    3. Quantos dias da semana tiveram o faturamento estritamente ACIMA da média calculada.

Exemplo de Execução:
    Digite o faturamento do Dia 1 (R$): 1000.00
    Digite o faturamento do Dia 2 (R$): 1500.00
    ... [até o Dia 7]
    --------------------------------------------------------
    Relatório de Desempenho Comercial:
    > Faturamento Total da Semana: R$ 8400.00
    > Média Diária de Vendas: R$ 1200.00
    > Dias com vendas acima da média: 3 dias.
    --------------------------------------------------------
"""

# Desenvolva o seu código abaixo:

faturamento_semanal = [0,0,0,0]
entrada_diaria=[]
dias_acima_media =[]

print("--------- Faturamento Mensal -----------")
for i in range (1,29):
    n = float(input(f"Digite o faturamento do Dia {i} (R$): "))
    entrada_diaria.append(n)

    if (i>=1) and (i<=7):
        faturamento_semanal[0] = faturamento_semanal[0] + n
    elif (i>=8) and (i<=14):
        faturamento_semanal[1] = faturamento_semanal[1] + n
    elif (i>=15) and (i<=21):
        faturamento_semanal[2] = faturamento_semanal[2] + n
    elif (i>=22) and (i<=29):
        faturamento_semanal[3] = faturamento_semanal[3] + n

faturamento_mensal = sum(faturamento_semanal)
media_entrada = faturamento_mensal/28

print(faturamento_mensal)
print(media_entrada)

for valor in entrada_diaria:
    if (valor > media_entrada):
        dias_acima_media.append(valor)
        valor += 1
print(dias_acima_media)
