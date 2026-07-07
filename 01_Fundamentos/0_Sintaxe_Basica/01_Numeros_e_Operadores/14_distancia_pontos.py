"""
Exercicio 14: Cálculo de Distância entre Dois Pontos (Fórmula Matemática)

    I) Objetivo: Traduzir uma fórmula matemática complexa (Fórmula da Distância Euclidiana) para o Python.
    II) Conceitos: Entrada de múltiplos dados (float), potenciação (**), precedência de operadores 
    e raiz quadrada.

Enunciado:
    - Construa um script que calcule a distância entre dois pontos em um plano cartesiano.
    - O usuário deve fornecer as coordenadas do Ponto A (x1, y1) e do Ponto B (x2, y2).
    - A fórmula que você deve aplicar é: Distancia = √((x2 - x1)² + (y2 - y1)²)
        Dica: Para tirar a raiz quadrada de toda a operação no final, eleve o resultado a 0.5.
        Exiba o resultado final formatado com 4 casas decimais.

Exemplo de Execução:
--------------------------------------------------------
    Coordenada x1 do Ponto A: 1.0
    Coordenada y1 do Ponto A: 2.0
    Coordenada x2 do Ponto B: 4.0
    Coordenada y2 do Ponto B: 6.0
--------------------------------------------------------
    Cálculo de Geometria Analítica:
    > A distância entre o Ponto A e o Ponto B é de: 5.0000
--------------------------------------------------------
"""

# Desenvolva o seu código abaixo:
print("""
             ------ Calculadora de Distância Cartesiana -------
Este script calculará a menor distância entre dois pontos em um plano
--------------------------------------------------------""", end="\n")
print("""Informações Iniciais:
      -Ponto A (x1, y1)  
      -Ponto B (x2, y2)
      """)

pontoA_x1 = float(input("Informe o valor de X1 do ponto A: "))
pontoA_y1 = float(input("Informe o valor de Y1 do ponto A: "))
print("\033[H\033[J", end="")

print(f"""Informações Atualizadas:
      -Ponto A ({pontoA_x1},{pontoA_y1} )  
      -Ponto B (x2, y2)
      """, end="\n")

pontoB_x1 = float(input("Informe o valor de X1 do ponto B: "))
pontoB_y1 = float(input("Informe o valor de Y1 do ponto B: "))
print("\033[H\033[J", end="")

print(f"""Informações Atualizadas:
      -Ponto A ({pontoA_x1},{pontoA_y1} )  
      -Ponto B ({pontoB_x1},{pontoB_y1})
      """,end="\n")

distancia = ((pontoB_x1 - pontoA_x1)**2 + (pontoB_y1 - pontoA_y1)**2)**0.5
print(f"""
--------------- Cálculo de Geometria Analítica-------------------------
    > A distância entre o Ponto A e o Ponto B é de: {distancia:.2f}
-----------------------------------------------------------------------     
""")
