"""
Desafio 2: Acelerando um Carro

Crie uma classe chamada Carro.
1. Atributos: modelo (string) e velocidade (inteiro). O carro sempre deve iniciar com velocidade 0.
2. Métodos:
   - __init__(self, modelo): Inicializa o modelo e define a velocidade inicial como 0.
   - acelerar(self): Aumenta a velocidade em 10 e imprime a velocidade atual.
   - frear(self): Diminui a velocidade em 10. 
   
   (Desafio: garanta que a velocidade não fique menor que zero) e imprime a velocidade atual.
"""

class Carro():
    def __init__(self, modelo):
      self.modelo = modelo
      self.velocidade = 0

    def acelerar(self):
      self.velocidade += 10
      print(f"O carro acelerou, velocidade atual: {self.velocidade} km/h")

    def frear(self):
      self.velocidade -= 10

      if(self.velocidade < 0):
         print("O carro está parado!")
         self.velocidade = 0

      else:
         print(f"O carro desacelerou, velocidade atual: {self.velocidade} km/h")
    
carro_1 = Carro("Fiat-Cronos")
carro_1.acelerar()
carro_1.frear()
carro_1.frear()
carro_1.frear()
carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()
