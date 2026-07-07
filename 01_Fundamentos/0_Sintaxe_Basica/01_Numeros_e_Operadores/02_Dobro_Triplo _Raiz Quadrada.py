"""
Exercicio 02: Dobro, Triplo e Raiz Quadrada

    01) Objetivo: Explorar os operadores aritméticos de multiplicação e potenciação.
    02) Conceitos: Multiplicação, operador de potência (**) ou raiz quadrada por expoente fracionário (0.5).

Enunciado:
    - Crie um algoritmo que leia um número inteiro do usuário e mostre na tela o seu dobro, o seu triplo 
    e a sua raiz quadrada.

Exemplo de Execução:
--------------------------------------------
    Digite um número: 9
    O dobro de 9 é: 18
    O triplo de 9 é: 27
    O número elevado ao quadrado: 81
    A raiz quadrada de 9 é: 3.0
--------------------------------------------
"""

# Para imprimir valores com mais de uma linha, utilize aspas triplas print(""" """)
print("""
             ------ Dobro, Triplo e Raiz Quadrada -------
Este Script mostrará o dobro, triplo e a raiz quadrada de um número
--------------------------------------------------------""", end="\n")

n = int(input("Favor informar um número inteiro: "))

# Para multiplicar valores, utilize "*".             Saída : 3*2 = 6
# Para criar uma potência, utilize "**"              Saída : 3² = 9
#Para uma raiz quadrada, utilize "**" por 0.5        Saída : 9^0.5 = 3
n_dobro = n * 2
n_triplo = n * 3
n_quadrado = n ** 2
n_raizquadrada = n ** 0.5

print("--------------------------------------------------------",end="\n")
print(f"""
    1- Valor Digitado: {n}
    2- O dobro de {n} = {n_dobro}
    3- O triplo de {n} = {n_triplo}
    4- {n}² = {n_quadrado}
    5- A Raiz Quadrada de {n} = {n_raizquadrada:.2f} 
      """)
print("--------------------------------------------------------",end="\n")