"""
Exercício 06: Validador e Parser de URL e E-mail
    Objetivo: Fazer o parsing (extração limpa) de dados de uma URL sem usar bibliotecas externas.
    Conceitos: .startswith(), .endswith(), .find() e .index().

Enunciado:
    Crie um programa que faça a extração estruturada de dados. O programa deve receber 
    uma URL completa digitada pelo usuário e, utilizando exclusivamente métodos nativos de string, 
    separar e exibir:
        1. O protocolo (ex: http ou https).
        2. O domínio principal.
        3. Os parâmetros (tudo o que vier após o '?').
    
    Se a URL não começar com um protocolo válido, exiba uma mensagem de erro.

Exemplo de Execução:
    Digite uma URL: https://site.com/page?p=1
    --------------------------------------------------------
    Análise de URL:
    > Protocolo: https
    > Domínio: site.com/page
    > Parâmetros: p=1
    --------------------------------------------------------
"""

#Solicitando que um usuário insira um site:
site = input("Digite uma URL: ")

# [1] Extraindo o Protocolo
#   1. Obserseve que criamos uma variável e atribuimos o método find() com o parametro "://"
#   2. A variável fim_protocolo armazenará um inteiro, com a posição inicial do primeiro parametro encontrado.
#   2. Com valor em mãos em mãos, conseguimos criar a variável protocolo, delimitando o limite do corte
fim_protocolo = site.find("://")
protocolo = site[:fim_protocolo]

# [2] Extraindo o domínio e parâmetros:
#   1. Perceba que nossa busca possui 3 caracateres: "://"
#   2. Portanto, a variável inicio_resto deve somar + 3, para removermos a parte inicial do site

inicio_resto = fim_protocolo + 3
resto_da_url = site[inicio_resto:]

# [3] Separando o Dominio e Parâmetros
#   1. Encontrando a posição "?" na variável resto_da_url 

posicao_interrogacao = resto_da_url.find("?")

# [4] Fatiamento Linear: O domínio vai do início até a "?" os parâmetros começam após até o fim
dominio = resto_da_url[:posicao_interrogacao]
parametros = resto_da_url[posicao_interrogacao +1:]

# [5] Exibindo a saída
print(f"""--------------------------------------------------------
      Análise de URL
> Protocolo: {protocolo}
> Domínio: {dominio}
> Parâmetros: {parametros}
--------------------------------------------------------""")




"""

# 3. Separando Domínio e Parâmetros
# Encontramos a posição da interrogação "?" no que sobrou da string
posicao_interrogacao = resto_da_url.find("?")

# Fatiamento linear: o domínio vai do início até a "?" e os parâmetros vão de depois da "?" até o fim
dominio = resto_da_url[:posicao_interrogacao]
parametros = resto_da_url[posicao_interrogacao + 1:]

# Exibição dos resultados formatados
print("--------------------------------------------------------")
print("Análise de URL:")
print(f"> Protocolo: {protocolo}")
print(f"> Domínio: {dominio}")
print(f"> Parâmetros: {parametros}")
print("--------------------------------------------------------")

"""
