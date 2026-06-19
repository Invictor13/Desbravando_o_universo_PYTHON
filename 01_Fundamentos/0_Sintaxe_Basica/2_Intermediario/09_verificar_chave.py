"""
DESAFIO 09: Verificador de Permissões de Acesso

Nível: Intermediário
Objetivo: Validar a existência de chaves específicas em um dicionário de configurações.
Conceitos: Dicionários, operadores de associação ('in' / 'not in'), controle de fluxo básico.

Enunciado:
    Crie um dicionário chamado 'configuracoes' que represente o perfil de um usuário no sistema. 
    Ele deve conter as chaves: 'usuario', 'nivel_acesso' (ex: 'Admin', 'Estudante') e 'status' (ex: 'Ativo').
    O script deve pedir para o usuário digitar o nome de uma configuração que ele deseja checar 
    (ex: o usuário digita 'nivel_acesso' ou 'senha').
    1. Se a chave digitada existir no dicionário, exiba o valor armazenado nela.
    2. Se não existir, exiba a mensagem: "A configuração '[chave]' não foi encontrada no sistema."

Exemplo de Execução:
    Escolha uma configuração para checar: nivel_acesso
    --------------------------------------------------------
    A configuração 'nivel_acesso' está definida como: Admin
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Verificador de Configurações -------
Este script checará se uma chave de configuração existe no perfil do usuário
--------------------------------------------------------""", end="\n")