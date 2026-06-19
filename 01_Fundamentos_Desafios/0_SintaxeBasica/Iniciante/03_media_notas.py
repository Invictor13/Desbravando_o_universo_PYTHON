"""
DESAFIO 03: Operadores Práticos e Médias

Nível: Iniciante
Objetivo: Utilizar operadores aritméticos básicos e formatação de casas decimais.
Conceitos: Entrada de dados flutuantes (float), precedência de operadores e formatação de saída.

Enunciado:
    Desenvolva um script que receba 3 notas de um aluno (valores decimais), 
    calcule a média aritmética entre elas e exiba o resultado formatado 
    com exatamente duas casas decimais.

Exemplo de Execução:
    Digite a primeira nota: 7.5
    Digite a segunda nota: 8.0
    Digite a terceira nota: 6.5
    A média final do aluno é: 7.33
"""

# Desenvolva o seu código abaixo:

print("\n")
print("------ Média Aritmética -------",end="\n")
print("Seja Bem Vindo ao Programa que calculará a média das suas notas!")
print("--------------------------------------------------------",end="\n")

primeira_nota = float(input("Favor informar o valor da primeira nota: "))
segunda_nota = float(input("Favor informar o valor da segunda nota: "))
terceira_nota = float(input("Favor informar o valor da terceira nota: "))

media = (primeira_nota + segunda_nota + terceira_nota)/3
print("--------------------------------------------------------",end="\n")
print(f"Média das Notas: {media:.2f}") #Exibindo apenas dois números Significativos
print("--------------------------------------------------------",end="\n")