"""
Exercício 11: Reversão de Palavras na Frase
    Objetivo: Inverter a ordem das palavras em uma frase completa, mantendo a escrita correta de cada palavra.
    Conceitos: Uso de .split(), inversão de listas e reconstrução de texto com .join().

Enunciado:
    Crie um programa que solicite uma frase ao usuário. Diferente de um palíndromo 
    que inverte letra por letra, o seu sistema deve inverter a posição das palavras 
    dentro da frase.

Exemplo de Execução:
    Digite uma frase: O Python é incrível
    --------------------------------------------------------
    > Nova frase: incrível é Python O
    --------------------------------------------------------
"""

# Entrada do usuário
frase = input("Digite uma frase: ")

# 1. Separa a frase em uma lista de palavras
palavras = frase.split()

# 2. Inverte a ordem dos elementos da lista utilizando fatiamento (slice)
palavras_invertidas = palavras[::-1]

# 3. Reconstrói o texto unindo as palavras por espaços
nova_frase = " ".join(palavras_invertidas)

print("--------------------------------------------------------")
print(f"> Nova frase: {nova_frase}")
print("--------------------------------------------------------")