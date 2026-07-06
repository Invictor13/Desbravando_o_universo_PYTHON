"""
DESAFIO 05: Gerenciador de Instância Única (Padrão Singleton via __new__)

Nível: Avançado (POO)
Objetivo: Dominar o ciclo de criação de objetos interceptando o método especial '__new__' para implementar um Singleton.
Conceitos: Método construtor primitivo (__new__), atributos de classe estáticos, reaproveitamento de instância.

Enunciado:
    Em arquitetura de software, o padrão Singleton garante que uma classe tenha APENAS UMA instância em toda a 
    execução do programa (útil para pools de conexão com bancos de dados ou gerenciadores de configuração).
    1. Crie uma classe chamada 'GerenciadorConexao'.
    2. Sobrescreva o método '__new__(cls, *args, **kwargs)'. A lógica interna deve verificar se uma variável 
       de classe privada (ex: '_instancia') já foi criada. Se não foi, use 'super().__new__(cls)' para criá-la 
       e guardá-la. Se já existia, retorne a instância antiga ignorando a criação de um novo objeto.
    3. Instancie a classe duas vezes (g1 e g2) e verifique se 'g1 is g2' retorna True.

Exemplo de Execução:
    g1 = GerenciadorConexao()
    g2 = GerenciadorConexao()
    --------------------------------------------------------
    > Endereço na Memória g1: 0x...
    > Endereço na Memória g2: 0x...
    > Ambas as variáveis apontam para o mesmo objeto? True
--------------------------------------------------------
"""
# Desenvolva a sua classe e o código de teste abaixo: