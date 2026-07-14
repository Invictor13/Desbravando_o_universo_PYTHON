"""
Exercício 07: Criptografia com Cifra de César Modular
    Objetivo: Introdução à criptografia básica e manipulação de caracteres a nível ASCII[cite: 145].
    Conceitos: Funções embutidas ord() (converte caractere para número) e chr() (converte número para caractere)[cite: 146].

Enunciado:
    Crie um programa que receba uma mensagem de texto e um número inteiro que representará a "chave" 
    de deslocamento. O programa deve encriptar a mensagem rotacionando as letras utilizando a lógica da 
    Cifra de César. Faça a conversão de cada caractere para seu número ASCII, some a chave de 
    deslocamento e converta de volta para texto.

Exemplo de Execução:
    Digite a mensagem: abc
    Digite a chave de deslocamento: 2
    --------------------------------------------------------
    Resultado da Criptografia:
    > Mensagem Original: abc
    > Mensagem Encriptada: cde
    --------------------------------------------------------
"""

# [1] Entrada de dados, utilizando os valores do enunciado
mensagem = "abc"
chave = 2

# [2] Separando cada caractere da string original
#   1. Repare que criamos 3 variáveis atribuindo uma letra pra cada uma.
letra_1 = mensagem[0]
letra_2 = mensagem[1]
letra_3 = mensagem[2]

# 2. Convertendo para o código ASCII correspondente
#O que é a Tabela ASCII e o método ord():
# O computador não entende letras, apenas números. A Tabela ASCII é um dicionário 
# universal que associa cada caractere a um número exclusivo (ex: 'a' vale 97).
# A função ord() revela esse número secreto, permitindo que a Cifra de César faça 
# contas matemáticas com o texto (ex: somar +2 ao código da letra para empurrá-la).
ascii_1 = ord(letra_1)
ascii_2 = ord(letra_2)
ascii_3 = ord(letra_3)

# 3. Aplicando o deslocamento (somando a chave)
novo_ascii_1 = ascii_1 + chave
novo_ascii_2 = ascii_2 + chave
novo_ascii_3 = ascii_3 + chave

# 4. Convertendo os novos números de volta para caracteres
nova_letra_1 = chr(novo_ascii_1)
nova_letra_2 = chr(novo_ascii_2)
nova_letra_3 = chr(novo_ascii_3)

# 5. Juntando as novas letras na mensagem encriptada
mensagem_encriptada = nova_letra_1 + nova_letra_2 + nova_letra_3

# Exibição dos resultados formatados
print("--------------------------------------------------------")
print("Resultado da Criptografia:")
print(f"> Mensagem Original: {mensagem}")
print(f"> Mensagem Encriptada: {mensagem_encriptada}")
print("--------------------------------------------------------")