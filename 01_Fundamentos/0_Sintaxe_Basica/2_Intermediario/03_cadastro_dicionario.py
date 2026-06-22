"""
DESAFIO 03: Cadastro de Perfil de Usuário

Nível: Intermediário
Objetivo: Estruturar dados utilizando o conceito de chave e valor com dicionários.
Conceitos: Criação de dicionários, input de valores para chaves e f-strings com dicionários.

Enunciado:
    Desenvolva um programa que simule um formulário de cadastro. Peça ao usuário 
    que digite seu Nome, Idade, Cidade e Tecnologia Favorita. Armazene essas 
    informações em chaves correspondentes dentro de um único dicionário chamado 'usuario'. 
    No final, exiba uma frase formatada lendo os dados diretamente do dicionário.

Exemplo de Execução:
    Digite o Nome: Victor
    Digite ldade: 33
    Digite a Cidade: Angra dos Reis
    Digite a Tecnologia Favorita: Python
    --------------------------------------------------------
    Perfil Criado com Sucesso!
    O desenvolvedor Victor tem 33 anos, mora em Angra dos Reis e sua tecnologia favorita é Python.
"""

# Desenvolva o seu código abaixo:
# 1. Criamos as perguntas direto alimentando as chaves do dicionário
cadastro = {
    "nome": input("Favor informar o seu nome: "),
    "idade": int(input("Favor informar a sua idade: ")),
    "cidade": input("Favor informar a sua cidade: "),
    "tecnologia": input("Favor informar a sua tecnologia favorita: ")
}

print("--------------------------------------------------------")
print("Perfil Criado com Sucesso!")

# 2. Lendo os dados direto do dicionário usando f-string
print(f"O desenvolvedor {cadastro['nome']} tem {cadastro['idade']} anos, mora em {cadastro['cidade']} e sua tecnologia favorita é {cadastro['tecnologia']}.")
print("--------------------------------------------------------")