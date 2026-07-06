"""
DESAFIO 03: Filtro e Contador de Números Pares

Nível: Iniciante (Estruturas de Controle)
Objetivo: Utilizar o laço 'for' combinado com intervalos numéricos e avaliações lógicas.
Conceitos: Laço for, função range(), operador módulo (%), contadores aritméticos (+=).

Enunciado:
    Crie um algoritmo que calcule a soma e conte quantos números pares existem em um intervalo dinâmico.
    O script deve pedir o Número Inicial (int) e o Número Final (int) desse intervalo.
    Utilizando o laço 'for', percorra esse intervalo (incluindo o número final), identifique os pares, 
    some-os e exiba o resultado consolidado.

Exemplo de Execução:
    Digite o início do intervalo: 1
    Digite o fim do intervalo: 10
    --------------------------------------------------------
    Análise do Intervalo (1 a 10):
    > Quantidade de números pares encontrados: 5
    > A soma total de todos os números pares é: 30
    --------------------------------------------------------
"""

# Desenvolva o seu código abaixo:

print(" ------------- Contador de Pares -----------------")
intervalo_inicial = int(input("Informe o Valor Inicial do Intervalo: "))
intervalo_final = int(input("Informe o Valor Final do Intervalo: "))
conta_par = 0
soma_par = 0

for n in range(intervalo_inicial,intervalo_final):
    if(n%2):
        conta_par+=1
        soma_par = soma_par + n

print(f"""
-----------------  Analise -----------------------
 Análise do Intervalo ({intervalo_inicial} a {intervalo_final}):
    > Quantidade de números pares encontrados: {conta_par}
    > A soma total de todos os números pares é: {soma_par}
---------------------------------------------------   
      """)
    