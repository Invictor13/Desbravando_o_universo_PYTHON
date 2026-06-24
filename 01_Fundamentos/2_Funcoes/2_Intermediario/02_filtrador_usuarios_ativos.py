"""
DESAFIO 02: Filtrador de Base de Usuários (Dicionários em Listas)

Nível: Intermediário (Funções)
Objetivo: Percorrer e filtrar listas compostas por múltiplos dicionários através de critérios lógicos.
Conceitos: Iteração de coleções dentro de funções, métodos de lista (.append), filtros condicionais.

Enunciado:
    Imagine que você recebeu uma base de dados simulada por uma lista de dicionários, onde cada 
    dicionário possui as chaves 'nome' (str) e 'ativo' (bool).
    Crie uma função chamada 'filtrar_ativos(usuarios)' que percorra essa lista e RETORNE uma 
    NOVA lista contendo apenas os nomes (strings) dos usuários que estão com o status 'ativo' como True.

Exemplo de Execução:
    Base original: [
        {"nome": "Victor", "ativo": True},
        {"nome": "Jessica", "ativo": True},
        {"nome": "Eros", "ativo": False}
    ]
    --------------------------------------------------------
    > Lista de Usuários Ativos: ['Victor', 'Jessica']
--------------------------------------------------------
"""
# Desenvolva a sua função e o seu código abaixo: