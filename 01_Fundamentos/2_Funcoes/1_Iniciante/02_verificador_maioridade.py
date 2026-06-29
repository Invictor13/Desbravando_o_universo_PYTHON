"""
DESAFIO 02: Verificador de Maioridade Legal

Nível: Iniciante (Funções)
Objetivo: Praticar estruturas condicionais internas à função com retornos booleanos.
Conceitos: Retorno booleano (True/False), condicionais (if/else), modularização.

Enunciado:
    Desenvolva uma função chamada 'eh_maior_de_idade(idade)' que receba a idade de uma pessoa.
    - Se a idade for maior ou igual a 18, a função deve retornar True.
    - Caso contrário, deve retornar False.
    Fora da função, capture a idade do usuário e, baseando-se no retorno da função, 
    exiba uma mensagem personalizada de "Acesso Liberado" ou "Acesso Negado".

Exemplo de Execução:
    Informe a sua idade: 17
    --------------------------------------------------------
    > Status: Acesso Negado (Usuário menor de idade).
--------------------------------------------------------
"""
# Desenvolva a sua função e o seu código abaixo:

def eh_maior_de_idade(idade):
    verificador_idade = (x>=18)
    return(verificador_idade)


print("------- Verificador de Idade --------")
x = int(input("Informe a sua idade:: "))
verificador = eh_maior_de_idade(x)

if (verificador == True):   
    print(f"""
----------------------------------------------------
> Status: Acesso Liberado ( Usuário Maior de Idade).
----------------------------------------------------
      """)

else:
    print(f"""
---------------------------------------------------
> Status: Acesso Negado ( Usuário Menor de Idade).
---------------------------------------------------
      """)    