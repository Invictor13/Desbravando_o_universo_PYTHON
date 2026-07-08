"""
DESAFIO 02: O Acumulador de Caixa (Closures e Escopo Nonlocal)

Nível: Avançado (Funções)
Objetivo: Dominar o conceito de Closures e a manipulação de escopos internos usando a palavra-chave 'nonlocal'.
Conceitos: Funções aninhadas (nested functions), variáveis livres, escopo não-local (nonlocal).

Enunciado:
    Desenvolva uma função principal chamada 'criar_caixa_registradora()'. 
    Internamente, ela deve inicializar uma variável chamada 'total_caixa' em 0.0.
    A função deve RETORNAR uma função interna chamada 'adicionar_venda(valor)'.
    Cada vez que a função interna for chamada, ela deve acumular o valor da venda na variável 'total_caixa' 
    (usando nonlocal) e retornar o saldo atualizado do caixa.

Exemplo de Execução:
    caixa = criar_caixa_registradora()
    print(caixa(50.00))  # Retorna 50.0
    print(caixa(25.50))  # Retorna 75.5
    --------------------------------------------------------
    > Venda 1: R$ 50.00
    > Venda 2: R$ 75.50
--------------------------------------------------------
"""
# Desenvolva a sua função e o seu código abaixo: