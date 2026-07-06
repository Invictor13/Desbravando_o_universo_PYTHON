"""
DESAFIO 04: Limpador de Itens Duplicados

Nível: Intermediário
Objetivo: Compreender a diferença entre listas e conjuntos (sets) para remoção de duplicadas.
Conceitos: Listas, conversão de tipos (casting para set), ordenação e manipulação de coleções.

Enunciado:
    Crie um script que simule a limpeza de um carrinho de compras ou lista de tarefas 
    onde o usuário acabou digitando itens repetidos. O programa deve receber 6 nomes 
    de produtos inseridos pelo usuário e adicioná-los a uma lista. Em seguida:
    1. Remova todos os elementos duplicados da lista (Dica: converta a lista para 'set').
    2. Exiba os produtos únicos na tela organizados em ordem alfabética.

Exemplo de Execução:
    Produto 1: Banana
    Produto 2: Maçã
    Produto 3: Banana
    Produto 4: Uva
    Produto 5: Maçã
    Produto 6: Laranja
    --------------------------------------------------------
    Produtos únicos cadastrados (Ordem Alfabética):
    ['Banana', 'Laranja', 'Maçã', 'Uva']
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Limpador de Duplicadas -------
Este script identificará e removerá itens repetidos da sua lista
--------------------------------------------------------""", end="\n")
lista = []
n1=input("Favor Informar uma fruta: ")
lista.append(n1)
n2=input("Favor Informar uma fruta: ")
lista.append(n2)
n3=input("Favor Informar uma fruta: ")
lista.append(n3)
n4=input("Favor Informar uma fruta: ")
lista.append(n4)
n5=input("Favor Informar uma fruta: ")
lista.append(n5)
n6=input("Favor Informar uma fruta: ")
lista.append(n6)

print("----------- Lista Informada Pelo Usuário ------------")
print(lista)
print("----------- Lista Corrigida Sem Repetição -----------")
lista_corrigida = set(lista)
lista_ordenada = sorted(lista_corrigida)
print(lista_ordenada)