"""
DESAFIO 02: Sobrecarga de Operadores com Métodos Mágicos (Dunder Methods)

Nível: Avançado (POO)
Objetivo: Ensinar o Python a interagir matematicamente com os seus objetos customizados.
Conceitos: Métodos mágicos (__str__, __add__, __eq__), sobrecarga de operadores, representação de objetos.

Enunciado:
    Crie uma classe chamada 'Vetor2D' que represente uma coordenada matemática espacial com os atributos 'x' e 'y'.
    Implemente os seguintes Dunder Methods para dar superpoderes à sua classe:
    1. '__init__(self, x, y)': Construtor tradicional.
    2. '__str__(self)': Retorna a string formatada no padrão "Vetor2D(X, Y)".
    3. '__add__(self, outro_vetor)': Permite somar dois objetos Vetor2D utilizando o operador aritmético '+'. 
       A soma deve gerar um NOVO objeto Vetor2D somando o X de um com o X do outro (e o mesmo para Y).
    4. '__eq__(self, outro_vetor)': Permite comparar se dois vetores são idênticos utilizando o operador '=='.

Exemplo de Execução:
    v1 = Vetor2D(3, 5)
    v2 = Vetor2D(1, 2)
    print(v1 + v2)  # Deve exibir: Vetor2D(4, 7)
    print(v1 == v2) # Deve exibir: False
--------------------------------------------------------
"""
# Desenvolva a sua classe e o código de teste abaixo: