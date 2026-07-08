"""
DESAFIO 03: Contador de Frequência de Caracteres

Nível: Intermediário (Funções)
Objetivo: Mapear e contar a ocorrência de dados textuais alimentando dicionários dinamicamente.
Conceitos: Manipulação de strings (.replace, .lower), loops de contagem, método de busca em dicionário (.get).

Enunciado:
    Construa uma função chamada 'contar_frequencia_letras(texto)'.
    A função deve limpar os espaços em branco do texto, converter todas as letras para minúsculas 
    e gerar um mapeamento. Ela deve retornar um dicionário onde cada chave é uma letra encontrada 
    no texto e o valor é a quantidade de vezes que essa letra se repetiu.

Exemplo de Execução:
    Texto de Entrada: "Python"
    --------------------------------------------------------
    > Mapa de Frequência: {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
--------------------------------------------------------
"""
# Desenvolva a sua função e o seu código abaixo:

def contar_frequencia_letras(texto):
    # 1. Criamos um dicionário vazio que será o nosso mapa final
    mapa_frequencia = {}

    # 2. Lemos cada letra do texto digitado
    for letra in texto:
        
        # 3. Ignoramos espaços e pontuações
        if letra.isalpha():
            
            # 4. Padronizamos para minúscula (para que 'P' e 'p' contem como a mesma letra)
            letra_formatada = letra.lower()
            
            # 5. A MÁGICA DO .get()
            # O .get(chave, valor_padrao) tenta buscar a letra no dicionário.
            # Se a letra ainda não existe lá dentro, ele retorna 0 (valor padrão que definimos).
            # Em seguida, somamos +1. 
            mapa_frequencia[letra_formatada] = mapa_frequencia.get(letra_formatada, 0) + 1

    # 6. Retornamos o dicionário pronto e preenchido
    return mapa_frequencia


# ==========================================
# TESTANDO A FUNÇÃO NA PRÁTICA
# ==========================================
print("-" * 56)
print(" Analisador de Frequência de Letras ".center(56, "-"))
print("-" * 56)

# Coletamos o texto e já aplicamos o .strip() para limpar as bordas
texto_usuario = input("Digite um texto ou palavra: ").strip()

# Chamamos a função e guardamos o retorno (o dicionário)
resultado = contar_frequencia_letras(texto_usuario)

print("-" * 56)
print(f"> Texto Original: '{texto_usuario}'")
print(f"> Mapa de Frequência: {resultado}")
print("-" * 56)