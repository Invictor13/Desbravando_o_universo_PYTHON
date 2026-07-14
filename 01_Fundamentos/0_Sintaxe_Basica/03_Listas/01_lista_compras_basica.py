"""
Exercício 01: Lista de Compras Básica
    Objetivo: Entender a criação de listas, o acesso a elementos por índices positivos e negativos, e a substituição direta de valores.
    Conceitos: Listas [], índices (0, 1, -1) e atribuição de valores.

Enunciado:
    Crie um programa que inicie uma lista de compras contendo 5 itens de supermercado à sua escolha.
    O sistema deve exibir:
    1. A lista completa.
    2. O primeiro item da lista (usando índice positivo).
    3. O último item da lista (usando índice negativo).
    
    Em seguida, simule uma troca: substitua o terceiro item da lista (índice 2) pela string "Café". 
    Exiba a lista final atualizada.

Exemplo de Execução:
    --- Lista de Compras ---
    > Original: ['Maçã', 'Banana', 'Leite', 'Pão', 'Ovos']
    > Primeiro item: Maçã
    > Último item: Ovos
    --------------------------------------------------------
    Trocando o 3º item por Café...
    > Nova lista: ['Maçã', 'Banana', 'Café', 'Pão', 'Ovos']
    --------------------------------------------------------
"""

# Criando a lista com os 5 elementos:
lista = ["Maçã","Banana","Leite","Feijão","Arroz"]
print(lista)

#Substituindo o terceiro item por café:
lista[2] = "Café"
print(lista)