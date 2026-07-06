"""
DESAFIO 02: Analisador Estatístico de Grupo

Nível: Avançado (Estruturas de Controle)
Objetivo: Acumular e cruzar múltiplos dados dinâmicos dentro de uma repetição para gerar relatórios complexos.
Conceitos: Laço for com range(), inputs de múltiplos tipos, acumuladores, contadores e comparadores de maior valor.

Enunciado:
    Escreva um programa que leia o Nome, Idade e Sexo (M/F) de 4 pessoas através de um laço de repetição.
    No final do processamento, o sistema deve calcular e gerar um relatório completo contendo:
    1. A média de idade exata do grupo.
    2. O nome e a idade do homem mais velho do grupo.
    3. Quantas mulheres cadastradas têm menos de 20 anos.

Exemplo de Execução:
    --- Cadastro 1/4 ---
    Nome: Victor
    Idade: 33
    Sexo (M/F): M
    ...
    --------------------------------------------------------
    Relatório Estatístico do Grupo:
    > Média de idade do grupo: 26.5 anos.
    > O homem mais velho é o Victor, que tem 33 anos.
    > Total de mulheres com menos de 20 anos: 1.
    --------------------------------------------------------
"""

# Desenvolva o seu código abaixo:
cadastro = []
total_idade = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

for i in range(4):
    print(f"--- Cadastro {i + 1}/4 ---")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()

    cadastro.append({'nome': nome, 'idade': idade, 'sexo': sexo})
    total_idade += idade

    if sexo == 'M':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            homem_mais_velho = nome
    elif sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media_idade = total_idade / 4
print('-' * 56)
print('Relatório Estatístico do Grupo:')
print(f'> Média de idade do grupo: {media_idade:.1f} anos.')
if homem_mais_velho:
    print(f'> O homem mais velho é o {homem_mais_velho}, que tem {idade_homem_mais_velho} anos.')
else:
    print('> Não há homens cadastrados no grupo.')
print(f'> Total de mulheres com menos de 20 anos: {mulheres_menos_20}.')
print('-' * 56)
