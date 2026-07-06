"""
Desafio 10: Sistema Simplificado de Conta Bancária

Nível: Iniciante (POO)
Objetivo: Gerenciar o estado interno de um objeto através de métodos que validam condições lógicas.
Conceitos: Atributos de instância, métodos de alteração de estado (setters lógicos) e validação com 
condicionais (if/else).

Enunciado:
Em sistemas bancários, a regra de ouro é garantir que o cliente não saque um dinheiro que não possui 
(ignorando cheque especial por enquanto).
Crie uma classe chamada ContaBancaria.

1) Atributos:

    1.1) titular (texto): O nome do dono da conta.

    1.2) saldo (float): O dinheiro disponível (deve iniciar zerado por padrão, a menos que especificado).

2) Métodos:

    2.1) __init__(self, titular, saldo=0.0): Inicia a conta.

    2.2) depositar(self, valor): Recebe um valor float e adiciona ao saldo da conta. 
    Imprima uma mensagem de sucesso.

    2.3) sacar(self, valor): Recebe um valor float e tenta subtrair do saldo. Regra: 
    O saque só pode ser realizado se o valor for menor ou igual ao saldo. 
    Caso contrário, imprima uma mensagem de "Saldo insuficiente".

    2.4) exibir_extrato(self): Imprime o nome do titular e o saldo atual formatado com duas casas decimais.

Exemplo de Execução Esperada:
--------------------------------------------------------
> Depósito de R$ 150.00 realizado com sucesso!
> ERRO: Saldo insuficiente para sacar R$ 200.00.
> Saque de R$ 50.00 realizado com sucesso!
--------------------------------------------------------
    Titular: Maria da Silva | Saldo Atual: R$ 100.00
--------------------------------------------------------
"""

class ContaBancaria():
    def __init__(self, titular, saldo = 0.0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self,valor):
        self.saldo = self.saldo + valor
        print(f"> Deposito de R${valor} realizado com sucesso")

    def sacar(self,valor):
        if(self.saldo < valor):
            print("> Saldo insuficiente para esta operação.")
        else:
            self.saldo = self.saldo - valor
            print(f"> Saque de R${valor} realizado com sucesso")
        

    def exibir_extrato(self):
        print(f"""--------------------------------------------------------
Titular: {self.titular} | Saldo Atual: R$ {self.saldo:.2f}
--------------------------------------------------------""")


cliente1 = ContaBancaria("Victor")
cliente1.sacar(50)
cliente1.depositar(120)
cliente1.sacar(50)
cliente1.exibir_extrato()
