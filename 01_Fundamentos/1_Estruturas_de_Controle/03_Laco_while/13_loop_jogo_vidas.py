"""
DESAFIO 03: Loop de Game Over (Sistema de Vidas)

Nível: Avançado (Estruturas de Controle)
Objetivo: Criar uma máquina de estados simples simulando a lógica de um game usando condicionais aninhadas.
Conceitos: Laço while condicional (vidas > 0), contadores de pontuação, operadores lógicos, strings.

Enunciado:
    Crie um script que simule o looping de um minijogo de sobrevivência. 
    O jogador começa com um total de 3 vidas. O script deve rodar dentro de um loop 'while' baseado nessa quantidade.
    A cada rodada, exiba as vidas restantes e peça uma ação no input: "avançar" ou "fazer nada".
    - Se ele digitar "avançar", ele passa de fase com sucesso, ganha 10 pontos e o loop continua.
    - Se digitar qualquer outra ação, ele cai em uma armadilha, perde 1 vida e o loop segue.
    Quando as vidas zerarem, o loop deve terminar sozinho e exibir a tela de "Game Over" com a pontuação final.

Exemplo de Execução:
    Status: Você tem 3 vidas restantes!
    O que deseja fazer? (avançar/parar): avançar
    > Sucesso! Você avançou e ganhou +10 pontos.
    --------------------------------------------------------
    Status: Você tem 3 vidas restantes!
    O que deseja fazer? (avançar/parar): correr
    > Armadilha detetada! Você perdeu 1 vida.
    --------------------------------------------------------
    ...
    > GAME OVER! Suas vidas acabaram. Pontuação Final: 20 pontos.
    --------------------------------------------------------
"""
# Desenvolva o seu código abaixo:

vida=3
i=1

while(vida > 0):
    print(f"""
----------- {i}ª Rodada -------------
> Vida Atual: {vida}
-------------------------------------
Por favor, informe uma ação:
> (1) - Avançar
> (2) - Recuar
> (3) - Caminhar para a Direita
> (4) - Caminhar para a Esquerda""")
    
    escolha = input("Escolha uma opção: ") 
    if (escolha == "1"):
        print("""
-----------------------------------
> Opção Escolhida: Avançar
> Sucesso! Você avançou de fase!
> ...e ganhou +10 de vida                       
            """)
        vida +=10

    elif (escolha == "2") or (escolha == "3") or (escolha == "4"):
        print("""
-----------------------------------
> Armadilha detetada! Você perdeu 10 vida.                    
            """)
        vida -= 10
    
    else:
        print("Opção Invalida")
    
    i +=1

    if(vida <= 0):
        print("""
-----------------------------------
>Game Over - Você Morreu!
-----------------------------------              
                      
              """)