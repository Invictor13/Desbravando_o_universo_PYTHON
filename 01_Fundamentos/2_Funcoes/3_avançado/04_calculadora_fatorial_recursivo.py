"""
DESAFIO 04: Motor de Recursividade (Cálculo de Fatorial)

Nível: Avançado (Funções)
Objetivo: Compreender a estrutura de funções que chamam a si mesmas (Recursão) e a definição de caso base.
Conceitos: Funções recursivas, pilha de execução (call stack), caso base e caso recursivo.

Enunciado:
    Crie uma função matemática recursiva chamada 'calcular_fatorial(numero)'.
    A função deve calcular o fatorial de um número inteiro positivo passado por parâmetro.
    - Caso base: Se o número for 0 ou 1, a função deve retornar 1 de imediato.
    - Caso recursivo: A função deve retornar o número multiplicado pela chamada de si mesma passando (numero - 1).

Exemplo de Execução:
    Digite um número para calcular o fatorial: 5
    --------------------------------------------------------
    > O fatorial de 5 (5!) é exatamente: 120
--------------------------------------------------------
"""
# Desenvolva a sua função recursiva abaixo: