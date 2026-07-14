"""
Exercicio 11: Conversor de Moedas Básico

    1) Objetivo: Praticar divisão e formatação de dados monetários.
    2) Conceitos: Entrada de dados (float), divisão e formatação com duas casas decimais.

Enunciado:
    -   Crie um script que pergunte quanto dinheiro uma pessoa tem na carteira (em R$) 
    e a taxa de câmbio atual do dólar (ex: 5.00). O programa deve calcular e exibir  
    quantos dólares ela pode comprar com esse valor.

Exemplo de Execução:
-----------------------------------------------------
    Quanto dinheiro você tem na carteira? R$ 50.00
    Qual a cotação atual do dólar? 5.00
    Com R$ 50.00 você pode comprar: US$ 10.00
-----------------------------------------------------
"""

# Desenvolva o seu código abaixo:

print("""
             ------ Conversor de Moedas -------
Este Script Converterá seu valor na Carteira em Real Para Dolar
--------------------------------------------------------""", end="\n")

valor_carteira = float(input("Quantos Reais você possui na carteira(R$): "))
valor_dolar = valor_carteira/5.00  #Pegaremos o Valor Aproximádo em Dólar

print("--------------------------------------------------------",end="\n")
print(f"""
    Valor na Carteira: R$ {valor_carteira:.2f}
    Carteira em Dólar: US$ {valor_dolar:.2f}
      """)
print("--------------------------------------------------------",end="\n")