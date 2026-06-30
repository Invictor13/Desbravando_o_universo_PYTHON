"""-------------------------------------------------------------------------------------------------------------------------
|                                       Projeto DIO - Sistema Bancário 0.1                                                  |              
                                                                          
    Entendendo o Desafio:
        1 - Criar um sistema Bancário com operações de Saque, depósito e visualização de extrato
        2 - O cliente deve realizar apenas 3 saques por dia, com um valor máximo de R$ 500,00 por saque.
        3 - O extrato deve listar todas as operações realizadas na conta

        OBS: A princípio não serão aplicados conceitos de Interfáce gráfica e nem Segurança de Dados
                                          
|                                Desenvolvedor: Invictor13 (Victor Ladislau Viana)                                          |



------------------------------- [1] Variáveis e Funções para Controle de Ambiente ------------------------------------

        [Organizadores]
        [1.1.1] Para Facilitar a utilização de um banco via console, organizei o design matemáticamente com o "-"
        [1.1.2] Deste Modo, o código ficará menos poluído e escalável com um método padrão
        [1.1.3] Organização para simbolos no titulo {l_t} Organização para todo resto {l}
        
        [Limpador de Tela]
        [1.2.1] A função limpa_tela foi uma sacada para organizar a navegação via console de maneira natural.
        [1.2.2] Em python não existe um método nativo, por isso, importamos a biblioteca 'os'
        [1.2.3] A função verifica o sistema operacional do usuário e aplica o método corresponte do terminal (cls ou clear)

-----------------------------------------------------------------------------------------------------------------------"""


l= "-"*60
l_t="-"*20
banco = True

import os
def limpar_tela():
    # Verifica se o sistema é Windows ('nt')
    if os.name == 'nt':
        os.system('cls')
    # Caso contrário, assume que é Linux/Mac ('posix')
    else:
        os.system('clear')

# Chamando a função para limpar o terminal
limpar_tela()


"""---------------------------------- [2] Dicionário para Cadastrar os Clientes ----------------------------------------------------

        [Organizando a Base de Dados]
        [2.1] Utilizamos um dicionário com um chaveamento por login (nome + último nome)
        
        [Alerta Sobre a Segurança dos Dados]
        [2.2] NUNCA COLOQUE DADOS SENSÍVEIS DIRETAMENTE NO CÓDIGO!
        [2.3] Apesar de ter informado a senha dentro do .py, a intenção é mostrar o funcionamento do banco.
        [2.4] Em atualizações Futuras, ensinarei a proteger dados sensíveis dos usuários da maneira CORRETA.
        [2.5] NOVAMENTE, NUNCA UTILIZE DADOS SENSÍVEIS OU SENHAS DENTRO DO SEU SCRIPT!!!!!!!!!!

-------------------------------------------------------------------------------------------------------------------------"""


banco_de_clientes = {
    "victor.viana" : {"Nome": "Victor Ladislau Viana", "Senha":"123", "Saldo": 1000.00, "Extrato": []}  
    }


""" ----------------------------- [3] Função para Autenticar o acesso do colaborador---------------------------------------------
        
        [Validando o Login]
        [3.1] A função autenticar_acesso possui um único parametro : login.
        [3.2] Seu ato inicial é tentar validar se o Login informado existe na nossa base de dados.
        [3.3] O usuário possui 3 tentativas para informar o login correto, antes de ser encerrado: range(0,3)

        [Coletando as informações de Acesso]
        [3.4] Através de uma nova variavel "cliente_atual", apenas as informações do login serão armazenadas
        
        [Validando a Senha]
        [3.5] Entretanto, antes do usuário receber qualquer informação armazenada ele deverá informar a senha da conta
        [3.6] Novamente, o usuário possuirá 3 tentativas para informar corretamente a senha solicitada.
        [3.7] Caso o processo seja um sucesso, ele retornará as informações coletadas em cliente_atual na etapa [3.4]

        [Tentativas excedidas]
        [3.8] Se o usuário não conseguir realizar o processo de autenticação o script retornará "False"
        [3.9] Deste Modo, o programa identificará que o processo falhou e por questões de segurança encerrará.

-------------------------------------------------------------------------------------------------------------------------"""


def autenticar_acesso(login):
    for i in range(0,3):
        if login in banco_de_clientes:
            cliente_atual = banco_de_clientes[login]
            print(f"""
{l}                
Olá {cliente_atual["Nome"]},
Identificamos a sua conta, para prosseguir informe a sua Senha!
{l}""")
            senha = input("> Senha:")
            for j in range(0,3):
                if( senha == cliente_atual["Senha"]):
                    print("Acesso Liberado")
                    limpar_tela()
                    return cliente_atual
                else:
                    limpar_tela()
                    print(f"""
                          
{l_t} [Atenção] {cliente_atual["Nome"]} {l_t}                        
Senha Incorreta! Tente Novamente...
Tentativas Restantes: {3-j}
{l}""")
                    senha = input("> Senha: ")     
            return False
        else:
            limpar_tela()
            print(f"""
{l_t} [Atenção] {l_t}
Usuário Não Encontrado. Favor tentar novamente!
Tentativas Restantes: {3-i}
{l}
                  """)
            login = input("> Login: ")
            limpar_tela()

    return False


"""--------------------------------------- [4] Função para Cadastrar um cliente:---------------------------------------------
        
        [Cadastrando um Cliente]
        [4.1] Utilizamos uma lista "quebrar_nome" que pega o nome completo do usuário e cria elementos de lista.
        [4.2] O nome completo do usuário é divido pelo "espaço" para criar os elementos da lista.
        [4.3] Deste modo, conseguimos automatizar o processo de criar login.
        [4.4] Será solicitado que o usuário cadastre uma senha e em seguida ele receberá outros parametros em seu cadastro.
        [4.4] Saldo, status e extrato, sã valores padrões para todos os usuários criados.

-------------------------------------------------------------------------------------------------------------------------"""


def cadastrar_cliente(nome):
    quebrar_nome = nome.lower().split()
    # Prevenção de erro para quem digita apenas um nome
    if len(quebrar_nome) == 1:
        login_user = quebrar_nome[0]
    else:
        login_user = quebrar_nome[0] + "." + quebrar_nome[-1]
        
    nome_completo = nome.title()

    senha_user = input("> Favor Informar uma senha: ")

    novo_cliente = {
        "Nome" : nome_completo,
        "Login" : login_user,
        "Senha" : senha_user,
        "Saldo" : 0.0,
        "Status" : "Ativo",
        "Extrato" : []
    }
    
    # O PULO DO GATO: Inserindo o cliente no banco de dados principal
    banco_de_clientes[login_user] = novo_cliente
    return novo_cliente


"""------------------------------------------------ [5] Acessando a Conta--------------------------------------------------

        [Processos Bancários]
        [5.1] Essa etapa é a mais complexa, pois aqui mora o coração das funções do banco [saque,deposito e extrato]
        [5.2] Para fins de organização e controle, antes da abertura do laço de repetição, criamos variáveis chaves.
        [5.3] O laço de repetição While, aliado a função de limpar a tela, criam um menu dinâmico e organizado.
        [5.4] Idenpendente dos processos que ocorrerão, ele sempre disponibilizará o mesmo layout de maneira limpa.

        [Operação de Saque - Opção 3]
        [5.5] Caso o colaborador selecione a oção 3, ele entrará em uma condicional dentro do laço de repetição.
        [5.6] Como anunciado no desafio a opção saque possui diversas Limites: Saques, valores e saldo.
        [5.7] Portanto, algumas condicionais foram criadas para atender essas restrições.
        [5.8] Até mesmo, para informar mensagens de erros personalizadas devido as restrições.
        
        [Operação Deposito - Opção 2]
        [5.9] De Maneira similar ao menu, o usuário conseguirá verificar quanto ele possui de saldo

        [Operação Extrato - Opção 1]
        [5.10] Declaramos duas listas para saque e deposito, para realizarmos esta etapa
        [5.11] Cada Operação de Saque e Deposito, um novo elemento é armazenado nestas listagens
        [5.12] Para sua visualização, criamos um laço de repetição for, para exibição por linha dos elementos da lista.

-------------------------------------------------------------------------------------------------------------------------"""


def acessando_a_conta(usuario_logado):
    escolha_user = 10
    limite_saque = 3
    msg_error=""

    while(escolha_user != 0):
        print(f"""
{l_t} {user_logado["Nome"]} {l_t}
Seja bem Vindo, como podemos ajudar? 

Saldo Atual: (R$) {user_logado["Saldo"]}
Limite de Saques: {limite_saque}
{msg_error}
{l}
[3] Sacar
[2] Depositar
[1] Extrato
[0] Sair
{l}""")
        escolha_user = int(input("> Opção: "))
        if (escolha_user!=1) and (escolha_user!=2) and (escolha_user!=3) and (escolha_user!= 0):
            limpar_tela()
            msg_error = "[Atenção] Opção Inválida, tente Novamente!"  


        elif (escolha_user == 3 ):
            limpar_tela()
            print(f"""
{l_t} Opção Escolhida: Saque {l_t} 
Caro Cliente, 
você consegue realizar {limite_saque} saque(s) diário(s) de até R$ 500,00

Saldo Disponível: (R$) {user_logado["Saldo"]}
Saques Disponíveis: {limite_saque}

{l}
""")
            saque = float(input("> Valor do Saque: "))
            if (saque > user_logado["Saldo"]):
                limpar_tela()
                print("[Atenção] Você não Possui Saldo Suficiente Para esta Operação: ")
            elif (saque > 500.00):
                limpar_tela()
                print("[Atenção] Valor Informado superior ao limite por saque : R$ 500,00")
            elif( limite_saque <= 0):
                limpar_tela()
                print("[Atenção] Você já realizou todos os saques diários disponíveis.")

            else:
                user_logado["Extrato"].append(f"[Saque]: R$ {saque :.2f}")
                user_logado["Saldo"] = user_logado["Saldo"] - saque
                limite_saque-=1
                print("Operação Realizada!")
                limpar_tela()


        elif (escolha_user == 2):
            limpar_tela()
            print(f"""
Caro Cliente, 
Você possui um Saldo Disponível de : (R$){user_logado["Saldo"]}""")
            deposito = float(input("> Valor do Deposito: "))
            user_logado["Extrato"].append(f"[Deposito]: R$ {deposito :.2f}")
            user_logado["Saldo"] = user_logado["Saldo"] + deposito
            print("Operação Realizada!")
            limpar_tela()

        elif (escolha_user == 1):
            limpar_tela()
            print(f"{l_t} Extrato Bancário {l_t}")
            # Checa se o extrato está vazio
            if not user_logado["Extrato"]:
                print("Não foram realizadas movimentações.")
            else:
                # Imprime operação por operação em ordem cronológica
                for operacao in user_logado["Extrato"]:
                    print(operacao)
                print(l)
                continuar = input("Pressione Qualquer Tecla, para continuar...") 
            limpar_tela()

        elif (escolha_user == 0):
            limpar_tela()
            print(f"""
{l}
Sistema Encerrado, Obrigado pela preferência
{l}""")




"""------------------------------------------- [6]Menu Inicial -------------------------------------------------
    [Primeira Tela a ser exibida]
    [6.1] Esta é a primeira tela a ser exibida ao usuário.
    [6.2] As opções de acesso, indicam qual função deverá ser acessada para prosseguirmos com o processo.

    [Mensagem de Encerramento por Tentativas]
    [6.3] Existe uma mensagem de encerramento personalizada, caso o acesso seja bloqueado

-------------------------------------------------------------------------------------------------------------"""

while banco == True:
    limpar_tela()
    print(f"""
{l_t}Sistema Bancário{l_t}
Olá, 
seja bem vindo ao Banco Python ltda!
{l}\n
[1] Acessar Conta - Sou cadastrado
[2] Primeiro Acesso - Criar Conta
[0] Encerrar o Programa
""")
    user_escolha = int(input("> Selecione uma Opção: "))
    limpar_tela()

    if(user_escolha != 1) and (user_escolha != 2) and (user_escolha != 0):
        print("Opção Inexistente, tente novamente.")
        print(user_escolha)

    else:  
    #Login   
        if(user_escolha == 1):
            print(f"""
{l_t} Olá Cliente {l_t}
Para Prosseguirmos com o acesso,
Favor informar o Seu login:
{l}""")
            login_user = input("> Login: ").lower()
            limpar_tela()
            user_logado = autenticar_acesso(login_user)
            if user_logado == False:
                limpar_tela()
                print(f"""
{l_t} [Atenção] {l_t}
Caro Cliente, não foi possível identificar suas credenciais.
Sessão Encerrada por Excesso de Tentativas
{l}""")
                banco = False

            else:
                acessando_a_conta(user_logado)



    # Processo para Cadastrar
        if(user_escolha == 2):
            print(f"""
{l_t} Olá Visitante {l_t}
Agradecemos o seu interesse pelo nosso banco.
Para prosseguirmos com o cadastro, informe seu nome completo:
{l}         
                """)
            nome_user = input("> Nome: ")
            novo_cliente = cadastrar_cliente(nome_user)
            print(f"""
{l_t} {novo_cliente['Login']} {l_t}
Nome Completo: {novo_cliente['Nome']}
Saldo Atual: {novo_cliente['Saldo']}
Status: {novo_cliente['Status']}

Cadastro Realizado com sucesso!
    {l}""")
        
        if(user_escolha == 0 ):
            print(f"""
{l_t} Olá Cliente {l_t}
Programa Encerrado,
Aguardaremos o seu retorno!
{l} """)
            banco = False
