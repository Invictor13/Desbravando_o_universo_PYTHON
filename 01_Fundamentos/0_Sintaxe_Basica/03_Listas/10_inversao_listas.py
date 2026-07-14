"""
Exercício 10: Inversão de Listas (Duas Abordagens)
    Objetivo: Inverter a ordem dos elementos de uma lista de duas formas distintas[cite: 795].
    Conceitos: Método nativo .reverse() e técnica de fatiamento [::-1][cite: 795].

Enunciado:
    Crie um programa que inicie uma lista de números desordenada. Você deve demonstrar 
    duas técnicas diferentes para inverter a ordem (de trás para a frente) dos elementos[cite: 795].
    
    1. Inversão Temporária: Crie uma versão invertida da lista usando fatiamento [::-1] e exiba[cite: 795].
    2. Inversão Definitiva: Utilize o método .reverse() para modificar a lista original permanentemente[cite: 795].

Exemplo de Execução:
    > Lista Original: [10, 20, 30, 40, 50]
    --------------------------------------------------------
    > Inversão via Slicing (Temporária): [50, 40, 30, 20, 10]
    > A lista original continua intacta: [10, 20, 30, 40, 50]
    
    Aplicando .reverse()...
    > A lista original foi modificada: [50, 40, 30, 20, 10]
    --------------------------------------------------------
"""