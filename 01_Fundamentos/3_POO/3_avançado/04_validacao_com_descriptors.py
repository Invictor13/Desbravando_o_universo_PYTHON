"""
DESAFIO 04: Controle Estrito de Atributos com Descritores (Descriptors)

Nível: Avançado (POO)
Objetivo: Interceptar o mecanismo de atribuição e leitura de dados usando o protocolo de descritores do Python.
Conceitos: Métodos __get__ e __set__, controle de acesso a atributos de baixo nível, encapsulamento avançado.

Enunciado:
    Para evitar que atributos críticos recebam dados inválidos (como salários negativos), podemos criar descritores reutilizáveis.
    1. Crie uma classe descritora chamada 'NaoNegativo'. Ela deve implementar os métodos '__set__(self, instancia, valor)' 
       e '__get__(self, instancia, dono)'. No método '__set__', valide se o valor é numérico e maior ou igual a zero. 
       Se for negativo, levante uma exceção do tipo 'ValueError'.
    2. Crie uma classe chamada 'Funcionario' que possua o atributo de classe 'salario = NaoNegativo()'.
    3. Instancie o funcionário e tente definir um salário negativo para validar o bloqueio do sistema.

Exemplo de Execução:
    f = Funcionario("Victor")
    f.salario = 5000.00  # Funciona normalmente
    f.salario = -100.00  # Deve levantar: ValueError ("O valor não pode ser negativo!")
--------------------------------------------------------
"""
# Desenvolva as suas classes e o código de teste abaixo: