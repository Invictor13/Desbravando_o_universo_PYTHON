"""
DESAFIO 09: Verificador de Permissões de Acesso (Menu Interativo)

Nível: Intermediário
Objetivo: Filtrar dados de usuários específicos acessando elementos de uma lista por meio de índices numéricos.
Conceitos: Dicionários com listas posicionais, método get(), menus interativos (int) e estruturas condicionais (if/elif).

Enunciado:
    Crie um dicionário chamado 'configuracoes' onde cada chave seja o nome de um usuário 
    e o valor seja uma lista contendo seu Nível de Acesso (índice 0) e seu Status (índice 1).
    O script deve solicitar o nome de um usuário para checar no sistema:
    1. Se o usuário não existir, exiba a mensagem: "Este Usuário Não Existe!"
    2. Se existir, apresente um menu numérico para o operador escolher entre:
       1 - Checar Perfil no Sistema (Nível de Acesso)
       2 - Verificar o Status (Ativo ou Inativo)
    3. Exiba a informação selecionada lendo a posição correta da lista retornada.

Exemplo de Execução:
    Informe o Nome do Usuário: victor
    --------------------------------------------------------
    --- Filtrando a Pesquisa ----
    ---- Usuário Identificado: Victor ----
    Favor informar uma opção(1-2):
    1 - Checar Perfil no Sistema
    2 - Verificar o status(Ativo ou Inativo)
    1
    --------------------------------------------------------
    Perfil no Sistema: Admin
    --------------------------------------------------------
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Verificador de Configurações -------
Este script checará se uma chave de configuração existe no perfil do usuário
--------------------------------------------------------""", end="\n")

configuracoes ={
    "Victor":["Admin", "Ativo"],
    "Jessica":["Estudante", "Ativo"],
    "Eros":["Estudante", "Inativo"],
}

print("---- Consultando Dados ---")
nome_consulta = input("Informe o Nome do Usuário: ")
pesquisa = configuracoes.get(nome_consulta,"Este Usuário Não Existe!")

if pesquisa != "Este Usuário Não Existe!":
    print(f"\n--- Filtrando a Pesquisa ----")

    permissao_checar = int(input(f"""
---- Usuário Identificado: {nome_consulta} ----
Favor informar uma opção(1-2):
1 - Checar Perfil no Sistema
2 - Verificar o status(Ativo ou Inativo)
    """))

    if(permissao_checar == 1):
        print(f"""
----------------------------------------------              
Perfil no Sistema: {pesquisa[0]}
----------------------------------------------  
""")
    elif(permissao_checar ==2):
        print(f"""
----------------------------------------------                
Status: {pesquisa[1]}
----------------------------------------------  
""")
