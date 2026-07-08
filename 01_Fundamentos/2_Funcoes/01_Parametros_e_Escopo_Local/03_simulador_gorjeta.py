"""
DESAFIO 03: Calculadora de Gorjeta de Restaurante

Nível: Iniciante (Funções)
Objetivo: Aplicar parâmetros opcionais (valores padrão) na assinatura de uma função.
Conceitos: Argumentos nomeados, parâmetros com valor padrão (default arguments), cálculo percentual.

Enunciado:
    Crie uma função chamada 'calcular_gorjeta(valor_conta, porcentagem=10)'. 
    Note que, se o usuário não informar a porcentagem, a função deve assumir automaticamente o valor de 10%.
    A função deve retornar o valor exato da gorjeta.
    Faça dois testes no seu código para demonstrar o funcionamento:
    1. Passando apenas o valor da conta (usando o padrão de 10%).
    2. Passando o valor da conta e uma porcentagem customizada (ex: 15%).

Exemplo de Execução:
    Valor da Conta: R$ 100.00
    --------------------------------------------------------
    > Teste 1 (Gorjeta padrão 10%): R$ 10.00
    > Teste 2 (Gorjeta customizada 15%): R$ 15.00
--------------------------------------------------------
"""
# Desenvolva a sua função e o seu código abaixo:

# A mágica acontece aqui: 'porcentagem=10' define o valor padrão!
def calcular_gorjeta(valor_conta, porcentagem=10):
    gorjeta = valor_conta * (porcentagem / 100)
    return gorjeta

print("""
---------------- Calculadora de Gorjeta ----------------
""")

valor_informado = float(input("Informe o Valor da Conta (R$): "))

print("""
---------------- Resultados dos Testes -----------------
""")

# Teste 1: Omitindo o segundo parâmetro (O Python usa o 10% padrão)
gorjeta_padrao = calcular_gorjeta(valor_informado)
print(f"> Teste 1 (Gorjeta padrão 10%): R$ {gorjeta_padrao:.2f}")

# Teste 2: Passando o segundo parâmetro (O Python sobrescreve o 10 por 15)
gorjeta_customizada = calcular_gorjeta(valor_informado, 15)
print(f"> Teste 2 (Gorjeta custom 15%): R$ {gorjeta_customizada:.2f}")

print("--------------------------------------------------------")