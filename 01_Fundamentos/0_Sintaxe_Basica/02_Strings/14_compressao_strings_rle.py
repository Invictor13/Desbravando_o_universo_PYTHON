"""
Exercício 14: Compressão de Strings (RLE)
    Objetivo: Implementar o algoritmo clássico de compressão Run-Length Encoding (RLE)[cite: 169].
    Conceitos: Loops de iteração, comparações sequenciais e contadores condicionais.

Enunciado:
    Crie um programa que receba uma string contendo muitos caracteres repetidos 
    em sequência. O seu sistema deve transformá-la em uma string compactada, 
    mostrando o caractere seguido do seu número de repetições sequenciais[cite: 170].

Exemplo de Execução:
    Digite a string: AAAABBBCCDAAAA
    --------------------------------------------------------
    > String comprimida: A4B3C2D1A4 [cite: 171]
    --------------------------------------------------------
"""
# Entrada do usuário
texto = input("Digite a string: ")

# Caso a string inserida seja vazia
if not texto:
    print("> String vazia")
else:
    string_comprimida = ""
    caractere_atual = texto[0]
    contador = 1

    # Percorre a string a partir do segundo caractere (índice 1)
    for i in range(1, len(texto)):
        if texto[i] == caractere_atual:
            contador += 1
        else:
            # Salva o resultado do bloco anterior
            string_comprimida += f"{caractere_atual}{contador}"
            # Reseta para o novo caractere encontrado
            caractere_atual = texto[i]
            contador = 1
            
    # Não esquecer de adicionar o último caractere após o término do loop
    string_comprimida += f"{caractere_atual}{contador}"

    print("--------------------------------------------------------")
    print(f"> String comprimida: {string_comprimida}")
    print("--------------------------------------------------------")