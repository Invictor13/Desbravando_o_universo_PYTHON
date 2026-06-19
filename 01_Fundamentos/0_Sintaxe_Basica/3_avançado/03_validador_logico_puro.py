"""
DESAFIO 03: Validador Lógico de Empréstimo (Expressões Booleanas)

Nível: Avançado (Sintaxe Básica)
Objetivo: Construir expressões lógicas complexas combinando múltiplos operadores relacionais e lógicos.
Conceitos: Operadores relacionais (>, <, ==), operadores lógicos (and, or, not) e saída booleana direta.

Enunciado:
    Crie um sistema analítico para um banco que avalia se um cliente tem direito a uma linha de crédito. 
    O programa deve pedir três informações: Renda Mensal (float), Idade (int) e se possui Nome Limpo (True/False).
    A regra para o crédito ser aprovado (retornar True) é:
    - Ter o Nome Limpo AND (Renda Mensal maior ou igual a 3000.00 OR Idade maior que 21 anos).
    Exiba o resultado final da análise diretamente como um valor booleano (True ou False) na tela.

Exemplo de Execução:
    Informe a Renda Mensal (R$): 2500.00
    Informe a sua Idade: 25
    Possui nome limpo? (True/False): True
    --------------------------------------------------------
    Resultado da avaliação de crédito: True
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Validador Lógico de Crédito -------
Este script avaliará critérios combinados usando lógica booleana pura
--------------------------------------------------------""", end="\n")