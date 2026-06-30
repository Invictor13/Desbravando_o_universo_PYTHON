"""
DESAFIO 03: A Máquina do Tempo (Criando Datas)

Nível: Iniciante (Bibliotecas - Datetime)
Objetivo: Instanciar objetos de data específicos passados pelo usuário.
Conceitos: Construtor datetime(), passagem de argumentos inteiros.

Enunciado:
    Peça ao usuário para digitar um dia, um mês e um ano de nascimento (como números inteiros).
    Utilize o módulo datetime para criar um objeto de data com esses valores e exiba 
    esse objeto na tela para provar que o Python o reconheceu como uma data válida.

Exemplo de Execução:
    Digite o dia: 13
    Digite o mês: 3
    Digite o ano: 1993
    --------------------------------------------------------
    > Data registrada no sistema: 1993-03-13 00:00:00
    --------------------------------------------------------
"""

# Desenvolva o seu código abaixo:
from datetime import datetime

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

data_nascimento = datetime(ano, mes, dia)

print("-" * 56)
print(f"> Data registrada no sistema: {data_nascimento}")
print("-" * 56)