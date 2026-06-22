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