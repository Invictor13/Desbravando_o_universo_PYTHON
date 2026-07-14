"""
Exercício 13: Contador de Palavras Únicas
    Objetivo: Simular uma ferramenta de análise de texto calculando palavras únicas e suas frequências[cite: 168].
    Conceitos: Limpeza de pontuações (., ,, !, ?), divisão de texto em palavras individuais e métodos de busca[cite: 168].

Enunciado:
    Crie um programa que receba um parágrafo longo. O sistema deve primeiro limpar 
    todas as pontuações comuns do texto. Em seguida, deve dividir o texto e calcular 
    quantas palavras únicas existem e a frequência que cada uma aparece[cite: 168].

Exemplo de Execução:
    Digite o texto: Python é incrível. Python é poderoso!
    --------------------------------------------------------
    > Total de palavras únicas: 4
    > Frequência:
      - python: 2
      - é: 2
      - incrível: 1
      - poderoso: 1
    --------------------------------------------------------
"""

# Entrada do usuário
texto = input("Digite o texto: ")

# 1. Padroniza o texto para minúsculas
texto_limpo = texto.lower()

# 2. Limpeza de pontuações comuns substituindo por um espaço vazio
pontuacoes = [".", ",", "!", "?"]
for pontuacao in pontuacoes:
    texto_limpo = texto_limpo.replace(pontuacao, "")

# 3. Divide o texto em uma lista de palavras individuais
palavras = texto_limpo.split()

# 4. Usa um dicionário para contar a frequência de cada palavra
frequencia = {}
for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1  # Incrementa se já existir
    else:
        frequencia[palavra] = 1   # Inicializa com 1 se for a primeira aparição

print("--------------------------------------------------------")
print(f"> Total de palavras únicas: {len(frequencia)}")
print("> Frequência:")
for palavra, contagem in frequencia.items():
    print(f"  - {palavra}: {contagem}")
print("--------------------------------------------------------")