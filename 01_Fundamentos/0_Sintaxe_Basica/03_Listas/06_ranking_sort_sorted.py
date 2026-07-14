"""
Exercício 06: Ranking de Pontuação (Sort vs Sorted)
    Objetivo: Entender a diferença crucial entre alterar uma lista definitivamente e gerar uma cópia ordenada.
    Conceitos: Método .sort(), função embutida sorted() e parâmetro reverse=True.

Enunciado:
    Crie um programa que possua uma lista desordenada com 5 pontuações de jogadores (ex: 45, 12, 89, 34, 76).
    O programa deve demonstrar duas formas de ordenação:
    
    1. Exiba uma versão ordenada crescente temporária da lista (sem alterar a lista original).
    2. Modifique a lista original ordenando-a de forma decrescente (do maior para o menor) 
       para formar um pódio definitivo. Exiba o Top 3 (usando fatiamento, se quiser!).

Exemplo de Execução:
    Pontuações Originais: [45, 12, 89, 34, 76]
    --------------------------------------------------------
    > Ordenação Temporária (Crescente): [12, 34, 45, 76, 89]
    > A lista original continua igual: [45, 12, 89, 34, 76]
    
    Aplicando ordenação definitiva para o Pódio...
    > Ranking Oficial (Decrescente): [89, 76, 45, 34, 12]
    > 🏆 TOP 3: [89, 76, 45]
    --------------------------------------------------------
"""

lista = [45, 12, 89, 34, 76]
print(f">Lista Original: {lista}")

lista_crescente = sorted(lista)
print(f">Lista Ordenada: {lista_crescente}")
lista_decrescente = sorted(lista, reverse = True)

print(f"> TOP 3: {lista_decrescente[-5:-2]}")