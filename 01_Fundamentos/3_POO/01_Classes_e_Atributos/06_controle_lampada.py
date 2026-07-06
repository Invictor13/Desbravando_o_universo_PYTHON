"""
DESAFIO 06: O Interruptor Inteligente (Estado do Objeto)

Nível: Iniciante (POO)
Objetivo: Manipular o estado interno de um objeto por meio de métodos de ação.
Conceitos: Atributos booleanos, métodos alternadores, condicionais dentro de métodos.

Enunciado:
    Desenvolva uma classe chamada 'Lampada' cujo atributo 'ligada' comece sempre como False (desligada).
    A classe deve conter dois métodos:
    1. 'ligar()': Altera o atributo 'ligada' para True.
    2. 'observar()': Exibe "A lâmpada está iluminando o quarto." se estiver ligada, 
       ou "O quarto está completamente escuro." se estiver desligada.
    Instancie uma lâmpada, mude seu estado e observe o comportamento no console.

Exemplo de Execução:
    --------------------------------------------------------
    > Status Inicial: O quarto está completamente escuro.
    > Ligando o interruptor...
    > Status Atual: A lâmpada está iluminando o quarto.
--------------------------------------------------------
"""
# Desenvolva a sua classe e a lógica de teste abaixo:

class Lampada:
    def __init__(self):
        # Começa sempre como False, sem precisar de parâmetro externa
        self.ligada = False 

    def ligar(self):
        self.ligada = True
    
    def observar(self):
        if self.ligada:  # Em Python, não precisa de '== True', só 'if self.ligada' já basta
            print("> Status Atual: A lâmpada está iluminando o quarto.")
        else:
            print("> Status Inicial: O quarto está completamente escuro.")

# --- Lógica de Teste ---
print("--------------------------------------------------------")

# Instancia a lâmpada (repare que não passa nada nos parênteses)
lampada_1 = Lampada()

# Chama o método direto. Ele mesmo já faz o print interno.
lampada_1.observar()

print("> Ligando o interruptor...")
lampada_1.ligar()

# Chama novamente para ver o novo estado
lampada_1.observar()

print("--------------------------------------------------------")