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

from datetime import datetime, timedelta

l="-"*60
l_t="-"*20
print(f"""
{l_t} Instruções {l_t}     
> Para testarmos a velocidade da linguagem Python...
> Construiremos laços de repetição para testar o tempo de processamento
{l}""")

print(f"""
{l_t} Primeiro Cronometro: 1.000.000 repetições {l_t}
> Processando...""")

inicio = datetime.now()
for i in range(0,1000000):
    pass
final = datetime.now()

tempo_decorrido = final - inicio

print(f"""> Processo Finalizado!
           
Tempo de Excução {tempo_decorrido.seconds} segundos e {tempo_decorrido.microseconds} milisegundos 
{l}""")

print(f"""
{l_t} Segundo Cronometro: 10.000.000.000 repetições {l_t}
> Processando...""")

inicio = datetime.now()
for i in range(0,10000000):
    pass
final = datetime.now()

tempo_decorrido = final - inicio

print(f"""> Processo Finalizado!
           
Tempo de Excução {tempo_decorrido.seconds} segundos e {tempo_decorrido.microseconds} milisegundos 
{l}""")
