"""
Exercício 04: Removedor de Itens por Valor
    Objetivo: Deletar itens buscando diretamente pelo nome e proteger o código contra quebras (ValueError).
    Conceitos: Método .remove() e operador lógico 'in'.

Enunciado:
    Crie um programa que possua uma lista com nomes de 4 cores (ex: "Azul", "Verde", "Amarelo", "Roxo").
    Solicite ao usuário que digite o nome de uma cor que ele deseja remover.
    
    Regra de Ouro: Antes de usar o método .remove(), verifique se a cor digitada realmente 
    existe na lista utilizando o operador 'in'. Se existir, remova-a e exiba o sucesso. 
    Se não, exiba uma mensagem de erro amigável.

Exemplo de Execução:
    Cores disponíveis: ['Azul', 'Verde', 'Amarelo', 'Roxo']
    Digite uma cor para remover: Preto
    --------------------------------------------------------
    ❌ Erro: A cor 'Preto' não está na lista!
    --------------------------------------------------------
    Digite uma cor para remover: Verde
    ✅ 'Verde' removida com sucesso. Nova lista: ['Azul', 'Amarelo', 'Roxo']
"""

lista = ['Azul','Verde','Amarelo',"Vermelho"]

print(f"""
---------- [ Cores Disponíveis] --------------
{lista}
----------------------------------------------
> Selecione uma Cor para exclui-la....""")

cor_escolhida = input("Informe a cor: ").capitalize()

if cor_escolhida in lista:
    lista.remove(cor_escolhida)
    print(f"""
---------- [ Cores Atualizadas] --------------
{lista}
----------------------------------------------
> A cor {cor_escolhida} foi apagada....""",end="\n")

else:
    print(f"A cor {cor_escolhida} não está na lista")
