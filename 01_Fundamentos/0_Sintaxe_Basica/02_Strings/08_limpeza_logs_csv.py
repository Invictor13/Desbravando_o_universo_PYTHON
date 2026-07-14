"""
Exercício 08: Limpeza e Tabulação de Logs/CSV Corrompidos
    Objetivo: Simular a recepção de uma string suja vinda de um arquivo de log ou CSV corrompido.
    Conceitos: .join(), .splitlines(), remoção de quebras de linha (\n) ou tabulações (\t) e substituições encadeadas.

Enunciado:
    Imagine que o sistema recebeu um bloco de texto corrompido, cheio de quebras de linha irregulares 
    e espaçamentos incorretos. Crie um programa que receba essa string "suja" e aplique substituições 
    encadeadas e remoções de escape (\n, \t) para devolver o texto perfeitamente limpo e tabulado, 
    como um formato CSV limpo.

Exemplo de Execução:
    Texto recebido (Simulação): "Nome\n\tIdade\t\n  Profissao\n"
    --------------------------------------------------------
    Limpando dados...
    > Formato finalizado: Nome, Idade, Profissao
    --------------------------------------------------------
"""





# 1. Definição da string "suja" simulada pelo enunciado
texto_corrompido = "Nome\n\tIdade\t\n  Profissao\n"

print(f"""
-----------[1] Apresentação do Texto--------------------

> Texto Original: {texto_corrompido}
--------------------------------------------------------
Limpando Dados...  
""")

# 2. Tratando a string:
# - .split() sem argumentos é mágico: ele automaticamente divide a string
#   eliminando QUALQUER caractere de escape (\n, \t) e espaços em branco extras.
palavras_limpas = texto_corrompido.split()
# 3. Juntando as palavras limpas com uma vírgula e espaço para simular o CSV
formato_final = ", ".join(palavras_limpas)

print(f"""
---------------[2] Tratando a String--------------------
> Dados Limpos: {palavras_limpas}
--------------------------------------------------------
Ajustando o arquivo para separação por ","....
""")

# 4. Exibindo o resultado
print(f"""
---------------------[3] CSV Tratado--------------------
> Dadps Formatados: {formato_final}
--------------------------------------------------------
""")


