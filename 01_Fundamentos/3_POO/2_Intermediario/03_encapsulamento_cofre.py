"""
DESAFIO 03: O Cofre Digital Protegido (Encapsulamento)

Nível: Intermediário (POO)
Objetivo: Proteger o estado interno do objeto utilizando atributos privados e métodos de validação (Getters/Setters).
Conceitos: Atributos privados (__), decorador @property, decorador @setter, validação de dados.

Enunciado:
    Desenvolva uma classe chamada 'CofreDigital' que possua um atributo privado chamado '__saldo' (iniciado em 0.0) 
    e um atributo privado chamado '__senha' (definido na criação do objeto).
    1. Crie uma propriedade (@property) para permitir a LEITURA do saldo (sem restrições).
    2. Crie um método chamado 'depositar(valor, senha_informada)' que só altera e soma o valor ao saldo 
       SE a senha informada pelo usuário for estritamente igual à senha privada do cofre. Caso erre, exiba um erro.

Exemplo de Execução:
    --------------------------------------------------------
    > Tentando depósito com senha incorreta (123)...
    > ERRO: Senha incorreta! Operação cancelada.
    --------------------------------------------------------
    > Tentando depósito com senha correta...
    > Depósito realizado com sucesso! Saldo Atual: R$ 500.00
--------------------------------------------------------
"""
# Desenvolva a sua classe e o código de teste abaixo: