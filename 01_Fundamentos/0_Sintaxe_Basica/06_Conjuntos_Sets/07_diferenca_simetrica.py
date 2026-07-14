"""
Exercício 07: Diferença Simétrica (Exclusividade)
    Objetivo: Encontrar os elementos que são completamente exclusivos de cada conjunto (o inverso da interseção).
    Conceitos: Método .symmetric_difference() ou operador ^.

Enunciado:
    Dois amigos, Lucas e Camila, fizeram listas de filmes que querem assistir. 
    lucas_filmes = {"Matrix", "Inception", "Duna", "Avatar"}
    camila_filmes = {"Duna", "Interstellar", "Avatar", "Gravidade"}
    
    Eles querem descobrir quais filmes são interesses exclusivos de apenas um deles 
    (ou seja, excluir os filmes que ambos querem ver). Utilize a Diferença Simétrica 
    para extrair essa lista e exiba-a.

Exemplo de Execução:
    Comparando interesses...
    --------------------------------------------------------
    > Filmes para assistir sozinhos (Interesses exclusivos): {'Matrix', 'Inception', 'Interstellar', 'Gravidade'}
"""