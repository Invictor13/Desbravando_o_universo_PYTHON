"""
Exercício 07: Fatiamento e Cópias Independentes (Sublistas)
    Objetivo: Aplicar a sintaxe de slicing [:] em listas para extrair porções específicas e criar cópias independentes.
    Conceitos: Fatiamento (slicing) e prevenção de problemas de referência de memória.

Enunciado:
    Crie um programa que inicie uma lista com 8 nomes de cidades. Utilizando exclusivamente a sintaxe 
    de fatiamento (slicing), o sistema deve extrair e exibir:
    1. Os 3 primeiros itens da lista.
    2. Os 3 últimos itens da lista.
    
    Em seguida, crie uma cópia exata e independente da lista original. Modifique um item 
    na lista original e exiba ambas as listas para provar que a cópia não foi afetada 
    (provando que não dividem a mesma referência de memória).

Exemplo de Execução:
    > Lista Original: ['Rio', 'SP', 'BH', 'Curitiba', 'Manaus', 'Natal', 'Recife', 'Fortaleza']
    > Primeiros 3: ['Rio', 'SP', 'BH']
    > Últimos 3: ['Natal', 'Recife', 'Fortaleza']
    --------------------------------------------------------
    Alterando a original...
    > Original alterada: ['Modificado', 'SP', 'BH', 'Curitiba', 'Manaus', 'Natal', 'Recife', 'Fortaleza']
    > Cópia Independente (Intacta): ['Rio', 'SP', 'BH', 'Curitiba', 'Manaus', 'Natal', 'Recife', 'Fortaleza']
"""

lista = ['Rio', 'SP', 'BH', 'Curitiba', 'Manaus', 'Natal', 'Recife', 'Fortaleza']

print(lista[:3])
print(lista[-3:])

lista_modificada = lista.append("Modificado", 0)