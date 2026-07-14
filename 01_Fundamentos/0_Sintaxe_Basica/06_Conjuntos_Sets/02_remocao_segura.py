"""
Exercício 02: Remoção Segura de Elementos
    Objetivo: Entender a diferença crítica entre os métodos de remoção em conjuntos e evitar quebras no código (KeyError).
    Conceitos: Métodos .remove() e .discard().

Enunciado:
    Crie um conjunto contendo os números de 1 a 5. 
    1. Tente remover o número 3 utilizando o método .remove() e exiba o conjunto.
    2. Tente remover o número 10 (que não existe) utilizando o método .discard() e 
       comprove através de um print que o programa não quebrou.
    3. Em um bloco de comentário, explique brevemente o que aconteceria se você usasse 
       o .remove(10) no lugar do .discard().

Exemplo de Execução:
    > Conjunto Inicial: {1, 2, 3, 4, 5}
    > Após remover o 3: {1, 2, 4, 5}
    > Tentando remover o 10 com .discard()... Sucesso, o código continuou rodando!
"""