"""
DESAFIO 05: Modelando um Smartphone

Nível: Iniciante (POO)
Objetivo: Compreender a estrutura de uma classe básica, criação de atributos e instanciação.
Conceitos: Definição de classe (class), construtor (__init__), palavra-chave self, objetos.

Enunciado:
    Crie uma classe chamada 'Smartphone' que possua:
    - Atributos de instância: 'marca', 'modelo' e 'bateria' (que sempre inicia em 100).
    - Um método construtor (__init__) para receber a marca e o modelo.
    - Um método chamado 'exibir_detalhes()' que mostre as informações do aparelho e a carga da bateria.
    Fora da classe, instancie um objeto (ex: um iPhone ou Galaxy) e chame o método de exibição.

Exemplo de Execução:
    --------------------------------------------------------
    Smartphone Cadastrado:
    > Marca: Apple | Modelo: iPhone 15
    > Bateria Atual: 100%
--------------------------------------------------------
"""
# Desenvolva a sua classe e a lógica de teste abaixo:


# Iniciando a classse Smartphone com os 2 parametros __init__ e exibir detalhes.
class Smartphone():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = 100

    def exibir_detalhes(self):
        print(f"""
-----------------------------------------------------------------------             
Smartphone Cadastrado:
> Marca: {self.marca} | Modelo: {self.modelo}
> Bateria: {self.bateria}
                       
-----------------------------------------------------------------------""")

cel_1 = Smartphone("Samsung","Galaxy S22")
cel_1.exibir_detalhes()