"""
DESAFIO 8: Simulador de Relógio

Crie uma classe Relogio para simular o formato de 24 horas.

1. Atributos:
   - hora, minuto, segundo (todos inteiros).

2. Métodos:
   - __init__(self, hora=0, minuto=0, segundo=0): Inicia o relógio (padrão 00:00:00).
   - avancar_segundo(self): Soma 1 segundo. 
     * Regras: Ao bater 60s, zera e soma 1 min; ao bater 60m, zera e soma 1 hora; ao bater 24h, zera a hora.
   - exibir_hora(self): Imprime no formato HH:MM:SS.

Exemplo de uso:
relogio = Relogio(23, 59, 59)
relogio.avancar_segundo()
relogio.exibir_hora() # Saída esperada: 00:00:00
"""

class Relogio():
   def __init__(self, hora=0, minuto=0, segundo=0):
      self.hora = hora
      self.minuto = minuto
      self.segundo = segundo

   def avancar_segundo(self):
      self.segundo += 1
      
      # Verifica os segundos
      if self.segundo >= 60:
         self.segundo = 0
         self.minuto += 1
         
         # Verifica os minutos
         if self.minuto >= 60:
            self.minuto = 0
            self.hora += 1
            
            # Verifica as horas (Virada do dia)
            if self.hora >= 24:
               self.hora = 0
   
   def exibir_hora(self):
      # O :02d garante que sempre teremos 2 casas decimais
      print(f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}")

# Testando o código
relogio1 = Relogio(23, 59, 59)
relogio1.avancar_segundo()
relogio1.exibir_hora() # Saída esperada: 00:00:00