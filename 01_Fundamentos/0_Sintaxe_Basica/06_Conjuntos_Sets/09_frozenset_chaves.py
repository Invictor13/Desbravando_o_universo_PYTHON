"""
Exercício 09: Chaves Imutáveis com Frozenset
    Objetivo: Contornar a limitação de que dicionários não aceitam tipos mutáveis (como sets e listas) como chaves.
    Conceitos: Função embutida frozenset() e imutabilidade.

Enunciado:
    Imagine que você quer criar um dicionário de rotas de viagem, onde a chave é o conjunto de 
    duas cidades conectadas, e o valor é a distância entre elas. Como a ordem não importa 
    (A pra B é igual B pra A), um Set seria a chave perfeita. Porém, Sets normais são mutáveis 
    e não podem ser chaves de dicionário.
    
    Transforme os conjuntos de cidades em frozensets e utilize-os como chaves de um dicionário. 
    Exiba a distância buscando a rota através de um novo frozenset de pesquisa.

Exemplo de Execução:
    > Rota ('SP', 'RJ') cadastrada com sucesso!
    > A distância entre RJ e SP é: 430 km
"""