"""
DESAFIO 05: Verificador de Coordenadas Geográficas

Nível: Intermediário
Objetivo: Utilizar tuplas para armazenar dados compostos e praticar desempacotamento (unpacking).
Conceitos: Tuplas, desempacotamento de variáveis, validação lógica simples.

Enunciado:
    Em sistemas de mapas (como GPS), a Latitude e a Longitude são guardadas juntas em estruturas 
    imutáveis. Crie um script que receba o valor da Latitude e da Longitude de um local.
    1. Salve esses dois valores decimais (float) dentro de uma única tupla chamada 'coordenadas'.
    2. Desempacote os valores da tupla em duas variáveis separadas: 'lat' e 'lon'.
    3. Exiba os valores desempacotados na tela formatados.

Exemplo de Execução:
    Digite a Latitude: -23.01
    Digite a Longitude: -44.31
    --------------------------------------------------------
    Coordenadas salvas com sucesso!
    Latitude registrada: -23.01°
    Longitude registrada: -44.31°
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Sistema de Coordenadas GPS -------
Este script empacotará e validará dados geográficos imutáveis
--------------------------------------------------------""", end="\n")