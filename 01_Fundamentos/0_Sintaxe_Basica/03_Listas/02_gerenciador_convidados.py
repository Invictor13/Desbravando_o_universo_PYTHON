"""
Exercício 02: Gerenciador de Convidados VIP
    Objetivo: Adicionar elementos dinamicamente no final da lista e inserir elementos em posições específicas.
    Conceitos: Métodos .append() e .insert().

Enunciado:
    Crie um programa que inicie com uma lista vazia de convidados. Solicite ao usuário que 
    digite o nome de 3 convidados comuns, adicionando-os um a um ao final da lista. 
    
    Após isso, avise que um Convidado VIP chegou de surpresa. Insira esse convidado VIP 
    exatamente na primeira posição da fila (índice 0), empurrando os demais para trás. 
    Exiba a lista final.

Exemplo de Execução:
    Adicione 3 convidados:
    > Convidado 1: Lucas
    > Convidado 2: Maria
    > Convidado 3: João
    
    Um Convidado VIP ("Rei Python") chegou!
    --------------------------------------------------------
    > Lista Final de Convidados: ['Rei Python', 'Lucas', 'Maria', 'João']
    --------------------------------------------------------
"""

# Inicializa a lista vazia
lista_convidados = []

print("Adicione 3 convidados:")
# Captura os 3 convidados comuns usando .append()
convidado1 = input("> Convidado 1: ")
lista_convidados.append(convidado1)

convidado2 = input("> Convidado 2: ")
lista_convidados.append(convidado2)

convidado3 = input("> Convidado 3: ")
lista_convidados.append(convidado3)

print("\nUm Convidado VIP (\"Rei Python\") chegou!")

# Correção 1: Atribuição correta usando '='
convidado_vip = "Rei Python"  # Defini como "Rei Python" para bater com o exemplo do enunciado

# Correção 2: Inserir no índice 0 (primeira posição) empurrando os outros para trás
lista_convidados.insert(0, convidado_vip)

# Exibição do resultado final idêntico ao exemplo
print("--------------------------------------------------------")
print(f"> Lista Final de Convidados: {lista_convidados}")
print("--------------------------------------------------------")
