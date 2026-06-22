"""
DESAFIO 04: Simulador de Investimento (Juros Compostos)

Nível: Avançado (Sintaxe Básica)
Objetivo: Aplicar a precedência de operadores aritméticos em fórmulas financeiras complexas.
Conceitos: Potenciação (**), precedência de operadores, entrada de dados (float/int) e formatação monetária.

Enunciado:
    Crie um script que calcule o valor final de um investimento usando a fórmula dos juros compostos:
    M = P * (1 + i) ** t
    Onde:
    - M é o montante final.
    - P é o capital inicial (float fornecido pelo usuário).
    - i é a taxa de juros mensal (o usuário digita como porcentagem, ex: 1.5 para 1.5%. Você deve dividir por 100).
    - t é o tempo em meses (int fornecido pelo usuário).
    O programa deve calcular o montante final e exibir o valor total acumulado e o total de juros rendidos.

Exemplo de Execução:
    Capital Inicial (R$): 1000.00
    Taxa de Juros Mensal (%): 2.0
    Tempo de Investimento (meses): 12
    --------------------------------------------------------
    Resultado da Simulação:
    > Valor Total Acumulado: R$ 1268.24
    > Total de Juros Rendidos: R$ 268.24
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Simulador de Juros Compostos -------
Este script calculará o rendimento de um capital no regime de juros compostos
--------------------------------------------------------""", end="\n")


p = float(input("Favor informar o valor investido: "))
i = float(input("Favor informar a taxa de juros (ex: 1.5): "))
t = int(input("Tempo de Investimento (Meses): "))

m = p * (1 + (i/100)) ** t

print(f"""
---------- Extrato do Investimento -------------
Capital Inicial (R$): {p}
Taxa de Juros Mensal (%): {i}
Tempo de Investimento (meses): {t}
-----------Resultado da Simulação-----------------
> Valor Total Acumulado: R$ {m:.2f}
> Total de Juros Rendidos: R$ {m-p:.2f}     
      """)