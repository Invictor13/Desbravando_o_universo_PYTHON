"""
DESAFIO 04: Verificador de Lista de Convidados (Portaria VIP)

Nível: Intermediário (Estruturas de Controle)
Objetivo: Interromper buscas em coleções assim que o objetivo for alcançado para poupar processamento.
Conceitos: Laço for, listas (strings), comando break, bandeiras lógicas (flags booleanas).

Enunciado:
    Crie uma lista contendo 5 nomes de convidados VIPs (ex: ['Victor', 'Jessica', 'Ana', 'Carlos', 'Mariana']).
    O script deve pedir para o operador da portaria digitar o nome de uma pessoa que acabou de chegar.
    Utilizando o laço 'for', percorra a lista para verificar se o nome está lá.
    - Se encontrar o nome, mude uma variável de controle para True e pare o loop na hora (break) — não há necessidade de continuar procurando.
    No final do programa, baseado na variável de controle, exiba se a entrada está liberada ou se a pessoa não foi convidada.

Exemplo de Execução:
    Nome do visitante na portaria: Jessica
    --------------------------------------------------------
    Procurando na lista VIP...
    > Usuário encontrado! Interrompendo busca...
    --------------------------------------------------------
    ENTRADA LIBERADA: Jessica é uma convidada VIP.
    --------------------------------------------------------
"""

# Desenvolva o seu código abaixo:

convidados = ['Victor', 'Jessica', 'Ana', 'Carlos', 'Mariana']

print("""-------------- Identificador de Convidados ------------------""")
nome_visitante = input("Favor Informar um Nome: ")
validador = False

print("--------------------------------------------------------")
print("Procurando na lista VIP...")

for nome in convidados:
    if nome.lower() == nome_visitante_lower():
        validador = True
        print("> Usuário encontrado! Interrompendo busca...")
        break

if validador:
    print(f"ENTRADA LIBERADA: {nome_visitante} é uma convidada VIP.")
else:
    print(f"ENTRADA NEGADA: {nome_visitante} não está na lista VIP.")
print("--------------------------------------------------------")
