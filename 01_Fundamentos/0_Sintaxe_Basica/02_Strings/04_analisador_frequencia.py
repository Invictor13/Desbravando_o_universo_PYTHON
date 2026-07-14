"""
Exercicio 04: Analisador Estático de Nomes

    1) Objetivo: Explorar os métodos embutidos de strings para análise de dados textuais.
    2) Conceitos: Métodos de string (.upper, .lower, .strip, .replace), contagem com len() e indexação.

Enunciado:
    -Crie um programa que leia o nome completo de uma pessoa (com espaços) e, utilizando 
    apenas manipulação de strings e funções básicas, exiba:
        1. O nome com todas as letras maiúsculas e todas minúsculas.
        2. Quantas letras ao todo o nome possui (sem considerar os espaços internos).
        3. Quantas letras tem apenas o primeiro nome da pessoa.

Exemplo de Execução:

--------------------------------------------------------
 Digite seu nome completo: Victor Viana
--------------------------------------------------------
    Análise de Sintaxe de Texto:
    > Em Maiúsculas: VICTOR VIANA
    > Em Minúsculas: victor viana
    > Total de letras (sem espaços): 11
    > Letras no primeiro nome: 6
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Analisador Estático de Nomes -------
Este script destrinchará uma string usando métodos nativos do Python
--------------------------------------------------------""", end="\n")
nome = input("Informe o seu nome: ")

#Transformando em Maiúsculo e Minúsculo:
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()

#Retirando os espaços do nome e realizando a contagem:
nome_sem_espaço = nome.replace(" ","")
total_letras = len(nome_sem_espaço)

#Fatiando o Nome completo, através da criação de lista separada por espaço.
nome_fatiado = nome.split()
total_primeironome = len(nome_fatiado[0])

print("Nome em Maiúsculo: ",nome_maiusculo)
print("Nome em Minúsculo: ",nome_minusculo)
print("Total de Letras: ",total_letras)
print("Total de Letras do Primeiro Nome: ",total_primeironome)

