"""
DESAFIO 03: Processador de Altas Ordens (Map e Filter com Lambda)

Nível: Avançado (Funções)
Objetivo: Utilizar funções anônimas (lambda) combinadas com funções nativas de processamento de coleções.
Conceitos: Funções Lambda, filter(), map(), conversão de iteradores para listas.

Enunciado:
    Você recebeu uma lista com os preços brutos de vários produtos: [100, 250, 400, 80, 150, 600].
    Crie um script que execute um pipeline de duas etapas utilizando funções puras de alta ordem:
    1. Filtre a lista para manter apenas os produtos com preço estritamente MAIOR que 150 (use filter e lambda).
    2. Aplique um reajuste de 10% de inflação sobre os preços que restaram (use map e lambda).
    Retorne e exiba a lista final processada.

Exemplo de Execução:
    Lista Original: [100, 250, 400, 80, 150, 600]
    --------------------------------------------------------
    > Pipeline Finalizado (Produtos > 150 com +10%): [275.0, 440.0, 660.0]
--------------------------------------------------------
"""
# Desenvolva o seu código utilizando funções de alta ordem abaixo: