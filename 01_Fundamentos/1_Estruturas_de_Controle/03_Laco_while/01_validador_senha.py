"""
DESAFIO 01: Validador de Senha Consecutiva (Loop de Segurança)

Nível: Iniciante (Estruturas de Controle)
Objetivo: Controlar repetições baseadas em uma condição ativa usando o laço 'while'.
Conceitos: Condicional if/else, laço while, operadores de comparação (==, !=).

Enunciado:
    Crie um sistema de login simples que obrigue o usuário a digitar a senha correta para entrar.
    Defina uma variável interna com a senha padrão (ex: "Python2026").
    O programa deve pedir para o usuário digitar a senha. Se ele errar, exiba "Acesso Negado. Tente novamente."
    e continue repetindo a pergunta. Quando ele acertar, exiba "Acesso Permitido!" e encerre o script.

Exemplo de Execução:
    Digite a senha de acesso: 1234
    Acesso Negado. Tente novamente.
    --------------------------------------------------------
    Digite a senha de acesso: abc
    Acesso Negado. Tente novamente.
    --------------------------------------------------------
    Digite a senha de acesso: Python2026
    --------------------------------------------------------
    Acesso Permitido! Welcome back.
    --------------------------------------------------------
"""

# Desenvolva o seu código abaixo:

senha = "Python2026"
senha_user = "0"

while(senha_user != senha):
    senha_user = input("Digite a Senha de Acesso: ")
    if(senha_user != senha):
        print("Acesso Negado. Tente Novamente!")
    else:
        print("Acesso Permitido! Welcome Back!")
        

