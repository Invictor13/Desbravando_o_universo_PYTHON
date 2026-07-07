"""
DESAFIO 15: Analisador de Viabilidade Financeira (Lógica Pura)

Nível: Avançado (Sintaxe Básica)
Objetivo: Consolidar custos fixos, variáveis e receitas para gerar um indicador booleano de viabilidade.
Conceitos: Operações aritméticas, expressões lógicas, atribuição de variáveis e saída True/False.

Enunciado:
    Uma empresa de turismo quer saber se uma viagem fretada trará lucro antes de executá-la.
    Crie um script que receba três dados: Custo Fixo do Ônibus (float), Preço do Ingresso por Pessoa (float) 
    e a Quantidade de Passageiros Confirmados (int).
    O programa deve calcular:
    1. O Custo Total da viagem (sabendo que há uma taxa fixa extra de R$ 15.00 de seguro por passageiro).
    2. A Receita Bruta Total (Quantidade de Passageiros x Preço do Ingresso).
    3. Um indicador booleano chamado 'viagem_lucrativa' que verifica se a Receita é estritamente maior que o Custo Total.
    Exiba o Custo Total, a Receita Bruta e se a viagem é lucrativa (True ou False).

Exemplo de Execução:
    Custo de Fretamento do Ônibus (R$): 1200.00
    Valor do Ingresso por Pessoa (R$): 80.00
    Quantidade de Passageiros: 25
    --------------------------------------------------------
    Relatório Estatístico de Viabilidade:
    > Custo Total do Evento: R$ 1575.00
    > Faturamento Bruto Previsto: R$ 2000.00
    > A viagem trará lucro real? True
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Analisador de Viabilidade de Fretamento -------
Este script calculará o balanço financeiro e retornará o status de lucro
--------------------------------------------------------""", end="\n")

# Entrada dos dados com casting correto
custo_onibus = float(input("Custo de Fretamento do Ônibus (R$): "))
valor_ingresso = float(input("Valor do Ingresso por Pessoa (R$): "))
passageiros = int(input("Quantidade de Passageiros: "))

# 1. Cálculo dos Custos (Taxa fixa de seguro de R$ 15.00 por pessoa)
custo_total = custo_onibus + (passageiros * 15.00)

# 2. Cálculo das Receitas
receita_total = passageiros * valor_ingresso

# 3. Indicador Booleano de Lucro Estrito (Receita > Custo)
viagem_lucrativa = receita_total > custo_total

print("--------------------------------------------------------")
print("Relatório Estatístico de Viabilidade:")
print(f"> Custo Total do Evento: R$ {custo_total:.2f}")
print(f"> Faturamento Bruto Previsto: R$ {receita_total:.2f}")
print(f"> A viagem trará lucro real? {viagem_lucrativa}")
print("--------------------------------------------------------")