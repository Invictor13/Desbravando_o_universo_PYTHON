"""
💻 Exercício 3: Diário de Classe
Crie uma classe chamada DiarioDeClasse.
1. Atributos: disciplina e professor (ambos strings), e alunos (uma lista).
2. Métodos:
   - __init__(self, disciplina, professor): Inicializa os atributos da disciplina e do professor. A lista de alunos deve começar vazia.
   - adicionar_aluno(self, nome_aluno): Adiciona um aluno à lista e imprime uma mensagem confirmando a matrícula na disciplina.
   - exibir_diario(self): Imprime o nome da disciplina, o professor responsável e a lista atual de alunos matriculados.
"""

# Início do Código
"""
-------- [1] Declarando uma Classe: DiarioDeClasse() --------
  [1.1] Observe que o construtor __init__ recebe apenas 'disciplina' e 'professor'. 
  [1.2] O atributo 'alunos' é definido internamente como uma lista vazia [], pois o diário começa zerado.
  [1.3] O método adicionar_aluno recebe um parâmetro extra (nome_aluno) para inserir na lista usando o comando .append().
  [1.4] Usamos 'self' em todos os lugares necessários para garantir que estamos modificando os dados daquele diário específico.
"""
l="-"*50
l_t="-"*20

class DiarioDeClasse():
   def __init__(self, disciplina, professor):
      self.disciplina = disciplina
      self.professor = professor
      self.alunos = []

   def adicionar_aluno(self, nome_aluno):
      self.alunos.append(nome_aluno)
      print(f"O Aluno(a): {nome_aluno} foi cadastrado com sucesso.")
   
   def exibir_diario(self):
      print(f"Disciplina: {self.disciplina}")
      print(f"Professor: {self.professor}")
      print(f"Alunos: {self.alunos}")  


print(f"""{l_t}  [1] Cadastrando uma Materia  {l_t}""")
diario_professor1 = DiarioDeClasse("Zé","TI")
diario_professor1.exibir_diario() 

print(f"""{l_t}  [2] Cadastrando os alunos  {l_t}""")
diario_professor1.adicionar_aluno("Victor")
diario_professor1.adicionar_aluno("Eros")
diario_professor1.adicionar_aluno("Jessica")
diario_professor1.adicionar_aluno("Maria")

print(f"""{l_t}  [3] Exibindo as informações da disciplina  {l_t}""")
diario_professor1.exibir_diario()  