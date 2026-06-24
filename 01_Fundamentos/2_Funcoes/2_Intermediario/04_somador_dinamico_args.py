"""
DESAFIO 04: Somador Dinâmico Avançado (*args)

Nível: Intermediário (Funções)
Objetivo: Dominar o conceito de empacotamento de argumentos variáveis usando a sintaxe *args.
Conceitos: Argumentos arbitrários (*args), iteração em tuplas geradas, fator multiplicador.

Enunciado:
    Crie uma função chamada 'somar_com_fator(fator, *numeros)'.
    A função deve aceitar obrigatoriamente um número como 'fator' e, logo em seguida, uma quantidade 
    indefinida de outros números (*args). A lógica interna deve somar todos os números passados no 
    *args e, no final, MULTIPLICAR o resultado da soma pelo valor do 'fator'. Retorne o total calculado.

Exemplo de Execução:
    Chamada: somar_com_fator(2, 5, 5, 5)  -> Soma (5+5+5=15) * Fator (2)
    --------------------------------------------------------
    > O resultado final calculado é: 30
--------------------------------------------------------
"""
# Desenvolva a sua função e o seu código abaixo: