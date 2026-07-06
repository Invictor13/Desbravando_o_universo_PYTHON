"""
DESAFIO 02: Catálogo de Jogos Clássicos

Nível: Intermediário
Objetivo: Compreender o uso de tuplas para dados imutáveis e fatiamento com índices.
Conceitos: Tuplas, indexação (0 a N), fatiamento e índices negativos.

Enunciado:
    Crie uma tupla preenchida com o nome de 5 jogos marcantes (ex: "Zelda: Ocarina of Time", 
    "Star Wars: KOTOR", "Kingdom Hearts", "Crimson Desert", "Super Mario World"). 
    O script deve:
    1. Exibir o catálogo completo na tela.
    2. Pedir para o usuário digitar um número de 1 a 5 para escolher um jogo.
    3. Mostrar o jogo correspondente àquela posição (tratando o índice do Python).
    4. Exibir o primeiro e o último jogo do catálogo usando índices diretos e negativos.

Exemplo de Execução:
    Catálogo de Jogos: ('Zelda', 'Star Wars', 'Kingdom Hearts', 'Crimson Desert', 'Mario')
    Escolha um jogo pelo número (1-5): 2
    --------------------------------------------------------
    Você escolheu o jogo: Star Wars
    Primeiro jogo do catálogo: Zelda
    Último jogo do catálogo: Mario
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Catálogo de Jogos -------
Este script exibirá uma lista imutável de jogos clássicos
--------------------------------------------------------""", end="\n")

# 1. Criando a TUPLA com parênteses ( ) e exibindo o catálogo completo
tupla = ("Zelda: Ocarina of Time", "Star Wars: KOTOR", "Kingdom Hearts", "Crimson Desert", "Super Mario World")
print(f"Catálogo de Jogos: {tupla}")
print("--------------------------------------------------------")

# 2. Entrada do usuário
user_escolha = int(input("Por favor, escolha um jogo pelo número (1-5): "))

# Ajustando o índice do usuário (ex: se escolher 2, vira índice 1)
indice_real = user_escolha - 1

# 3 e 4. Exibindo os resultados usando os colchetes [ ] e o índice negativo -1 para o último
print(f"""
      1) Você escolheu o jogo: {tupla[indice_real]}
      2) Primeiro Jogo do catálogo (Índice 0): {tupla[0]}
      3) Último Jogo do catálogo (Índice -1): {tupla[-1]}
--------------------------------------------------------""")