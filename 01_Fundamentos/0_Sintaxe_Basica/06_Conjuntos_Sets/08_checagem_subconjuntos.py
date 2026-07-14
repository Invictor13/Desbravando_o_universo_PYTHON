"""
Exercício 08: Checagem de Subconjuntos (Permissões)
    Objetivo: Validar hierarquias estruturais garantindo que um grupo está totalmente contido em outro.
    Conceitos: Métodos .issubset() (está contido) e .issuperset() (contém).

Enunciado:
    Você está construindo um sistema de segurança.
    permissoes_admin = {"ler", "escrever", "deletar", "criar_usuario", "excluir_usuario"}
    permissoes_usuario_atual = {"ler", "escrever"}
    permissoes_hacker = {"ler", "derrubar_servidor"}
    
    Utilizando o método .issubset(), faça o sistema checar e responder (True ou False):
    1. As permissões do usuário atual são válidas dentro do escopo do admin?
    2. As permissões do hacker estão limitadas ao escopo do admin?

Exemplo de Execução:
    Verificando autorizações...
    --------------------------------------------------------
    > Usuário Atual tem permissões válidas? True
    > Hacker tem permissões válidas? False
"""