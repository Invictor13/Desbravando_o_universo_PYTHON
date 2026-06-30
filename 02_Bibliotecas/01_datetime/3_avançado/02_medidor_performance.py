"""
DESAFIO 08: Analisador de Performance de Código

Nível: Avançado (Bibliotecas - Datetime)
Objetivo: Utilizar timestamps de alta precisão para medir o tempo de execução de blocos de código.
Conceitos: Marcação de tempo antes e depois, manipulação de .microseconds, cálculos de performance.

Enunciado:
    Vamos medir o quão rápido o Python é.
    Crie uma variável com a hora exata antes de executar um laço 'for' que vá de 1 até 1.000.000.
    Assim que o laço terminar, crie outra variável com a hora exata. 
    Subtraia as duas e exiba quantos segundos e microsegundos o Python levou para fazer a contagem.

Exemplo de Execução:
    --------------------------------------------------------
    > Processando 1 milhão de iterações...
    > Processo finalizado!
    > Tempo de execução: 0 segundos e 34512 microsegundos.
    --------------------------------------------------------
"""

# Desenvolva o seu código abaixo:
from datetime import datetime

print("-" * 56)
print("> Processando 1 milhão de iterações...")

inicio = datetime.now()

# Código pesado
for i in range(1000000):
    pass

fim = datetime.now()
tempo_execucao = fim - inicio

print("> Processo finalizado!")
print(f"> Tempo de execução: {tempo_execucao.seconds} segundos e {tempo_execucao.microseconds} microsegundos.")
print("-" * 56)