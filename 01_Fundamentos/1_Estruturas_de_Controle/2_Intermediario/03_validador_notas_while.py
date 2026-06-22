"""
DESAFIO 03: Coletor Acadêmico com Validação de Entrada

Nível: Intermediário (Estruturas de Controle)
Objetivo: Validar se os dados inseridos pelo usuário são aceitáveis antes de processá-los no loop.
Conceitos: Laço while, acumuladores (soma += valor), contadores (total += 1), condicionais aninhadas.

Enunciado:
    Crie um script para calcular a média de notas de um aluno, mas com validação de segurança.
    O programa deve pedir as notas uma por uma dentro de um loop.
    - Se o usuário digitar uma nota válida (entre 0.0 e 10.0), o sistema acumula a nota e conta o aluno.
    - Se digitar uma nota inválida, o sistema deve exibir "Nota inválida! Digite um valor entre 0 e 10." e NÃO contar essa nota.
    O loop só deve parar quando o usuário digitar um número negativo (ex: -1). No final, mostre a média calculada.

Exemplo de Execução:
    Digite uma nota (ou um número negativo para parar): 8.5
    Digite uma nota (ou um número negativo para parar): 12.0
    > Nota inválida! Digite um valor entre 0 e 10.
    Digite uma nota (ou um número negativo para parar): 7.5
    Digite uma nota (ou um número negativo para parar): -1
    --------------------------------------------------------
    Análise Finalizada:
    > Total de notas válidas processadas: 2
    > Média Final do Aluno: 8.00
    --------------------------------------------------------
"""

# Desenvolva o seu código abaixo: