"""
Exercício 03: Fatiamento e Inversão de Textos
    
    1) Objetivo: Dominar a manipulação de índices em strings utilizando a sintaxe de slicing [início:fim:passo].
    2) Conceitos: Slicing, índices positivos e negativos, extração de subfrases e inversão de coleções.

Enunciado:
    Crie um programa que solicite ao usuário a digitação de uma frase completa (com pelo menos 15 caracteres). 
    A partir dessa frase, utilize exclusivamente o fatiamento (slicing) para exibir:

    1. Apenas os 5 primeiros caracteres da frase.
    2. Apenas os 5 últimos caracteres da frase.
    3. A frase inteira, mas saltando de 2 em 2 caracteres (trazendo apenas as posições pares).
    4. A frase completamente invertida (de trás para frente), ideal para checar palíndromos!

Exemplo de Execução:
    Digite uma frase (mínimo 15 caracteres): O Python é incrível demais!
    --------------------------------------------------------
    Análise de Fatiamento:
    > Primeiros 5 caracteres: O Pyt
    > Últimos 5 caracteres: mais!
    > Saltando de 2 em 2: OPto  nríeldmi!
    > Frase invertida: !siamed levírcni é nohtyP O
    --------------------------------------------------------
"""

frase_completa = input("Favor informar uma frase(min 15 caracteres): ")

print(f"""
----------------------------------------------------
Análise de Fatiamento:
> Primeiros 5 caracteres: {frase_completa[:5]}
> Últimos 5 caracteres: {frase_completa[-5:]}
> Saltando de 2 em 2: {frase_completa[::2]}
> Frase invertida: {frase_completa[::-1]}
---------------------------------------------------- 
      """)