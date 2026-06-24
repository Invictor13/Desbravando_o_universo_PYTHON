"""
DESAFIO 01: O Decorador de Monitoramento (Log Simples)

Nível: Avançado (Funções)
Objetivo: Compreender o conceito de Decoradores (Decorators) para injetar comportamento em funções existentes.
Conceitos: Funções de alta ordem, closures, sintaxe @decorator, passagem de parâmetros dinâmicos (*args, **kwargs).

Enunciado:
    Crie uma função decoradora chamada 'monitorar_execucao(funcao)'.
    Esse decorador deve interceptar a execução de qualquer função decorada por ele e exibir na tela:
    1. Uma mensagem indicando qual função está prestes a ser executada.
    2. O resultado retornado pela função após a execução.
    Decore uma função simples de soma para testar o comportamento.

Exemplo de Execução:
    @monitorar_execucao
    def somar(a, b):
        return a + b

    Chamada: somar(8, 4)
    --------------------------------------------------------
    [LOG]: Inicializando a função 'somar'...
    [LOG]: Função finalizada com sucesso!
    > Resultado obtido: 12
--------------------------------------------------------
"""
# Desenvolva a sua função decoradora e o seu código abaixo: