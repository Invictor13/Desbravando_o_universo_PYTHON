"""
DESAFIO 05: Orquestrador de Transformações (Funções como Cidadãs de Primeira Classe)

Nível: Avançado (Funções)
Objetivo: Tratar funções como variáveis comuns, passando uma lista de funções para serem executadas em sequência.
Conceitos: First-Class Functions, iteração sobre estruturas de funções, transformação linear de dados.

Enunciado:
    Em engenharia de dados, é comum passar dados por uma cadeia de funções independentes.
    Crie três funções simples:
    1. 'remover_espacos(texto)': Retorna a string limpa com .strip().
    2. 'caixa_alta(texto)': Retorna a string em .upper().
    3. 'adicionar_hashtag(texto)': Retorna a string com um '#' no início.
    
    Crie uma quarta função principal chamada 'orquestrar_transformacoes(texto, lista_funcoes)'.
    Ela deve receber a string e uma lista contendo as referências das três funções anteriores.
    Utilizando um laço, passe o texto sucessivamente por cada função da lista e retorne o resultado final consolidado.

Exemplo de Execução:
    Texto de Entrada: "   universo python   "
    Lista de Funções: [remover_espacos, caixa_alta, adicionar_hashtag]
    --------------------------------------------------------
    > Resultado da Orquestração de Dados: #UNIVERSO PYTHON
--------------------------------------------------------
"""
# Desenvolva as funções e a lógica de orquestração abaixo: