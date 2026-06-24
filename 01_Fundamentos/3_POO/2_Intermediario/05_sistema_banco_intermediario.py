"""
DESAFIO 05: Simulador Financeiro com Validação de Limite

Nível: Intermediário (POO)
Objetivo: Combinar encapsulamento, estado do objeto e manipulação de fluxos lógicos complexos.
Conceitos: Métodos com condicionais compostas, alteração de múltiplos estados, retorno de status.

Enunciado:
    Crie uma classe chamada 'ContaEspecial' que possua os atributos: 'titular', 'saldo' e 'limite_cheque_especial'.
    O método de saque 'sacar(valor)' deve conter uma lógica de validação avançada:
    - O cliente pode sacar se o valor for menor ou igual ao 'saldo'.
    - Se o saldo for insuficiente, mas a diferença ainda couber dentro do 'limite_cheque_especial', o saque deve 
      ser liberado. O 'saldo' pode ficar negativo e o 'limite_cheque_especial' deve ser reduzido proporcionalmente.
    - Se não houver saldo nem limite suficiente, a operação deve ser negada com uma mensagem explicativa.

Exemplo de Execução:
    Conta: Victor | Saldo: R$ 100.00 | Limite Especial: R$ 300.00
    --------------------------------------------------------
    > Solicitando saque de R$ 250.00...
    > Saque autorizado utilizando o Cheque Especial!
    > Novo Saldo: R$ -150.00 | Limite Especial Restante: R$ 150.00
--------------------------------------------------------
"""
# Desenvolva a sua classe e o código de teste abaixo: