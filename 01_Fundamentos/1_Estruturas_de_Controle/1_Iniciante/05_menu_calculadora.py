"""
DESAFIO 05: Menu Interativo de Operações Matemáticas

Nível: Iniciante (Estruturas de Controle)
Objetivo: Construir um menu interativo resiliente que processe dados até que uma condição de saída seja acionada.
Conceitos: Loop infinito controlado (while True / break), entrada de dados, condicionais de controle.

Enunciado:
    Crie um script que receba dois valores numéricos iniciais (float). 
    Logo em seguida, apresente um menu na tela para o usuário escolher uma ação:
    [ 1 ] Somar os números
    [ 2 ] Multiplicar os números
    [ 3 ] Digitar novos números
    [ 4 ] Sair do Programa
    O programa deve executar a ação escolhida e reexibir o menu até que o usuário digite a opção '4' para encerrar.

Exemplo de Execução:
    Digite o 1º valor: 6.0
    Digite o 2º valor: 4.0
    --------------------------------------------------------
    Menu de Operações:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Novos Números
    [ 4 ] Sair do Programa
    Escolha uma opção: 1
    > Resultado da Soma: 10.0
    --------------------------------------------------------
    Menu de Operações:
    ...
    Escolha uma opção: 4
    > Saindo do sistema... Programa Encerrado.
"""

# Desenvolva o seu código abaixo:

print("""
------------ Calculadora Simples ---------------      
Seja Bem vindo,
Siga as instruções para utilizar a calculadora    
------------------------------------------------            
""")

i=0

while (i != 4):
    print("-------------Informe os Valores--------------")
    x = float(input("Informe o 1º Valor: "))
    y = float(input("Informe o 2º Valor: "))
    print(f"""
----------------------------------------------
Menu de Operações:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Novos Números
    [ 4 ] Sair do Programa
-----------------------------------------------""")
    i = int(input("Informe uma Opção: "))

    if (i == 1):
        soma = x + y
        print(f"Resultado da Soma: {soma} ")
    
    elif (i == 2):
        multiplicacao = x * y
        print(f"Resultado da Multiplicação: {multiplicacao} ")
    
    elif (i == 3):
        print("Resetando Valores!")
        pass

    elif ( i == 4):
        print("> Saindo do sistema... Programa Encerrado.")

    else:
        print("Opção Inválida! Tente Novamente...")