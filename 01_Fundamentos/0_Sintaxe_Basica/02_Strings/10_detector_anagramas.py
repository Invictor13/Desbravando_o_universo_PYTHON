"""
Exercício 10: Detector de Anagramas
    Objetivo: Verificar se duas palavras ou frases são anagramas (se possuem as mesmas letras na mesma quantidade, alterando apenas a ordem).
    Conceitos: Limpeza de espaços, ignorar maiúsculas/minúsculas e uso de ordenação com sorted() combinado com strings.

Enunciado:
    Crie um programa que receba duas palavras do usuário. O programa deve verificar 
    se elas formam um anagrama. Lembre-se de limpar os espaços e desconsiderar a 
    diferença entre letras maiúsculas e minúsculas.

Exemplo de Execução:
    Digite a primeira palavra: Amor
    Digite a segunda palavra: Roma
    --------------------------------------------------------
    > É um anagrama? True 
    --------------------------------------------------------
"""
# Entrada do usuário
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

# Limpeza: remove os espaços internos e padroniza para letras minúsculas
p1_limpa = palavra1.replace(" ", "").lower()
p2_limpa = palavra2.replace(" ", "").lower()

# Processamento: Ordena as letras de cada palavra e compara os resultados
eh_anagrama = sorted(p1_limpa) == sorted(p2_limpa)

print("--------------------------------------------------------")
print(f"> É um anagrama? {eh_anagrama}")
print("--------------------------------------------------------")