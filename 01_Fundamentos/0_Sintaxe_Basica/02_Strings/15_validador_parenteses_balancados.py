"""
Exercício 15: Validador de Parênteses Balanceados
    Objetivo: Lógica pura de compiladores para validar fechamento de escopos[cite: 172].
    Conceitos: Verificações sequenciais de caracteres e uso de estruturas de dados para rastreio[cite: 172].

Enunciado:
    Escreva um programa que receba uma expressão matemática. O sistema deve validar 
    se todos os parênteses (), colchetes [] e chaves {} presentes foram abertos e 
    fechados na ordem matemática correta[cite: 172].

Exemplo de Execução:
    Digite a expressão: (2 + 3) * [5 - 1]
    > Validação: True [cite: 173]
    
    Digite a expressão: (2 + 3]
    > Validação: False [cite: 174]
"""
# Entrada do usuário
expressao = input("Digite a expressão: ")

# Dicionário mapeando o fechamento com a sua respectiva abertura
mapeamento = {')': '(', ']': '[', '}': '{'}
pilha = []
valido = True

for caractere in expressao:
    # Se for um caractere de abertura, joga na pilha
    if caractere in mapeamento.values():
        pilha.append(caractere)
    # Se for um caractere de fechamento
    elif caractere in mapeamento.keys():
        # Se a pilha estiver vazia ou o topo não combinar com o fechamento
        if not pilha or pilha[-1] != mapeamento[caractere]:
            valido = False
            break
        else:
            pilha.pop() # Remove o par correspondente do topo da pilha

# Se sobrou algum elemento na pilha que não foi fechado, a expressão é inválida
if len(pilha) != 0:
    valido = False

print("--------------------------------------------------------")
print(f"> Validação: {valido}")
print("--------------------------------------------------------")