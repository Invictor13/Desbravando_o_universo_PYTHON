"""
DESAFIO 09: Aluguel de Carros

Nível: Iniciante
Objetivo: Juntar múltiplos tipos de dados e operadores para resolver um problema real.
Conceitos: Entrada de dados (int e float), multiplicação e soma.

Enunciado:
    Escreva um programa que pergunte a quantidade de dias pelos quais um carro 
    foi alugado e a quantidade de quilômetros (km) percorridos. Calcule o preço total 
    a pagar, sabendo que o carro custa R$ 60.00 por dia e R$ 0.15 por km rodado.

Exemplo de Execução:
    Quantos dias o carro foi alugado? 5
    Quantos km foram percorridos? 200
    O total a pagar pelo aluguel é: R$ 330.00
"""

# Desenvolva o seu código abaixo:


print("""
             ------ Aluguel de Carros -------
Este Script Calculará o Valor Total a Pagar Pelo Aluguel de um Carro
--------------------------------------------------------""", end="\n")

dias_alugados = int(input("Informe a quantidade de dias que o carro foi alugado: "))
km_percorridos = float(input("Informe a quantidade de km percorridos: "))

valor_aluguel = 60*dias_alugados + 0.15*km_percorridos

print(f"""
    ---------------------------------------------
    Valor a Pagar(R$): {valor_aluguel}
    ---------------------------------------------  
      """)
