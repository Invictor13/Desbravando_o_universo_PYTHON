"""
DESAFIO 07: Sistema Crítico de Aprovação (Lógica Booleana Pura)

Nível: Avançado (Sintaxe Básica)
Objetivo: Combinar cálculos matemáticos de médias ponderadas com operadores de comparação e lógicos.
Conceitos: Média ponderada, operadores de comparação (>=), operadores lógicos (and, or) e saída booleana.

Enunciado:
    Desenvolva um validador de aprovação de uma faculdade. O script deve solicitar: Nota da Prova (float), 
    Nota do Trabalho (float) e a Frequência do aluno em porcentagem (int, ex: 80 para 80%).
    Regras do sistema:
    1. Calcule a Média Ponderada: a Prova tem peso 7 e o Trabalho tem peso 3.
    2. Para o aluno ser aprovado diretamente (retornar True), ele precisa:
       Ter uma Média Ponderada maior ou igual a 7.0 AND uma Frequência maior ou igual a 75%.
    Exiba na tela a Média Final formatada e o status de aprovação DIRETAMENTE como True ou False.

Exemplo de Execução:
    Digite a nota da Prova: 6.5
    Digite a nota do Trabalho: 9.0
    Digite a Frequência (%): 80
    --------------------------------------------------------
    Análise de Desempenho Acadêmico:
    > Média Final Calculada: 7.25
    > Aluno Aprovado? True
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Validador Acadêmico Booleano -------
Este script avaliará critérios de nota e presença usando lógica pura
--------------------------------------------------------""", end="\n")