"""
DESAFIO 06: Minha Agenda de Contatos

Nível: Intermediário
Objetivo: Manipular dicionários usando métodos de busca para simular uma agenda telefônica.
Conceitos: Dicionários, busca por chaves, método get() ou verificação com o operador 'in'.

Enunciado:
    Crie um dicionário pré-populado com 3 nomes de amigos e seus respectivos telefones (ex: {'Ana': '9999-9999'}).
    O script deve solicitar que o usuário digite o nome de um amigo para buscar o telefone na agenda.
    1. Se o nome existir no dicionário, exiba o número de telefone correspondente.
    2. Se o nome não for encontrado, exiba a mensagem: "Contato não localizado na agenda."

Exemplo de Execução:
    Digite o nome para buscar na agenda: Ana
    --------------------------------------------------------
    Telefone de Ana: 9999-9999
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Agenda de Contatos Básica -------
Este script buscará números de telefone mapeados dentro de um dicionário
--------------------------------------------------------""", end="\n")

# Cada par chave:valor representa um contato completo na agenda
contatos = {
    "Ana": "9999-9999",
    "Victor": "8888-8888",
    "Jessica": "7777-7777"
}

consultar_nome = input("Digite o nome para buscar na agenda: ")
print("--------------------------------------------------------")

# Usando o método .get() para buscar o nome informado. 
# Se não achar, ele já retorna a mensagem padrão do enunciado.
resultado = contatos.get(consultar_nome, "Contato não localizado na agenda.")

# Se o resultado for diferente da mensagem de erro, significa que o contato existe!
if resultado != "Contato não localizado na agenda.":
    print(f"Telefone de {consultar_nome}: {resultado}")
else:
    print(resultado)

print("--------------------------------------------------------")