"""
DESAFIO 04: Somador Dinâmico Avançado (*args)

Nível: Intermediário (Funções)
Objetivo: Dominar o conceito de empacotamento de argumentos variáveis usando a sintaxe *args.
Conceitos: Argumentos arbitrários (*args), iteração em tuplas geradas, fator multiplicador.

Enunciado:
    Crie uma função chamada 'somar_com_fator(fator, *numeros)'.
    A função deve aceitar obrigatoriamente um número como 'fator' e, logo em seguida, uma quantidade 
    indefinida de outros números (*args). A lógica interna deve somar todos os números passados no 
    *args e, no final, MULTIPLICAR o resultado da soma pelo valor do 'fator'. Retorne o total calculado.

Exemplo de Execução:
    Chamada: somar_com_fator(2, 5, 5, 5)  -> Soma (5+5+5=15) * Fator (2)
    --------------------------------------------------------
    > O resultado final calculado é: 30
--------------------------------------------------------
"""

# 1. Adicionado o '*' para capturar múltiplos argumentos
def somar_com_fator(fator, *numeros):
    # 2. Somamos a tupla de '*numeros' e multiplicamos pelo 'fator'
    resultado = sum(numeros) * fator
    
    # 3. Retornando o valor ao invés de printar
    return resultado

# --- Bloco do Usuário (Seu código visual mantido) ---
org_t = "-" * 10
org = "-" * 80

print(f"""        {org_t} Somar com Fator {org_t}
Informe os números que serão somados, separados por espaço:
{org} """)

numeros = [int(x) for x in input("Digite vários números separados por espaço: ").split()]
print("Sua lista de números:", numeros)

n_fator = int(input("Informe o Fator: "))

# 4. Chamando a função: 
# Passamos o fator primeiro. 
# O '*' antes de 'numeros' desempacota a lista para que a função a receba como múltiplos argumentos soltos.
resultado_final = somar_com_fator(n_fator, *numeros)

print("-" * 56)
print(f"> O resultado final calculado é: {resultado_final}")