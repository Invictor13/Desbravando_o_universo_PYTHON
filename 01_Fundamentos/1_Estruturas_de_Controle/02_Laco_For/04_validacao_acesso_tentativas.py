"""
DESAFIO 04: Bloqueio de Segurança por Tentativas Excedidas

Nível: Avançado (Estruturas de Controle)
Objetivo: Controlar um loop de autenticação limitando as interações para mitigar ataques de força bruta.
Conceitos: Laço while, contadores de tentativas, break para saída de sucesso, condicionais combinadas.

Enunciado:
    Desenvolva um sistema de portaria eletrônica que valide uma senha de acesso (ex: "AcessoVIP2026").
    O usuário tem direito a no máximo 3 tentativas para acertar a senha.
    - Se ele digitar a senha correta, exiba "Acesso Liberado! Seja bem-vindo." e interrompa o loop (break).
    - Se ele errar, avise quantas tentativas ele ainda tem restantes e continue o loop.
    Caso ele erre as 3 vezes seguidas, o programa deve encerrar exibindo a mensagem "CONTA BLOQUEADA: Procure o administrador do sistema."

Exemplo de Execução:
    Digite a senha de acesso: 1234
    Senha Incorreta! Você ainda tem 2 tentativas restantes.
    --------------------------------------------------------
    Digite a senha de acesso: abc
    Senha Incorreta! Você ainda tem 1 tentativa restante.
    --------------------------------------------------------
    Digite a senha de acesso: erro3
    --------------------------------------------------------
    ALERTA: Tentativas esgotadas. CONTA BLOQUEADA!
    --------------------------------------------------------
"""
# Desenvolva o seu código abaixo:

senha = "AcessoVIP2026"
tentativas = 2
print("-------- Seja Bem Vindo ---------")
for n in range(0,3):
    senha_user=input("Favor informar uma senha: ")
    if( senha_user == senha):
        print("""
-----------------------------------------
> Acesso Garantido.
> Seja Bem vindo
-----------------------------------------""")
    else:
        print(f"""
 -----------------------------------------
> Acesso Negado.
> você possui mais {tentativas} tentativa(s).
-----------------------------------------""")
    tentativas-=1
print("""
------------------------------------------------
> ALERTA: Tentativas esgotadas. CONTA BLOQUEADA!
------------------------------------------------""")