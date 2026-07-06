"""
DESAFIO 02: Disparador de Notificações Multicanal (Polimorfismo)

Nível: Intermediário (POO)
Objetivo: Aplicar o conceito de Polimorfismo, onde objetos diferentes respondem ao mesmo método de formas distintas.
Conceitos: Métodos com assinaturas idênticas, comportamento polimórfico, iteração de objetos em listas.

Enunciado:
    Crie uma classe base chamada 'Notificacao' com um método 'enviar(mensagem)'. Esse método base deve apenas 
    levantar um aviso genérico ou não fazer nada (pass).
    Crie duas subclasses:
    1. 'NotificacaoEmail': Onde o método 'enviar(mensagem)' exibe: "[E-mail] Enviando: X".
    2. 'NotificacaoSMS': Onde o método 'enviar(mensagem)' exibe: "[SMS] Enviando: X".
    Instancie um objeto de cada subclasse, guarde-os dentro de uma lista chamada 'servicos' e, utilizando 
    um laço 'for', faça com que todos disparem a mesma mensagem para ver o polimorfismo em ação.

Exemplo de Execução:
    --------------------------------------------------------
    Disparando notificações em lote...
    > [E-mail] Enviando: O sistema está atualizado!
    > [SMS] Enviando: O sistema está atualizado!
--------------------------------------------------------
"""
# Desenvolva as suas classes e o código de teste abaixo:

# Classe Base (Mãe)
class Notificacao:
    # O método base não precisa fazer nada, apenas definir a "regra"
    def enviar(self, mensagem):
        pass

# Subclasse 1: E-mail
class NotificacaoEmail(Notificacao):
    # Sobrescrita do método enviar com a mesma assinatura
    def enviar(self, mensagem):
        print(f"> [E-mail] Enviando: {mensagem}")

# Subclasse 2: SMS
class NotificacaoSMS(Notificacao):
    # Sobrescrita do método enviar com a mesma assinatura
    def enviar(self, mensagem):
        print(f"> [SMS] Enviando: {mensagem}")


# ==========================================
# ÁREA DE TESTES
# ==========================================

# 1. Instanciando os objetos de cada subclasse
email_service = NotificacaoEmail()
sms_service = NotificacaoSMS()

# 2. Guardando os serviços dentro de uma lista chamada 'servicos'
servicos = [email_service, sms_service]

# 3. Disparando a mesma mensagem para todos usando um laço for (Polimorfismo em ação!)
texto_notificacao = "O sistema está atualizado!"

print("-" * 56)
print("Disparando notificações em lote...")

for servico in servicos:
    # O Python decide em tempo de execução qual método chamar dependendo do objeto atual
    servico.enviar(texto_notificacao)

print("-" * 56)