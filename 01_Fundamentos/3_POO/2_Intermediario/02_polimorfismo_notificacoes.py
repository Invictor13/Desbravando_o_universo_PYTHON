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