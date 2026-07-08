"""
DESAFIO 01: Analisador Estatístico de Listas

Nível: Intermediário (Funções)
Objetivo: Passar coleções dinâmicas como argumentos e retornar estruturas de dicionários.
Conceitos: Parâmetros de lista, funções embutidas (sum, max, min), retorno de dicionários (dict).

Enunciado:
    Desenvolva uma função chamada 'gerar_relatorio_numerico(lista_numeros)'.
    A função deve receber uma lista contendo múltiplos números inteiros ou floats e calcular:
    1. A média aritmética simples dos valores.
    2. O maior número presente.
    3. O menor número presente.
    A função deve RETORNAR esses três dados agrupados dentro de um dicionário com as chaves: 
    'media', 'maior' e 'menor'. Fora da função, passe uma lista de testes e exiba o dicionário resultante.

Exemplo de Execução:
    Lista de Teste: [10, 20, 30, 40, 50]
    --------------------------------------------------------
    > Relatório Processado: {'media': 30.0, 'maior': 50, 'menor': 10}
--------------------------------------------------------
"""
# Desenvolva a sua função e o seu código abaixo:

def gerar_relatorio_numerico(lista_numeros):
    media_lista = sum(lista_numeros)/len(lista_numeros)
    maior_numero = max(lista_numeros)
    menor_numero = min(lista_numeros)

    dicionario_personalizado = {
        'Media' : {media_lista},
        'Maior' : {maior_numero},
        'Menor' : {menor_numero}
    }
    return dicionario_personalizado


lista=[]
print("--------- Criando a Lista Personalizada -------------")
lista_tamanho = int(input("Informe o Tamanho da sua lista: "))
for i in range(1,lista_tamanho+1):
    n = int(input(f"[{i} de {lista_tamanho}]Favor Informar um número Inteiro: "))
    lista.append(n)
relatorio = gerar_relatorio_numerico(lista)
print(f"""
-------------------------------------------------------------------------
> Relatório Processado: {relatorio}
-------------------------------------------------------------------------
      """)