"""-------------------------------------------------------------------------------------------------------------------------
|                                       Projeto DIO - Sistema Bancário 0.5                                                  |              
                                                                          
    Entendendo o Desafio:
        1 - Criar um sistema Bancário com operações de Saque, depósito e visualização de extrato
        2 - O cliente deve realizar apenas 3 saques por dia, com um valor máximo de R$ 500,00 por saque.
        3 - O extrato deve listar todas as operações realizadas na conta assim como o horário e data.

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

        [Datetime]
        [1.3.1] Essa biblioteca possui a função de fornecer: Data e Hora

-----------------------------------------------------------------------------------------------------------------------"""
import os
from datetime import datetime


def limpar_tela():
    # Verifica se o sistema é Windows ('nt')
    if os.name == 'nt':
        os.system('cls')
    # Caso contrário, assume que é Linux/Mac ('posix')
    else:
        os.system('clear')

l= "-"*60
l_t="-"*20
banco = True



"""---------------------------------- [2] Dicionário para Cadastrar os Clientes ----------------------------------------------------

        [Modelagem Relacional de Dados]
        [2.1] banco_de_clientes: Utiliza chaveamento exclusivo por "login" (nome.sobrenome), guardando dados de perfil.
        [2.2] banco_de_conta_corrente: Utiliza chaveamento por número sequencial inteiro (ID da Conta). 
        [2.3] Faz um vínculo lógico através do campo "Usuário", apontando para o login correspondente no banco de clientes.
        
        [Alerta Sobre a Segurança dos Dados]
        [2.4] NUNCA COLOQUE DADOS SENSÍVEIS DIRETAMENTE NO CÓDIGO!
        [2.5] Apesar de ter informado a senha dentro do .py, a intenção é mostrar o funcionamento do banco.
        [2.6] NOVAMENTE, NUNCA UTILIZE DADOS SENSÍVEIS OU SENHAS DENTRO DO SEU SCRIPT!!!!!!!!!!

-------------------------------------------------------------------------------------------------------------------------"""
banco_de_conta_corrente = {

    1 : {"Agencia":"0001",
         "Usuário": "victor.viana"                 
        }

    
}

banco_de_clientes = {
"victor.viana" : {  "Nome": "Victor Ladislau Viana",
                    "Senha": "123", 
                    "Saldo": 1000.00,
                    "Extrato": [], 
                    "Saques_Hoje": 0,
                    "Ultimo_Saque_Data":"",
                    "CPF": 12312312312,
                    "Endereço": "Rua Pedro Eugênio de Oliveira, Bonfim, Angra dos Reis - RJ"}  
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
        [4.2] O nome completo do usuário é divido pelo "espaço" para criar os elementos da lista automatizando o login.
        
        [Validação Antiduplicidade por CPF]
        [4.3] Como o dicionário é indexado por login, uma busca direta 'in' não mapearia CPFs existentes nas subchaves.
        [4.4] Para mitigar isso, estruturamos um laço de repetição utilizando '.values()' que varre os perfis cadastrados,
        [4.5] Comparando o valor em formato string para bloquear cadastros duplicados com o mesmo documento.

        [Gerador Automático e Sequencial de Contas]
        [4.6] Após consolidar o perfil do cliente, a função acessa o dicionário 'banco_de_conta_corrente'.
        [4.7] Através do método 'max(keys()) + 1', o sistema identifica o último número de conta gerado e incrementa
        [4.8] Automaticamente o próximo dígito de forma sequencial, mantendo a amarração com a Agência padrão "0001".

-------------------------------------------------------------------------------------------------------------------------"""


def cadastrar_cliente(nome):
    cpf_valido = 0
    quebrar_nome = nome.lower().split()
    # Prevenção de erro para quem digita apenas um nome
    if len(quebrar_nome) == 1:
        login_user = quebrar_nome[0]
    else:
        login_user = quebrar_nome[0] + "." + quebrar_nome[-1]
        
    nome_completo = nome.title()

    print(f"""
{l_t} Cadastrando a Conta {l_t}
Olá {login_user}, informe o seu endereço, seguindo o padrão:
EX: Rua, Bairro, Cidade - Estado
{l}
          """)
    endereço_user = input("> Endereço: ")
    senha_user = input("> Favor Informar uma senha: ")
    
    while cpf_valido == 0:   
        cpf_user = input("> Informe seu CPF(Apenas Números): ")
        
        # Cria uma flag para identificar se encontrou o CPF duplicado
        cpf_duplicado = False
        
        # Varre todos os clientes cadastrados procurando pelo CPF digitado
        for cliente in banco_de_clientes.values():
            # Convertemos para string caso o CPF na base esteja salvo como número
            if str(cliente.get("CPF")) == cpf_user:
                cpf_duplicado = True
                break
        
        if cpf_duplicado:
            print("[Atenção] Este CPF já está cadastrado em outra conta!")
        else:
            cpf_valido = 1

    novo_cliente = {
        "Nome" : nome_completo,
        "Login" : login_user,
        "Senha" : senha_user,
        "Saldo" : 0.0,
        "Status" : "Ativo",
        "Extrato": [], 
        "Saques_Hoje": 0,
        "Ultimo_Saque_Data":"",
        "CPF" : cpf_user,
        "Endereço" : endereço_user
    }

    limpar_tela()
    print(f"""
{l_t} Cadastro Concluído {l_t}

Olá {login_user},
Seja Bem vinda ao nosso banco!

{l}         
          """)
    continuar = input("Pressione qualquer tecla para continuar...")
   
   # O PULO DO GATO: Inserindo o cliente no banco de dados principal
    banco_de_clientes[login_user] = novo_cliente

    # --- GERADOR SEQUENCIAL DE CONTA CORRENTE ---
    agencia_padrao = "0001"
    
    # Se o banco de contas estiver vazio, começa com a conta 1. 
    # Caso contrário, pega a maior chave atual (última conta) e soma 1.
    if not banco_de_conta_corrente:
        nova_conta = 1
    else:
        nova_conta = max(banco_de_conta_corrente.keys()) + 1
    
    # Salva a nova conta vinculada ao login do usuário
    banco_de_conta_corrente[nova_conta] = {
        "Agencia": agencia_padrao,
        "Usuário": login_user
    }

    limpar_tela()
    print(f"""
{l_t} Cadastro Concluído {l_t}

Olá {login_user},
Seja Bem-vinda ao nosso banco!
Sua Conta Corrente foi gerada: Ag: {agencia_padrao} | Conta: {nova_conta}

{l}         
          """)
    continuar = input("Pressione qualquer tecla para continuar...")
    return novo_cliente


"""--------------------- Processos Bancários -  Funcao acessando_a_conta()--------------------------------------------

        [Processos Bancários -  Funcao acessando_a_conta() ]
        [5.1] Essa etapa é a mais complexa, pois aqui mora o coração das funções do banco [saque,deposito e extrato]
        [5.2] Para fins de organização e controle, antes da abertura do laço de repetição, criamos variáveis chaves.
        [5.3] O laço de repetição While, aliado a função de limpar a tela, criam um menu dinâmico e organizado.
        [5.4] Idenpendente dos processos que ocorrerão, ele sempre disponibilizará o mesmo layout de maneira limpa.

        [Operação de Saque - Funcao sacar()]
        [5.5] Caso o colaborador selecione a oção 3, ele entrará em uma condicional dentro do laço de repetição.
        [5.6] Como anunciado no desafio a opção saque possui diversas Limites: Saques, valores e saldo.
        [5.7] Portanto, algumas condicionais foram criadas para atender essas restrições.
        [5.8] Até mesmo, para informar mensagens de erros personalizadas devido as restrições.
        
        [Operação Deposito - funcao depositar()]
        [5.9] De Maneira similar ao menu, o usuário conseguirá verificar quanto ele possui de saldo

        [Operação Extrato - funcao extrato()]
        [5.10] Declaramos duas listas para saque e deposito, para realizarmos esta etapa
        [5.11] Cada Operação de Saque e Deposito, um novo elemento é armazenado nestas listagens
        [5.12] Para sua visualização, criamos um laço de repetição for, para exibição por linha dos elementos da lista.

-------------------------------------------------------------------------------------------------------------------------"""

def acessando_a_conta(usuario_logado):
    escolha_user = 10
    horario_atual = datetime.now()
    msg_error=""

    while(escolha_user != 0):
        limite_saque = 3 - user_logado["Saques_Hoje"]
        print(f"""
{l_t} {user_logado["Nome"]} {l_t}
Seja bem Vindo, como podemos ajudar? 

Saques Hoje: {user_logado["Saques_Hoje"]}
Saldo Atual: (R$) {user_logado["Saldo"]}
Limite de Saques: {limite_saque}
{msg_error}

[3] Sacar
[2] Depositar
[1] Extrato
[0] Sair

{l_t}{[horario_atual.strftime("%d/%m/%Y - %H:%M")]}{l_t}
""")
        escolha_user = int(input("> Opção: "))
        if (escolha_user!=1) and (escolha_user!=2) and (escolha_user!=3) and (escolha_user!= 0):
            limpar_tela()
            msg_error = "[Atenção] Opção Inválida, tente Novamente!"  


        elif (escolha_user == 3 ):
            sacar(usuario_logado)


        elif (escolha_user == 2):
            depositar(usuario_logado)

        elif (escolha_user == 1):
            extrato(usuario_logado)

        elif (escolha_user == 0):
            limpar_tela()
            print(f"""
{l}
Sistema Encerrado, Obrigado pela preferência
{l}""") 

"""-------------------------------------- [6] Operação de Saque - Funcao sacar()----------------------------------------------
        [Operação de Saque - Funcao sacar()]
        [6.1] Caso o colaborador selecione a oção 3, ele entrará em uma condicional dentro do laço de repetição.
        [6.2] Como anunciado no desafio a opção saque possui diversas Limites: Saques, valores e saldo.
        [6.3] Portanto, algumas condicionais foram criadas para atender essas restrições.
        [6.4] Até mesmo, para informar mensagens de erros personalizadas devido as restrições.
-------------------------------------------------------------------------------------------------------------------------"""

def sacar(user_logado):
    
    agora = datetime.now()
    dia_atual = agora.strftime("%d/%m/%Y")
    horario_formatado = agora.strftime("%d/%m/%Y %H:%M:%S")

    
    if user_logado["Ultimo_Saque_Data"] != "" and user_logado["Ultimo_Saque_Data"] != dia_atual:
        user_logado["Saques_Hoje"] = 0  # Reseta o contador para o novo dia
    
    print(user_logado["Saques_Hoje"])
    limite_saque = 3 - user_logado["Saques_Hoje"]
    msg_error=""
    limpar_tela()

    print(f"""
{l_t} Opção Escolhida: Saque {l_t} 
Caro Cliente, 
você consegue realizar {limite_saque} saque(s) diário(s) de até R$ 500,00

Saldo Disponível: (R$) {user_logado["Saldo"]}
Saques Disponíveis: {limite_saque}

{l_t}{[horario_atual.strftime("%d/%m/%Y - %H:%M")]}{l_t}
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
        user_logado["Extrato"].append(f"[Saque][{horario_atual.strftime('%d/%m/%Y - %H:%M')}]: R$ {saque :.2f}")
        user_logado["Saldo"] = user_logado["Saldo"] - saque
        
        # Atualiza a data do último saque para a data de hoje e soma 1
        user_logado["Ultimo_Saque_Data"] = dia_atual
        user_logado["Saques_Hoje"] += 1

        print("Operação Realizada!")
        limpar_tela()


"""--------------------- [7] Operação Deposito - funcao depositar()--------------------------------------------

        [7.1] De Maneira similar ao menu, o usuário conseguirá verificar quanto ele possui de saldo

-------------------------------------------------------------------------------------------------------------------------"""

def depositar(user_logado):
    escolha_user = 10
    msg_error=""
    limpar_tela()
    print(f"""
{l_t} Depositar {l_t}
Caro Cliente, 
Você possui um Saldo Disponível de : (R$){user_logado["Saldo"]}

{l_t}{[horario_atual.strftime("%d/%m/%Y - %H:%M")]}{l_t}""")    
    
    deposito = float(input("> Valor do Deposito: "))
    user_logado["Extrato"].append(f"[Deposito][{horario_atual.strftime("%d/%m/%Y - %H:%M")}]: R$ {deposito :.2f}")
    user_logado["Saldo"] = user_logado["Saldo"] + deposito
    print("Operação Realizada!")
    limpar_tela()

"""--------------------- [8] Operação de Extrato -  Funcao extrato()--------------------------------------------
        
        [8.1] Declaramos duas listas para saque e deposito, para realizarmos esta etapa
        [8.2] Cada Operação de Saque e Deposito, um novo elemento é armazenado nestas listagens
        [8.3] Para sua visualização, criamos um laço de repetição for, para exibição por linha dos elementos da lista.

-------------------------------------------------------------------------------------------------------------------------"""

def extrato(user_logado):
    escolha_user = 10
    limite_saque = 3
    msg_error=""
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


"""------------------------------------------- [9] Menu Inicial -------------------------------------------------
    [Primeira Tela a ser exibida]
    [9.1] Esta é a primeira tela a ser exibida ao usuário.
    [9.2] As opções de acesso, indicam qual função deverá ser acessada para prosseguirmos com o processo.

    [Mensagem de Encerramento por Tentativas]
    [9.3] Existe uma mensagem de encerramento personalizada, caso o acesso seja bloqueado

-------------------------------------------------------------------------------------------------------------"""

while banco == True:
    horario_atual = datetime.now()
    limpar_tela()
    print(f"""
{l_t}Sistema Bancário{l_t}

Olá, 
seja bem vindo ao Banco Python ltda!

[1] Acessar Conta - Sou cadastrado
[2] Primeiro Acesso - Criar Conta
[0] Encerrar o Programa

{l_t}{[horario_atual.strftime("%d/%m/%Y - %H:%M")]}{l_t}
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
                contas_do_usuario = []
                
                # Varre o banco de contas procurando quais chaves têm o login deste usuário
                for numero_conta, dados_conta in banco_de_conta_corrente.items():
                    if dados_conta["Usuário"] == login_user:
                        contas_do_usuario.append(f"Agência: {dados_conta['Agencia']} | Conta Corrente: {numero_conta}")
                
                # Mostra as contas encontradas antes de entrar nas operações
                print(f"{l_t} Suas Contas Vinculadas {l_t}")
                if not contas_do_usuario:
                    print("Nenhuma conta corrente ativa encontrada para este perfil.")
                else:
                    for conta in contas_do_usuario:
                        print(conta)
                print(l)
                
                input("Pressione Qualquer Tecla para acessar o menu de operações...")
                limpar_tela()
                
                # Entra no menu de movimentação (sacar, depositar, etc)
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
