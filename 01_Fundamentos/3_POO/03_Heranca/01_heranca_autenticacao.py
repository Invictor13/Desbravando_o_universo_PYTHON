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

#Classe mãe
class Usuario():
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def exibir_perfil(self):
        print(f"""
--------------------------------------------------------
    Perfil do Usuário:
    > Nome: {self.nome} | Email: {self.email}
--------------------------------------------------------""")

#Classe Filha
class Administrador(Usuario):
    def __init__(self, nome, email, nivel_acesso):
        # O super() chama o __init__ da classe Usuario para lidar com nome e email
        super().__init__(nome, email)

        # O Administrador inicializa apenas o seu atributo exclusivo
        self.nivel_acesso = nivel_acesso
    
    def exibir_perfil(self):
        print(f"""
--------------------------------------------------------
    Perfil do Admin:
    > Nome: {self.nome} | Email: {self.email}
    > Nível de Acesso: {self.nivel_acesso}
--------------------------------------------------------""")

usuario1 = Administrador("Victor","victor@email.com","Admin Master")
usuario1.exibir_perfil()

usuario2 = Usuario("Eros","eros@email.com")
usuario2.exibir_perfil()