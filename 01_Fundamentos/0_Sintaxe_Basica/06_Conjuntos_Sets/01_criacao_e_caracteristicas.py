"""
Exercício 01: Criação e Características Únicas (Sets)
    Objetivo: Compreender a declaração de conjuntos (sets), a inserção de dados e a regra fundamental da unicidade.
    Conceitos: set(), método .add(), ignorar itens duplicados e diferença visual para dicionários.

Enunciado:
    Crie um programa que inicialize um conjunto (set) totalmente vazio. Em seguida, solicite 
    que o usuário digite 5 nomes de frutas (uma por vez) e adicione-as ao conjunto. 
    
    Atenção: Instrua intencionalmente o usuário a digitar pelo menos uma fruta repetida durante o processo.
    
    Ao final, exiba na tela:
    1. O conjunto resultante (para provar que a fruta repetida foi contabilizada apenas uma vez).
    2. O tipo da variável (usando a função type()), para garantir que é um 'set' e não um 'dict'.

Exemplo de Execução:
    --- Cadastro de Frutas Únicas ---
    Digite a 1ª fruta: Maçã
    Digite a 2ª fruta: Banana
    Digite a 3ª fruta: Maçã
    Digite a 4ª fruta: Uva
    Digite a 5ª fruta: Laranja
    --------------------------------------------------------
    Análise do Conjunto:
    > Frutas cadastradas: {'Maçã', 'Banana', 'Uva', 'Laranja'}
    > Tipo da estrutura: <class 'set'>
    --------------------------------------------------------
"""