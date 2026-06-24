"""
DESAFIO 04: Associação de Objetos (Carrinho de Compras)

Nível: Intermediário (POO)
Objetivo: Compreender a relação de associação/composição, onde um objeto interage e armazena outros objetos.
Conceitos: Associação de classes, passagem de objetos como argumentos, agregação.

Enunciado:
    Para este desafio, você precisará estruturar duas classes:
    1. Classe 'Item': Possui os atributos de instância 'nome' e 'preco' (float).
    2. Classe 'CarrinhoDeCompras': Não recebe parâmetros no construtor, apenas inicializa um atributo 
       'lista_itens' como uma lista vazia [].
    A classe 'CarrinhoDeCompras' deve ter os métodos:
    - 'adicionar_item(objeto_item)': Recebe um OBJETO da classe 'Item' e o guarda na lista.
    - 'calcular_total()': Percorre a lista de objetos, soma o atributo 'preco' de cada item e retorna o valor total.

Exemplo de Execução:
    --------------------------------------------------------
    > Adicionando itens ao carrinho...
    > Item: Mouse Gamer (R$ 150.00) adicionado.
    > Item: Headset (R$ 250.00) adicionado.
    --------------------------------------------------------
    > Valor total do carrinho: R$ 400.00
--------------------------------------------------------
"""
# Desenvolva as suas duas classes e o código de teste abaixo: