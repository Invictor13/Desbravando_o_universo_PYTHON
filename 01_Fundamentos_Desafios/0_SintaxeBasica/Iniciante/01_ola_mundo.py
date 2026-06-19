"""
DESAFIO 01: Ola Mundo Personalizado

Nivel: Iniciante
Objetivo: Desenvolver seu primeiro script focado em interatividade basica.
Conceitos: Entrada (input), Saida (print) e Formatacao de Strings (f-strings).

Enunciado:
    Crie um programa que solicite ao usuario o seu primeiro nome. 
    Apos receber o dado, o script deve exibir na tela uma mensagem 
    de boas-vindas personalizada no formato exato:
    "Ola, [Nome], bem-vindo ao Universo Python!"

Exemplo de Execucao:
    Digite o seu primeiro nome: Victor
    Ola, Victor, bem-vindo ao Universo Python!
"""

# Desenvolva o seu codigo abaixo:
print("Ola, Seja Bem vindo.", end="\n")
nome = input("Por Favor, Informe o seu Nome: ")

print(f"Ola, {nome}, Seja Bem-Vindo ao Universo Python")