"""
Desafio 4: Controle de Leitura

Crie uma classe chamada Livro.
1. Atributos: titulo (string), autor (string) e paginas_lidas (inteiro, padrão é 0).
2. Métodos:
   - __init__(self, titulo, autor): Inicializa o livro.
   - ler_paginas(self, quantidade): Adiciona a quantidade informada ao atributo paginas_lidas e imprime "Você já leu [paginas_lidas] páginas de [titulo]".

"""

class Livro():
   def __init__(self, titulo, autor):
      self.titulo = titulo
      self.autor = autor
      self.paginas_lidas = 0

   def ler_paginas(self, quantidade):
      self.paginas_lidas = self.paginas_lidas + quantidade

      print(f"Você já leu um total de {self.paginas_lidas} páginas")

livro1 = Livro("Testando Livros","Victor Viana")
livro1.ler_paginas(50)
