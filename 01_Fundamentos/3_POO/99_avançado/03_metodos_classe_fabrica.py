 l"""
DESAFIO 03: Construtores Alternativos e Utilitários (@classmethod e @staticmethod)

Nível: Avançado (POO)
Objetivo: Compreender a diferença prática e os casos de uso de métodos vinculados à classe e métodos estáticos.
Conceitos: Decorador @classmethod (parâmetro 'cls'), decorador @staticmethod, Factory Pattern (Padrão Fábrica).

Enunciado:
    Desenvolva uma classe chamada 'Usuario' que possua os atributos 'nome' e 'perfil' (ex: "comum", "admin").
    Estruture os seguintes métodos especiais dentro da classe:
    1. Um método construtor tradicional (__init__).
    2. Um @classmethod chamado 'criar_administrador(cls, nome)': Esse método deve atuar como um construtor 
       alternativo (Factory), instanciando a classe automaticamente e definindo o perfil fixo como "admin".
    3. Um @staticmethod chamado 'validar_email(email)': Um método utilitário que recebe uma string e verifica 
       se ela possui um caractere '@'. Ele deve retornar True ou False e não depende de nenhuma instância da classe.

Exemplo de Execução:
    --------------------------------------------------------
    > Validando email de teste: True
    > Criando usuário através da Fábrica...
    > Usuário Criado: Victor | Perfil do Sistema: admin
--------------------------------------------------------
"""
# Desenvolva a sua classe e o código de teste abaixo: