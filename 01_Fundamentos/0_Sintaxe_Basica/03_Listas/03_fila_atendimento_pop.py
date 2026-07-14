"""
Exercício 03: Fila de Atendimento do Banco (Pop)
    Objetivo: Simular uma fila do mundo real aprendendo a remover e capturar elementos do início e do fim.
    Conceitos: Métodos .pop(índice), .pop() vazio e .clear().

Enunciado:
    Crie um programa que inicie com uma fila de banco contendo 3 nomes (ex: "Ana", "Carlos", "Bia").
    Simule o seguinte fluxo e exiba o estado da fila a cada passo:
    
    1. Chame a primeira pessoa da fila para ser atendida (removendo-a pelo índice 0).
    2. Simule que a última pessoa da fila cansou de esperar e foi embora (removendo-a do final).
    3. Simule o fim do expediente, esvaziando totalmente a fila de uma vez.

Exemplo de Execução:
    Fila inicial: ['Ana', 'Carlos', 'Bia']
    --------------------------------------------------------
    > Atendendo: Ana. Fila restante: ['Carlos', 'Bia']
    > Desistência: Bia foi embora. Fila restante: ['Carlos']
    > Fim do expediente! Esvaziando fila...
    > Fila final: []
    --------------------------------------------------------
"""

fila = ["Ana", "Carlos", "Bia"]
primeiro = fila[0]
print(f"""
-------- Atendimento Iniciado --------
Fila Atual: {fila}
-------------------------------------- 
> Atendendo: {primeiro}""")
fila.pop(0)

ultimo = fila[-1]
print(f"""
-------- Atendimento Atualizado --------      
Fila Atual: {fila}     
-----------------------------------------""")

print(f"> Desistência:{ultimo} foi embora")
fila.pop(-1)

print(f"""
-------- Atendimento Atualizado --------      
Fila Atual: {fila}     
-----------------------------------------""")
