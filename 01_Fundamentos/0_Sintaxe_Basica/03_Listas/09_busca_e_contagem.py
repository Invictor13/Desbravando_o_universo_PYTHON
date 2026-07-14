"""
Exercício 09: Buscas e Contagens em Listas
    Objetivo: Localizar em qual posição um item está e contar quantas vezes um elemento repetido aparece.
    Conceitos: Métodos nativos .index() e .count().

Enunciado:
    Crie um programa com uma lista de 10 números, garantindo que pelo menos um dos números 
    se repita várias vezes (ex: [1, 5, 2, 5, 8, 5, 9, 3, 5, 0]). 
    Peça ao usuário que digite o número que deseja analisar.
    
    O programa deve procurar o número na lista e exibir:
    1. A posição (índice) da primeira vez que esse número aparece usando .index().
    2. A quantidade total de vezes que esse número se repete na lista usando .count().

Exemplo de Execução:
    Lista de Valores: [1, 5, 2, 5, 8, 5, 9, 3, 5, 0]
    Qual número deseja analisar? 5
    --------------------------------------------------------
    > O número 5 aparece 4 vez(es) na lista.
    > A sua primeira aparição está no índice: 1
    --------------------------------------------------------
"""

lista = [1, 5, 2, 5, 8, 5, 9, 3, 5, 0]

x = int(input("> Informe um Inteiro: "))

if x in lista:
    y = lista.index(x)
    print(y)
    soma = lista.count(x)
    print(soma)