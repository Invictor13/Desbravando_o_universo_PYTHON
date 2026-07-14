"""
Exercício 11: Registros Leves com NamedTuple
    Objetivo: Evoluir da tupla tradicional (acessada por índices confusos numéricos) para tuplas nomeadas, criando "mini-classes" imutáveis e legíveis.
    Conceitos: Módulo collections, namedtuple, declaração de moldes e acesso via ponto (objeto.atributo).

Enunciado:
    Importe a estrutura `namedtuple` do módulo nativo `collections`. 
    Crie um "molde" (a tupla nomeada) chamado `Carro` que exija três atributos: 'marca', 'modelo' e 'ano'.
    
    Utilizando esse molde, instancie dois carros diferentes. Ao final, imprima o nome do modelo do primeiro 
    carro e o ano do segundo carro. Acesse esses dados utilizando a sintaxe elegante de ponto (ex: carro.modelo), 
    provando que o código fica muito mais legível do que acessar por índices como carro[1].

Exemplo de Execução:
    > Sistema de Frota (NamedTuples)
    --------------------------------------------------------
    > Cadastro 1: Carro(marca='Honda', modelo='Civic', ano=2022)
    > Cadastro 2: Carro(marca='Toyota', modelo='Corolla', ano=2023)
    
    Acessos diretos:
    > O modelo do carro 1 é: Civic
    > O ano do carro 2 é: 2023
    --------------------------------------------------------
"""