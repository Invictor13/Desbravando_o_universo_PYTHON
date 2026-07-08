"""
Exercício 10: Engenharia de Performance (Set vs Lista)
    Objetivo: Provar matematicamente e na prática por que utilizamos Sets em buscas de grandes volumes de dados.
    Conceitos: Módulo time, Big-O Notation (Busca $O(1)$ vs Busca $O(n)$) e operador in.

Enunciado:
    Importe o módulo 'time'. Crie uma lista contendo 1 milhão de números sequenciais (0 a 999999) 
    utilizando list(range()). Em seguida, converta essa mesma lista para um set.
    
    Usando a função time.time() para medir o antes e o depois:
    1. Procure o número 999999 (o último) dentro da Lista usando 'in' e printe o tempo que levou.
    2. Procure o mesmo número 999999 dentro do Set e printe o tempo que levou.
    3. Comente brevemente a diferença absurda de performance demonstrada.

Exemplo de Execução:
    Gerando 1.000.000 de dados... Feito.
    --------------------------------------------------------
    > Tempo de busca na LISTA: 0.009841 segundos.
    > Tempo de busca no SET: 0.000001 segundos.
    --------------------------------------------------------
    O Set foi quase instantâneo!
"""