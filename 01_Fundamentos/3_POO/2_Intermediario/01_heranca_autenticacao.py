"""
DESAFIO 01: Sistema de Autenticação de Usuários (Herança)

Nível: Intermediário (POO)
Objetivo: Compreender a reutilização de código através de Herança simples entre classes.
Conceitos: Classe base (mãe), classe derivada (filha), palavra-chave super(), especialização.

Enunciado:
    Crie uma classe base chamada 'Usuario' que receba 'nome' e 'email' no construtor e possua 
    o método 'exibir_perfil()' para mostrar esses dados.
    Logo em seguida, crie uma subclasse chamada 'Administrador' que herde de 'Usuario'.
    O construtor do 'Administrador' deve receber 'nome', 'email' e um atributo específico 'nivel_acesso' (str).
    Use o método super() para alimentar os atributos da classe mãe e faça o override (sobrescrita) do 
    método 'exibir_perfil()' para que ele mostre também o nível de acesso do administrador.

Exemplo de Execução:
    --------------------------------------------------------
    Perfil do Usuário:
    > Nome: Victor Viana | Email: victor@email.com
    > Nível de Acesso: Admin Master
--------------------------------------------------------
"""
# Desenvolva as suas classes e o código de teste abaixo: