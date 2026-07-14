"""
Exercício 14: Agrupamento por Categoria (Listas em Dicionários)
    Objetivo: Combinar estruturas (Dicionários contendo Listas) para categorizar dados.
    Conceitos: Inicialização de chaves dinâmicas, método .append() em valores de dicionário.

Enunciado:
    Imagine que você tem uma lista bruta contendo tuplas de produtos e seus departamentos:
    dados = [("Notebook", "TI"), ("Mouse", "TI"), ("Mesa", "Escritorio"), ("Monitor", "TI"), ("Cadeira", "Escritorio")]
    
    Crie um algoritmo que leia essa lista e construa um dicionário onde a chave é 
    o nome do departamento, e o valor é uma lista contendo os itens daquele departamento.
    Imprima o dicionário final para mostrar os dados perfeitamente categorizados.

Exemplo de Execução:
    Agrupando produtos por departamento...
    --------------------------------------------------------
    > Categoria TI: ['Notebook', 'Mouse', 'Monitor']
    > Categoria Escritorio: ['Mesa', 'Cadeira']
"""