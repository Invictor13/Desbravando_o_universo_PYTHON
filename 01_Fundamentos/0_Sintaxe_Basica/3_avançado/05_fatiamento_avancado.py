"""
DESAFIO 05: Manipulador de Códigos de Segurança (Fatiamento)

Nível: Avançado (Sintaxe Básica)
Objetivo: Explorar a técnica de fatiamento de strings (slicing) com passos positivos e negativos.
Conceitos: Indexação de strings, fatiamento [início:fim:passo], inversão de texto.

Enunciado:
    Crie um script que receba um código de segurança de 8 caracteres digitado pelo usuário (ex: "ABC123X7").
    Utilizando apenas fatiamento de strings (sem loops), extraia e exiba na tela:
    1. Os 3 primeiros caracteres do código.
    2. Os 2 últimos caracteres do código (usando índices negativos).
    3. O código completamente invertido de trás para frente.

Exemplo de Execução:
    Digite o código de 8 caracteres: CONF2026
    --------------------------------------------------------
    Análise do Código:
    > Prefixo (3 primeiros): CON
    > Sufixo (2 últimos): 26
    > Código Invertido: 6202FNOC
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Analisador de Códigos (Slicing) -------
Este script extrairá partes de um texto usando fatiamento avançado
--------------------------------------------------------""", end="\n")