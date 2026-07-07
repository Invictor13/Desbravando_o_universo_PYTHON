"""
Exercicio 07: Conversor de Medidas

    1) Objetivo: Praticar a recepção de dados flutuantes (float) e operações aritméticas básicas.
    2) Conceitos: Entrada de dados, conversão de tipo (casting) e multiplicação.

Enunciado:
    - Desenvolva um programa que peça ao usuário um valor em metros. O script deve 
    - calcular e exibir esse valor convertido para centímetros e milímetros.
    - Dica: 1 metro = 100 centímetros e 1 metro = 1000 milímetros.

Exemplo de Execução:
------------------------------------
    Digite o valor em metros: 2.5
    Em centímetros: 250.0 cm
    Em milímetros: 2500.0 mm
------------------------------------
"""

print("""
             ------ Converter Medidas -------
Este Script transforma metros em Centímetros e Milímetros
--------------------------------------------------------""", end="\n")

medida_m = float(input("Informe a medida em Metros: "))
medida_cm = medida_m*100
medida_mm = medida_cm*10


print(f"""
--------------------------------------------------------
      Valor em Metros: {medida_m} m;
      Valor em Centímetros: {medida_cm} cm;
      Valor em Milímetors: {medida_mm} mm; 
---------------------------------------------------------""")