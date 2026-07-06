"""
DESAFIO 10: Pintando a Parede

Nível: Iniciante
Objetivo: Aplicar conceitos de área e cálculo proporcional simples.
Conceitos: Entrada de dados (float), multiplicação, divisão e exibição formatada.

Enunciado:
    Faça um programa que leia a largura e a altura de uma parede em metros. 
    O script deve calcular a sua área e a quantidade de tinta necessária para pintá-la, 
    sabendo que cada litro de tinta pinta uma área de 2 metros quadrados (2 m²).

Exemplo de Execução:
    Largura da parede (m): 2.5
    Altura da parede (m): 4.0
    Sua parede tem a dimensão de 2.5x4.0 e sua área é de 10.0 m².
    Para pintar essa parede, você precisará de 5.0L de tinta.
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Pintando a Parede -------
Este script analisará a área da parede que deverá ser pintada
--------------------------------------------------------""", end="\n")

largura_parede = float(input("Favor informar a largura da parede(M): "))
altura_parede = float(input("Favor informar a altura da parede(M): "))
area_parede = largura_parede*altura_parede

tinta_gastos = area_parede/2

print(f"""
--------------------------------------------------------
1) A sua parede possui as dimensões {largura_parede} x {altura_parede}
2) A área total que deverá ser pintada será de: {area_parede}
3) Será necessário gastar {tinta_gastos} L de tinta para pintar a parede.
--------------------------------------------------------""", end="\n")