"""
DESAFIO 06: Calculadora de Descontos

Nível: Iniciante
Objetivo: Trabalhar com percentagem, operadores aritméticos e formatação de strings.
Conceitos: Operações matemáticas, precedência de operadores e interpolação de strings.

Enunciado:
    Crie um script que receba o preço original de um produto e a percentagem de 
    desconto que será aplicada (ex: o usuário digita 15 para 15%). O programa deve 
    calcular o valor final do produto com o abatimento e exibir o resultado.

Exemplo de Execução:
    Digite o preço do produto (R$): 120.00
    Digite a percentagem de desconto (%): 15
    O preço do produto com 15% de desconto é: R$ 102.00
"""

# Desenvolva o seu código abaixo:

print("""
             ------ Calcular Desconto -------
Este Script Calculará o valor do Desconto do Produto
--------------------------------------------------------""", end="\n")

valor_produto = float(input("Por favor, informe o valor do Produto(R$): "))
desconto=int(input("Qual o valor do Desconto(%): "))

valor_final=(valor_produto*(1-desconto/100))

print("--------------------------------------------------------",end="\n")
print(f"""
    Valor do Produto(R$):{valor_produto}
    Desconto Aplicado(%):{desconto}

    Valor Final(R$): {valor_final}
      """)
print("--------------------------------------------------------",end="\n")