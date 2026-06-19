"""
DESAFIO 04: Par ou Impar?

Nível: Iniciante
Objetivo: Trabalhar com operadores de resto (%) e operadores de comparação direta.
Conceitos: Operador módulo, expressões lógicas e retorno booleano direto (True/False).

Enunciado:
    Receba um número inteiro do usuário. Exiba na tela se o número é par 
    (o resto da divisão por 2 deve ser igual a 0) e, na linha seguinte, 
    se ele é maior que 10. O retorno de ambas as perguntas deve ser diretamente 
    em formato booleano (True ou False).

Exemplo de Execução:
    Digite um número inteiro: 12
    O número é par? True
    O número é maior que 10? True
"""

# Desenvolva o seu código abaixo:
print("\n")
print("------ Par ou Impar -------",end="\n")
print("Esse código verificará se o número é par ou impar")
print("--------------------------------------------------------",end="\n")

numero = int(input("Informe um número inteiro: "))
id_numero=numero%2

print("--------------------------------------------------------",end="\n")
print(f"O número é Par?", id_numero == 0)
print(f"O número {numero} é maior que 10?", id_numero > 10)
print("--------------------------------------------------------",end="\n")