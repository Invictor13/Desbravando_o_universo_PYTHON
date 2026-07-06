"""
DESAFIO 08: Unificador de Listas de Transmissão

Nível: Intermediário
Objetivo: Combinar listas diferentes e garantir que não haja elementos duplicados no resultado final.
Conceitos: Listas, manipulação de múltiplos conjuntos de dados, conversão de tipos (set) e ordenação.

Enunciado:
    Imagine que você tem duas listas de convidados ou contatos vindas de fontes diferentes. 
    Crie duas listas distintas no seu código: a primeira com 3 nomes e a segunda com 3 nomes 
    (coloque pelo menos 1 nome repetido entre as duas listas para testar o script).
    O programa deve:
    1. Unir as duas listas em uma única estrutura.
    2. Filtrar a lista final para remover qualquer nome duplicado.
    3. Exibir a lista unificada e limpa em ordem alfabética.

Exemplo de Execução:
    Lista 1: ['Victor', 'Jessica', 'Ana']
    Lista 2: ['Carlos', 'Victor', 'Mariana']
    --------------------------------------------------------
    Lista de convidados unificada (Sem repetições):
    ['Ana', 'Carlos', 'Jessica', 'Mariana', 'Victor']
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Unificador de Listas -------
Este script combinará duas listas diferentes e removerá as duplicadas
--------------------------------------------------------""", end="\n")

lista1 = ['Victor', 'Jessica', 'Ana']
lista2 = ['Carlos', 'Victor', 'Mariana']

print("Primeira Lista: ",lista1)
print("Segunda Lista: ",lista2)

print("\n-------- Validando Informações ---------")
lista_unificada= lista1 + lista2
print("Lista Unificada: ", lista_unificada)

print("\n---- Removendo Duplicados ----")
lista_sem_duplicadas = set(lista_unificada)
print("Lista Sem Duplicados: ", lista_sem_duplicadas)

print("\n---- Lista Ordenada ----")
lista_ordenada = sorted(lista_sem_duplicadas)
print("Lista Ordenada: ",lista_ordenada)
