"""
DESAFIO 04: Classificador Analítico de Triângulos

Nível: Iniciante (Estruturas de Controle)
Objetivo: Cruzar múltiplas condições para validar a integridade e classificação de formas geométricas.
Conceitos: Operadores lógicos (and), condicionais aninhadas, comparações relacionais (==, !=).

Enunciado:
    Desenvolva um programa que receba o comprimento de três lados (float): Reta A, Reta B e Reta C.
    Primeiro, o sistema deve verificar se essas retas podem formar um triângulo 
    (A soma de dois lados deve ser sempre maior que o terceiro lado). Se não puderem, exiba "As retas não formam um triângulo".
    Se formarem, classifique-o em:
    - Equilátero: Todos os lados iguais.
    - Isósceles: Dois lados iguais e um diferente.
    - Escaleno: Todos os lados diferentes.

Exemplo de Execução:
    Comprimento do Lado A: 5.0
    Comprimento do Lado B: 5.0
    Comprimento do Lado C: 8.0
    --------------------------------------------------------
    Análise Geométrica:
    > Status: As retas formam um triângulo válido!
    > Classificação: Triângulo Isósceles.
    --------------------------------------------------------
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Classificador Analítico de Triângulos -------
Este script validará as medidas e classificará o tipo de triângulo formado
--------------------------------------------------------""", end="\n")

comprimento_A = float(input("Comprimento do Lado A: "))
comprimento_B = float(input("Comprimento do Lado B: "))
comprimento_C = float(input("Comprimento do Lado C: "))

print("--------------------------------------------------------")
print("Análise Geométrica:")

# 1. Validação da Condição de Existência de um Triângulo
if (comprimento_A < comprimento_B + comprimento_C) and (comprimento_B < comprimento_A + comprimento_C) and (comprimento_C < comprimento_B + comprimento_A):
    print("> Status: As retas formam um triângulo válido!")
    
    # 2. Classificação Lógica Avançada (Aninhada)
    if comprimento_A == comprimento_B == comprimento_C:
        print("> Classificação: Triângulo Equilátero.")
    elif comprimento_A != comprimento_B and comprimento_A != comprimento_C and comprimento_B != comprimento_C:
        print("> Classificação: Triângulo Escaleno.")
    else:
        print("> Classificação: Triângulo Isósceles.")
        
else:
    print("> Status: As retas NÃO formam um triângulo.")

print("--------------------------------------------------------")