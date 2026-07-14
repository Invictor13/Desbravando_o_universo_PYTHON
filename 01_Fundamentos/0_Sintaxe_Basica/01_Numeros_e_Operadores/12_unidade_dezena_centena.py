"""
Exercicio 12: Quebrador de Números (Divisão Inteira e Resto)

    1) Objetivo: Aplicar os operadores matemáticos de divisão inteira (//) e resto (%) para isolar dígitos.
    2) Conceitos: Operadores aritméticos avançados, precedência e conversão de tipos.

Enunciado:
    - Faça um programa que leia um número inteiro de 100 a 999 (três dígitos) digitado pelo usuário.
    - Utilizando apenas operações matemáticas matemáticas puras (sem converter o número para string), 
      separe e exiba na tela: a Centena, a Dezena e a Unidade desse número.

Exemplo de Execução:
--------------------------------------------
    Digite um número entre 100 e 999: 582
--------------------------------------------
    Decomposição Matemática do Número 582:
    > Centena: 5
    > Dezena: 8
    > Unidade: 2
--------------------------------------------

Como resolver isso matematicamente?
    Para isolar a Centena, Dezena e Unidade sem usar texto, nós usamos os operadores de Divisão Inteira (//) e o 
    Resto da Divisão (%). Olha que lógica maneira:

        1.1) Unidade: Qualquer número resto da divisão por 10 (% 10) sobra exatamente o último dígito. 
        (Ex: $582 \div 10$ dá 58 e sobra 2).

        1.2) Dezena: Se dividirmos o número inteiro por 10 (// 10), pegamos os dois primeiros dígitos 
        (Ex: $582 // 10 = 58$). 

        1.3) Se pegarmos o resto disso por 10 (% 10), isolamos o do meio! 
        (Ex: $58 \div 10$ dá 5 e sobra 8).

        1.4) Centena: É só pegar a divisão inteira por 100 (// 100). 
        (Ex: $582 // 100 = \mathbf{5}$).
"""


print("""
             ------ Quebrador de Números Matemático -------
Este script isolará os dígitos de um número usando operadores aritméticos
--------------------------------------------------------""", end="\n")

n = int(input("Digite um número entre 100 e 999: "))

# A mágica da matemática pura aplicada ao Python:
unidade = n % 10
dezena = (n // 10) % 10
centena = n // 100

print("--------------------------------------------------------")
print(f"Decomposição Matemática do Número {n}:")
print(f"> Centena: {centena}")
print(f"> Dezena: {dezena}")
print(f"> Unidade: {unidade}")
print("--------------------------------------------------------")