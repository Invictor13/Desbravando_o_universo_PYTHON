"""
Exercício 04: União de Assinantes
    Objetivo: Juntar dados de múltiplas fontes sem se preocupar em filtrar duplicatas manualmente.
    Conceitos: Teoria dos conjuntos, método .union() ou operador |.

Enunciado:
    Imagine que uma empresa tem duas listas de e-mails de clientes: 
    clientes_loja = {"ana@mail.com", "pedro@mail.com", "joao@mail.com"}
    clientes_blog = {"joao@mail.com", "maria@mail.com", "ana@mail.com"}
    
    O setor de marketing quer mandar um e-mail único para todos, sem enviar duplicado para 
    quem está nas duas listas. Utilize a operação de União de conjuntos para juntar 
    essas bases e exiba a lista final de e-mails.

Exemplo de Execução:
    Processando base de dados...
    --------------------------------------------------------
    > E-mails únicos para a campanha: {'maria@mail.com', 'pedro@mail.com', 'ana@mail.com', 'joao@mail.com'}
    > Total de disparos: 4
"""