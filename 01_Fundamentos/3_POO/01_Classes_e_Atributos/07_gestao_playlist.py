"""
DESAFIO 07: Sistema de Playlist de Música

Nível: Iniciante (POO)
Objetivo: Praticar a manipulação de coleções (listas) armazenadas como atributos de um objeto.
Conceitos: Atributos do tipo lista, método .append(), iteração sobre objetos.

Enunciado:
    Construa uma classe chamada 'Playlist' que receba o 'nome' da lista no construtor.
    Ela deve conter um atributo interno chamado 'musicas', inicializado como uma lista vazia [].
    Crie dois métodos:
    1. 'adicionar_musica(nome_musica)': Adiciona a string recebida à lista de músicas.
    2. 'mostrar_playlist()': Exibe o nome da playlist e lista todas as músicas inseridas usando um loop.

Exemplo de Execução:
    --------------------------------------------------------
    Playlist: Clássicos do Rock
    Músicas Inseridas:
    - Hotel California
    - Back In Black
--------------------------------------------------------
"""
# Desenvolva a sua classe e a lógica de teste abaixo:
class Playlist:
    def __init__(self, nome):
        self.nome = nome       # Recebe o nome da playlist (ex: "Clássicos do Rock")
        self.musicas = []      # Inicializa a lista vazia internamente

    def adicionar_musica(self, nome_musica):
        # Adiciona a música recebida por parâmetro dentro da nossa lista
        self.musicas.append(nome_musica)
    
    def mostrar_playlist(self):
        print("--------------------------------------------------------")
        print(f"Playlist: {self.nome}")
        print("Músicas Inseridas:")
        
        # Iteração (loop) sobre a lista de músicas do objeto
        for musica in self.musicas:
            print(f" - {musica}")
        print("--------------------------------------------------------")

# --- Lógica de Teste ---

# 1. Instancia a playlist passando apenas o nome dela
playlist1 = Playlist("Clássicos do Rock")

# 2. Adiciona as músicas usando o método criado
playlist1.adicionar_musica("Hotel California")
playlist1.adicionar_musica("Back In Black")

# 3. Exibe o resultado final
playlist1.mostrar_playlist()
        
