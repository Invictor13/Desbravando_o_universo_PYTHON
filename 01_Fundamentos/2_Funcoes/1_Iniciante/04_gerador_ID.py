"""
DESAFIO 04: Gerador Estático de ID de Usuário

Nível: Iniciante (Funções)
Objetivo: Manipular e concatenar strings dentro de uma função para padronização de dados.
Conceitos: Métodos de string (.lower, .strip), f-strings, concatenação de texto.

Enunciado:
    Desenvolva uma função chamada 'gerar_id_sistema(nome, ano_nascimento)'.
    A função deve limpar os espaços extras do nome, transformá-lo completamente em letras 
    minúsculas e concatenar com o ano de nascimento separado por um sublinhado (_).
    A função deve retornar a string do ID gerado.

Exemplo de Execução:
    Digite o seu nome:   Victor Viana   
    Digite o ano de nascimento: 1993
    --------------------------------------------------------
    > ID de Sistema Gerado: victor viana_1993
--------------------------------------------------------
"""
# Desenvolva a sua função e o seu código abaixo:

def gerar_id_sistema(nome, ano_nascimento):
    id_criacao = nome+"_"+ano_nascimento
    return id_criacao

print("-------- Gerador de ID ----------")
x = input("Informe seu Nome: ").lower().replace(" ","")
y = input("Digite o Ano de Nascimento: ").replace(" ","")
id_user = gerar_id_sistema(x,y)
print(f"""---------------------------------------------------------
> ID de Sistema Gerado:{id_user}
---------------------------------------------------------""")