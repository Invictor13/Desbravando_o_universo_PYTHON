"""
DESAFIO 05: Gerador de Matriz Cartesiana (Loops Aninhados)

Nível: Avançado (Estruturas de Controle)
Objetivo: Dominar o conceito de repetições aninhadas (um loop dentro de outro) para mapeamento espacial.
Conceitos: Laço for aninhado (for dentro de for), f-strings de posicionamento, controle de iteração.

Enunciado:
    Em desenvolvimento de jogos 2D e análise de dados, matrizes de coordenadas são fundamentais.
    Crie um script que simule a varredura de um radar em uma grade de tamanho 3x3.
    O programa deve pedir ao usuário o caractere indicador do radar (ex: "X").
    Utilizando dois laços 'for' aninhados, o primeiro controlando as Linhas (de 1 a 3) e o segundo 
    controlando as Colunas (de 1 a 3), exiba na tela todas as combinações de coordenadas no formato de matriz.

Exemplo de Execução:
    Informe o símbolo do Radar: X
    --------------------------------------------------------
    Iniciando Mapeamento da Grade 3x3:
    > Ponto [Linha 1, Coluna 1] = X
    > Ponto [Linha 1, Coluna 2] = X
    > Ponto [Linha 1, Coluna 3] = X
    > Ponto [Linha 2, Coluna 1] = X
    ...
    > Ponto [Linha 3, Coluna 3] = X
    --------------------------------------------------------
"""
# Desenvolva o seu código abaixo:
lista1=[]
lista2=[]
lista3=[]

print("""
----------------------------- Radar ---------------------------------
Observe a matriz abaixo, e suas coordenadas espaciais:
                    [1,1][1,2][1,3]
                    [2,1][2,2][2,3]
                    [3,1][3,2][3,3]      
--------------------------------------------------------------------
Por favor, informe os valores de acordo com a posição da coordenada     
--------------------------------------------------------------------""")

for i in range(0,3):
    for j in range(0,3):
        valor = int(input(f"Informe um número Inteiro para a coordenada{i+1,j+1}: "))
        if(i==0):
            lista1.append(valor)
        if(i==1):
            lista2.append(valor)
        if(i==2):
            lista3.append(valor)

print(f"""
--------------------- Radar Atualizado -----------------------------      
                    {lista1}
                    {lista2}
                    {lista3}
--------------------------------------------------------------------""")

