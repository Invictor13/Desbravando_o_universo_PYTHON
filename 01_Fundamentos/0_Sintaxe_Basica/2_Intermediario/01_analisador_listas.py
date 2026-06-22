"""
DESAFIO 01: Analisador de Listas Dinâmico

Nível: Intermediário
Objetivo: Praticar manipulação básica de listas e funções embutidas.
Conceitos: Entrada de dados, métodos de lista (append), funções max(), min() e sum().

Enunciado:
    Crie um script que receba 5 números inteiros do usuário (um por um) e 
    armazene-os em uma lista. Em seguida, exiba na tela:
    1. A lista na ordem exata em que os valores foram digitados.
    2. A lista organizada de forma crescente.
    3. A soma total de todos os elementos da lista.
    4. O maior e o menor valor digitado.

Exemplo de Execução:
    Digite o 1º número: 7
    Digite o 2º número: 2
    Digite o 3º número: 10
    Digite o 4º número: 5
    Digite o 5º número: 1
    --------------------------------------------------------
    Lista original: [7, 2, 10, 5, 1]
    Lista ordenada: [1, 2, 5, 7, 10]
    Soma dos valores: 25
    Maior valor: 10 | Menor valor: 1
"""
"""
DESAFIO 01: Analisador de Listas Estático

Nível: Iniciante
Objetivo: Praticar manipulação básica de listas sem laços de repetição.
Conceitos: Entrada de dados sequencial, criação de listas e funções max(), min() e sum().

Enunciado:
    Crie um script que receba 5 números inteiros do usuário (um por um) e 
    armazene-os em uma lista. Em seguida, exiba na tela:
    1. A lista na ordem exata em que os valores foram digitados.
    2. A lista organizada de forma crescente.
    3. A soma total de todos os elementos da lista.
    4. O maior e o menor valor digitado.

Exemplo de Execução:
    Digite o 1º número: 7
    Digite o 2º número: 2
    Digite o 3º número: 10
    Digite o 4º número: 5
    Digite o 5º número: 1
    --------------------------------------------------------
    Lista original: [7, 2, 10, 5, 1]
    Lista ordenada: [1, 2, 5, 7, 10]
    Soma dos valores: 25
    Maior valor: 10 | Menor valor: 1
"""

#Atenção, não utilizamos laços de repetição neste exercício. Pois o conceito será estudado em outro módulo. 
# Desenvolva o seu código abaixo:
print("""
             ------ Analisador de Listas -------
Este script coletará 5 números e trará estatísticas sobre a lista
--------------------------------------------------------""", end="\n")

# Coleta dos dados de forma sequencial
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
n3 = int(input("Digite o 3º número: "))
n4 = int(input("Digite o 4º número: "))
n5 = int(input("Digite o 5º número: "))

# Criando a lista diretamente com as variáveis
lista = [n1, n2, n3, n4, n5]

print("--------------------------------------------------------")
print(f"Lista original: {lista}")
print(f"Lista ordenada: {sorted(lista)}")
print(f"Soma dos valores: {sum(lista)}")
print(f"Maior valor: {max(lista)} | Menor valor: {min(lista)}")
print("--------------------------------------------------------")