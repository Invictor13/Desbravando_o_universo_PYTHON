"""
DESAFIO 09: Calculadora de Preço de Venda

Nível: Iniciante (POO)
Objetivo: Realizar cálculos matemáticos combinando atributos e parâmetros externos.
Conceitos: Métodos com retorno matemático, regras de precificação em objetos.

Enunciado:
    Em sistemas de e-commerce, calcular margens de lucro é rotina.
    Crie uma classe chamada 'Produto' que receba o 'nome' e o 'preco_custo' (float).
    Crie um método chamado 'calcular_preco_venda(margem_porcentagem)' que receba um valor 
    inteiro (ex: 50 para 50%) e RETORNE o preço final adicionando esse percentual sobre o custo.
    Instancie um produto, execute o cálculo e mostre o resultado monetário com duas casas decimais.

Exemplo de Execução:
    Produto: Teclado Mecânico | Custo: R$ 200.00
    --------------------------------------------------------
    > Preço de Venda sugerido com 50% de margem: R$ 300.00
--------------------------------------------------------
"""
# Desenvolva a sua classe e a lógica de teste abaixo:

class Produto():
    def __init__(self, nome, preco_custo):
        self.nome = nome
        self.preco_custo = preco_custo

    def calcular_preco_venda(self, margem_porcentagem):
        acrescimo = self.preco_custo * (margem_porcentagem / 100)
        preco_final = self.preco_custo + self.preco_custo*(1.0-margem_porcentagem/100)
        print(f"""
----------------------------------------------------------------
    Produto: {self.nome}   |    Custo: R$ {self.preco_custo}
---------------------------------------------------------------
> Preço de venda sugerido com {margem_porcentagem}% de margem.
> Preço Final: R$ {preco_final}        
---------------------------------------------------------------   
""")

produto1 = Produto("Teclado Mecânico", 200.00)
produto1.calcular_preco_venda(50)

