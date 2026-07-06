"""
DESAFIO 02: Radar de Velocidade Urbano

Nível: Iniciante (Estruturas de Controle)
Objetivo: Praticar tomadas de decisão compostas para aplicar penalidades ou advertências.
Conceitos: Condicionais complexas (if/elif/else), operadores relacionais (>, <=).

Enunciado:
    Escreva um programa que leia a velocidade de um carro (int) em uma via expressa onde o limite é 80 km/h.
    Regras do Sistema:
    - Se a velocidade for menor ou igual a 80 km/h, exiba: "Boa viagem! Você está dentro do limite."
    - Se a velocidade for maior que 80 km/h e até 100 km/h, exiba: "Advertência! Você excedeu o limite levemente."
    - Se a velocidade for maior que 100 km/h, exiba: "Multa Gravíssima! Velocidade perigosa detectada."

Exemplo de Execução:
    Informe a velocidade atual do veículo (km/h): 95
    --------------------------------------------------------
    Monitoramento de Tráfego:
    > Advertência! Você excedeu o limite levemente.
    --------------------------------------------------------
"""

# Desenvolva o seu código abaixo:

velocidade_carro = int(input("Informe a Velocidade do Veículo: "))

if( velocidade_carro <= 80):
    print("Boa viagem! Você está dentro do limite.")
elif( velocidade_carro > 100):
    print("Multa Gravíssima! Velocidade perigosa detectada.")
elif( velocidade_carro >= 80):
    print("Advertência! Você excedeu o limite levemente.")