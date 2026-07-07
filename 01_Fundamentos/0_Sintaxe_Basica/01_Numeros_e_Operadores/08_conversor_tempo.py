"""
Exercicio 08: Desestruturador de Tempo (Segundos para Horas)

    1) Objetivo: Utilizar múltiplos operadores de divisão inteira (//) e resto (%) para converter 
    unidades de tempo.
    2) Conceitos: Operadores aritméticos, divisões sucessivas e formatação de saídas numéricas.

Enunciado:
    - Faça um programa que leia um valor inteiro em segundos digitado pelo usuário. 
    - O script deve calcular e converter esse valor bruto no formato tradicional de relógio: 
                      Horas, Minutos e Segundos restantes.

Exemplo de Execução:
------------------------------------------------------------
    Digite a quantidade de segundos: 3665
------------------------------------------------------------
    Conversão de Tempo:
    > 3665 segundos equivalem a exatamente:
    > 1 hora(s), 1 minuto(s) e 5 segundo(s).
------------------------------------------------------------
"""

print("""
             ------ Conversor de Segundos para Tempo -------
Este script transformará segundos brutos em horas, minutos e segundos
--------------------------------------------------------""", end="\n")

tempo_segundos = int(input("Digite a quantidade de segundos: "))

# Aplicação da lógica de divisões sucessivas:
horas = tempo_segundos // 3600
segundos_restantes = tempo_segundos % 3600

minutos = segundos_restantes // 60
segundos_finais = segundos_restantes % 60

print(f"""--------------------------------------------------------
Conversão de Tempo:
{tempo_segundos} segundos equivalem a exatamente:
> {horas} hora(s), {minutos} minuto(s) e {segundos_finais} segundo(s).
--------------------------------------------------------""")
