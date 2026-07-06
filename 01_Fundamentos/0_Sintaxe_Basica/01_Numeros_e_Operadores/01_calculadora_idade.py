"""
DESAFIO 02: Calculadora de Idade

Nível: Iniciante
Objetivo: Praticar manipulação de variáveis, operações matemáticas simples e conversão de tipos (casting).
Conceitos: Entrada de dados, conversão para inteiro (int) e subtração.

Enunciado:
    Crie um programa que solicite o ano de nascimento do usuário e o ano atual. 
    Calcule e exiba a idade estimada da pessoa.
    
    Dica: Lembre-se de converter o valor do input() que vem como string para inteiro.

Exemplo de Execução:
    Digite o ano de seu nascimento: 1993
    Digite o ano atual: 2026
    Sua idade atual ou a completar este ano é: 33 anos.
"""

# Desenvolva o seu código abaixo:

print("\n")
print("------ Identificador de Idade -------",end="\n")
print("Seja Bem Vindo ao Programa que identificará a sua idade!")
print("--------------------------------------------------------",end="\n")

ano_nascimento=int(input("Em Qual Ano você Nasceu? "))
ano_atual=2026 #Não utilizaremos bibliotecas de sistemas para pegar o ano atual.

idade = ano_atual - ano_nascimento

print(f"Olá, a sua idade é: {idade} anos")
print("--------------------------------------------------------",end="\n")
