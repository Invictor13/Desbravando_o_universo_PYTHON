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