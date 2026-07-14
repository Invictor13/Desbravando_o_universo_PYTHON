"""
Exercício 09: Tuplas como Chaves de Dicionários
    Objetivo: Provar a característica "hashable" das tuplas gerada pela sua imutabilidade, algo impossível de se fazer com listas.
    Conceitos: Dicionários {}, tuplas () como chaves e mapeamento de coordenadas (X, Y).

Enunciado:
    Imagine que você está desenvolvendo um mapa 2D para um jogo. Crie um dicionário onde as chaves sejam 
    tuplas representando coordenadas (x, y) e os valores sejam strings informando o que existe naquela 
    posição (ex: (5, 5): "Tesouro", (1, 2): "Inimigo", (3, 3): "Árvore").
    
    Peça ao usuário para digitar uma coordenada X e uma Y. Transforme essas entradas em uma tupla e 
    busque no dicionário (utilize o método .get() para não quebrar o código). Se a coordenada existir, 
    exiba o que foi encontrado. Se não, exiba "Caminho livre".

Exemplo de Execução:
    --- Radar do Jogo ---
    Digite a coordenada X: 5
    Digite a coordenada Y: 5
    --------------------------------------------------------
    > Alerta: Você encontrou um(a) Tesouro!
    --------------------------------------------------------
"""