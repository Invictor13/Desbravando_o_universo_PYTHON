"""
Desafio 1: O mundo animal

Crie uma classe chamada Cachorro.
1. Atributos: nome e raca (ambos strings).
2. Métodos:
   - __init__(self, nome, raca): Inicializa os atributos do cachorro.
   - latir(self): Imprime uma mensagem como "O [nome], da raça [raca], está latindo: Au au!".
"""
# Início do Código

"""
 ----------------------- [1] Definindo a classe: Cachorro() ----------------------------------- 
  [1]nomes de classes em Python costumam ser escritos em PascalCase (letra maiúscula inicial).

 -------------------------------- [2] Método __init__() ---------------------------------------- 
  [2.1] O método __init__ atua como o "construtor", parametros criados: self, nome, raca. 
  [2.2] Ele é disparado automaticamente sempre que um novo cachorro é criado.
  [2.3] O 'self' é a ponte. Ele representa o objeto exato que está sendo criado.
  [2.4.1] As linhas abaixo pegam os valores recebidos na função e os atrelam permanentemente aos
  [2.4.2] atributos do objeto.

-------------------------------- [3] Método _latir() ----------------------------------------
  [3.1] O método latir obrigatoriamente recebe 'self' para enxergar os atributos (nome e raça)
  [3.2] que salvamos lá no __init__.
  [3.3] Ajuste na resolução: O exercício pede uma frase formatada com as variáveis.
  [3.4] A f-string (indicada pelo 'f' antes das aspas) permite injetar o self.nome e self.raca direto no texto.

----------------------------------- [4] Instanciação -------------------------------------------
  [4.1] Instanciação: Criamos um objeto real a partir do "molde" da classe Cachorro. 
  [4.2] O Python envia "Eros" e "Bulldogue" direto para o __init__. 
  [4.3] Execução: Chamamos a ação (método) específica para este objeto.
--------------------------------------------------------------------------------------------------
"""

class Cachorro(): 
    def __init__(self, nome, raca):
      self.nome = nome
      self.raca = raca


    def latir(self):
      print(f"O {self.nome}, da raça {self.raca}, está latindo: Au au!")
   
cao1 = Cachorro("Eros", "Bulldogue")
cao1.latir()
