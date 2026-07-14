"""
Exercício 09: Gerador de Slug para SEO
    Objetivo: Transformar títulos amigáveis de artigos em URLs válidas (slugs).
    Conceitos: .replace(), .strip(), .lower() e limpeza de pontuações.

Enunciado:
    Crie um script que receba o título de um artigo de blog digitado pelo usuário. O seu objetivo 
    é converter esse título em um "slug" (formato padronizado de URL). Para isso:
    1. Converta o texto inteiro para letras minúsculas.
    2. Remova pontuações indesejadas (como pontos de exclamação ou interrogação).
    3. Substitua todos os espaços em branco por hífens (-).
    4. Limpe hífens duplicados no texto final caso existam.

Exemplo de Execução:
    Digite o título do artigo: Aprenda Python em 10 Dias!
    --------------------------------------------------------
    Gerador de Slug SEO:
    > URL Gerada: aprenda-python-em-10-dias
    --------------------------------------------------------
"""

# Entrada do usuário
titulo = input("Digite o título do artigo: ")

# 1) Transformando tudo em minusculo: .lower()
slug = titulo.lower()
print(f"Transformando tudo em minusculo: {slug}")

# 2) Removendo as pontuações. replace("?"..."."...","...)
slug = slug.replace("!", "").replace("?", "").replace(".", "").replace(",", "")
print(f"Removendos os Pontos: {slug}")

# 2. Substitui espaços intermediários por hífens
slug = slug.replace(" ", "-").replace("--", "-")
print(f"Removendos os '-': {slug}")

# 3. Limpeza de hífens duplicados (caso o título tivesse espaços seguidos)
while "--" in slug:
    slug = slug.replace("--", "-")

print("--------------------------------------------------------")
print("Gerador de Slug SEO:")
print(f"> URL Gerada: {slug}")
print("--------------------------------------------------------")