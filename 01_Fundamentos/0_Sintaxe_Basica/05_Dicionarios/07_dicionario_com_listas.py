"""
DESAFIO 07: Boletim Escolar (Dicionário com Listas)

Nível: Intermediário
Objetivo: Integrar estruturas de dados complexas armazenando listas dentro de chaves de dicionários.
Conceitos: Dicionários, listas como valores, indexação e cálculo de média.

Enunciado:
    Crie um dicionário chamado 'boletim' que contenha duas chaves: 'aluno' (recebendo o nome do estudante) 
    e 'notas' (recebendo uma lista com 3 notas float fornecidas pelo usuário).
    Após alimentar as estruturas, o programa deve:
    1. Recuperar a lista de notas de dentro do dicionário e calcular a média delas.
    2. Exibir o nome do aluno e sua média final formatada com 2 casas decimais.

Exemplo de Execução:
    Nome do Aluno: Victor
    Nota 1: 8.5
    Nota 2: 7.0
    Nota 3: 9.0
    --------------------------------------------------------
    O aluno Victor obteve a média final de: 8.17
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Boletim Escolar Avançado -------
Este script gerenciará notas armazenando uma lista dentro de um dicionário
--------------------------------------------------------""", end="\n")

# Dicionário mapeando Nome -> Lista de Notas (corrigido para usar : e vírgulas decimais com ponto)
boletim = {
    "Victor": [9.0, 7.8, 7.9], 
    "Jessica": [8.5, 8.7, 8.4],
    "Eros": [8.0, 7.4, 9.0]
}

print("---- Boletim ----")
pesquisar_nome = input("Favor Informar um Nome: ")

# Buscando o nome digitado na agenda de contatos/notas
boletim_resultado = boletim.get(pesquisar_nome, "Nome não Encontrado")

print("--------------------------------------------------------")

# Validando se o resultado da busca foi um sucesso (ou seja, retornou a lista de notas)
if boletim_resultado != "Nome não Encontrado":
    # boletim_resultado guarda a lista de notas (ex: [9.0, 7.8, 7.9])
    notas = boletim_resultado
    media = sum(notas) / 3
    
    print(f"O aluno {pesquisar_nome} obteve a média final de: {media:.2f}")
else:
    print(boletim_resultado)

print("--------------------------------------------------------")