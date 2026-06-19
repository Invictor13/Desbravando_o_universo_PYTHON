"""
DESAFIO 08: Mascarador de Dados Sensíveis (Slicing e Lógica)

Nível: Avançado (Sintaxe Básica)
Objetivo: Tratar strings ocultando informações sensíveis e validar o tamanho do dado recebido.
Conceitos: Fatiamento de strings, concatenação, multiplicação de caracteres e comparação booleana.

Enunciado:
    Em conformidade com as leis de privacidade de dados, sistemas costumam mascarar números de cartões.
    Crie um script que receba um número de cartão de crédito de 16 dígitos (apenas números, como string).
    O programa deve:
    1. Gerar uma nova string mostrando apenas os 4 primeiros e os 4 últimos dígitos, substituindo os 8 dígitos do meio por '*'.
    2. Verificar se o cartão digitado possui exatamente 16 caracteres (retornando True ou False).
    Exiba o número mascarado e o resultado booleano da validação do tamanho na tela.

Exemplo de Execução:
    Digite o número do cartão (16 dígitos): 1234567890123456
    --------------------------------------------------------
    Processamento de Segurança:
    > Cartão Mascarado: 1234********3456
    > Cartão com tamanho válido? True
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Mascarador de Dados Sensíveis -------
Este script ocultará os dígitos centrais de um cartão e validará o seu formato
--------------------------------------------------------""", end="\n")