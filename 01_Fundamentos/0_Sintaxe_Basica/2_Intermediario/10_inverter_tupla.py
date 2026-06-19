"""
DESAFIO 10: Inversor de Histórico

Nível: Intermediário
Objetivo: Praticar fatiamento avançado (slicing) para inverter a ordem de coleções imutáveis.
Conceitos: Tuplas, fatiamento com passos negativos [::-1], indexação.

Enunciado:
    Crie uma tupla contendo uma sequência de 5 passos ou históricos de ações (ex: "Passo 1", "Passo 2", ...).
    Como as tuplas são imutáveis, você não pode alterar a ordem dela diretamente. O script deve:
    1. Exibir a sequência original na tela.
    2. Utilizar a técnica de fatiamento de strings/tuplas para gerar uma NOVA tupla com a ordem completamente invertida.
    3. Exibir a nova tupla gerada na tela.

Exemplo de Execução:
    Histórico Original: ('Login', 'Abrir Pasta', 'Editar Código', 'Salvar', 'Fazer Commit')
    --------------------------------------------------------
    Histórico Invertido (Mais recente primeiro):
    ('Fazer Commit', 'Salvar', 'Editar Código', 'Abrir Pasta', 'Login')
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Inversor de Histórico -------
Este script gerará uma nova sequência imutável com a ordem dos itens invertida
--------------------------------------------------------""", end="\n")