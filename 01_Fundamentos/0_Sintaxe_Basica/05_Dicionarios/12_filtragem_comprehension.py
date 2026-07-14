"""
Exercício 12: Filtragem com Dict Comprehension
    Objetivo: Criar novos dicionários a partir de outros aplicando lógicas de forma expressiva (em 1 linha).
    Conceitos: Dict Comprehension {k: v for k, v in dict.items() if condicao}.

Enunciado:
    Crie um dicionário contendo os nomes de 5 alunos e suas respectivas notas finais 
    (ex: {"João": 6.5, "Maria": 9.0, "Pedro": 5.0, "Bia": 8.5}).
    
    Utilizando exclusivamente a sintaxe de Dict Comprehension (em uma única linha), 
    crie um novo dicionário chamado 'aprovados' que contenha apenas os alunos com nota 
    maior ou igual a 7.0. Imprima o dicionário de alunos aprovados.

Exemplo de Execução:
    > Turma Completa: {'João': 6.5, 'Maria': 9.0, 'Pedro': 5.0, 'Bia': 8.5}
    --------------------------------------------------------
    Filtrando aprovados (Nota >= 7.0)...
    > Alunos Aprovados: {'Maria': 9.0, 'Bia': 8.5}
"""