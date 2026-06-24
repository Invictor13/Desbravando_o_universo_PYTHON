"""
DESAFIO 01: Abstração Corporativa (Classes Abstratas e Interfaces)

Nível: Avançado (POO)
Objetivo: Garantir contratos de código rígidos utilizando a biblioteca nativa 'abc'.
Conceitos: Classe Abstrata (ABC), decorador @abstractmethod, polimorfismo estrito, herança de interface.

Enunciado:
    Em sistemas de grande porte, as interfaces garantem que diferentes integrações sigam o mesmo padrão.
    1. Crie uma classe abstrata chamada 'ProvedorArmazenamento' que herde de 'ABC' (do módulo abc).
    2. Defina dois métodos abstratos utilizando @abstractmethod: 'salvar_arquivo(nome, dados)' e 'deletar_arquivo(nome)'.
    3. Crie duas subclasses concretas que herdem desse provedor: 'ArmazenamentoLocal' e 'ArmazenamentoNuvem'.
    4. Implemente a lógica (com prints simulados) em ambas as classes. Tente instanciar a classe abstrata 
       diretamente para validar se o Python impede a operação, e depois instancie as classes filhas.

Exemplo de Execução:
    --------------------------------------------------------
    > Inicializando Provedores de Armazenamento...
    > [Local] Arquivo 'relatorio.pdf' salvo com sucesso no diretório /uploads.
    > [Nuvem] Arquivo 'relatorio.pdf' enviado para o bucket S3 da AWS.
--------------------------------------------------------
"""
from abc import ABC, abstractmethod

# Desenvolva a sua classe abstrata, subclasses e código de teste abaixo: