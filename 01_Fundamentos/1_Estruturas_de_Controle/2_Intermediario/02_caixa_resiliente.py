"""
DESAFIO 02: Simulador de Caixa Eletrônico com Interrupção

Nível: Intermediário (Estruturas de Controle)
Objetivo: Utilizar controle de fluxo em loops infinitos com critérios de paragem imediatos.
Conceitos: Laço while True, operadores de atribuição (-=), comando break, condicionais.

Enunciado:
    Desenvolva um simulador de saques bancários que funcione de forma contínua.
    O sistema deve começar com um 'saldo_disponivel' fixo de R$ 500.00.
    A cada iteração do loop, pergunte ao usuário quanto ele deseja sacar:
    - Se o valor for menor ou igual ao saldo, realize o saque, subtraia o valor e mostre o saldo restante.
    - Se o valor for maior que o saldo, exiba uma mensagem de erro.
    O programa deve encerrar imediatamente (break) se o usuário digitar '0' ou se o saldo chegar a R$ 0.00.

Exemplo de Execução:
    Saldo Atual: R$ 500.00
    Quanto deseja sacar (0 para sair): 200
    > Saque de R$ 200.00 realizado com sucesso!
    --------------------------------------------------------
    Saldo Atual: R$ 300.00
    Quanto deseja sacar (0 para sair): 0
    --------------------------------------------------------
    > Operação encerrada pelo usuário. Sistema finalizado.
    --------------------------------------------------------
"""

# Desenvolva o seu código abaixo: