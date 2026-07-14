"""
Exercício 13: Algoritmo de Contagem de Frequência
    Objetivo: Usar dicionários para construir histogramas lógicos (contar aparições).
    Conceitos: Loops, condicionais de pertencimento e o uso avançado de .get(chave, valor_padrao).

Enunciado:
    Dada a string de texto: "abracadabra", você deve criar um programa que conte 
    quantas vezes cada letra aparece. 
    
    Para isso, crie um dicionário vazio. Percorra a string com um loop 'for'. Para cada 
    letra, verifique se ela já existe no dicionário: se não, adicione com o valor 1; 
    se sim, some 1 ao seu valor atual. (Dica de ouro: O método .get(letra, 0) torna isso incrivelmente fácil).
    Imprima o dicionário de frequências final.

Exemplo de Execução:
    > Analisando o texto: "abracadabra"
    --------------------------------------------------------
    > Frequência de caracteres: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
"""