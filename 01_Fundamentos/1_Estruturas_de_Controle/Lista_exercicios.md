# 🧪 Exercícios Práticos: Estruturas de Controle

Bem-vindo ao laboratório de Estruturas de Controle! É aqui que o seu código ganha inteligência, aprendendo a tomar decisões com `if/elif/else` e a repetir tarefas de forma automatizada com os laços `for` e `while`.

---

## 🎯 Desafios Práticos

### 🟨 Nível: Iniciante (Tomada de Decisão)

#### 1. Classificador de Voto (`01_classificador_voto.py`)
* **Objetivo:** Praticar condicionais simples e compostas (`if/elif/else`).
* **Enunciado:** Crie um programa que receba a idade do usuário. O script deve exibir se o voto dele é:
  * **Negado** (menor de 16 anos)
  * **Obrigatório** (entre 18 e 70 anos)
  * **Opcional** (entre 16 e 17 anos, ou acima de 70 anos)

#### 2. Simulador de Caixa Eletrônico (`02_caixa_eletronico.py`)
* **Objetivo:** Aplicar lógica de comparação e validação de dados.
* **Enunciado:** Defina uma variável com um `saldo_disponivel` inicial (ex: R$ 500.00). Peça para o usuário digitar o valor que deseja sacar. Se o valor for menor ou igual ao saldo, exiba `"Saque realizado com sucesso!"` e o novo saldo. Caso contrário, exiba `"Saldo insuficiente."`.

---

### 🟧 Nível: Intermediário (Laços de Repetição)

#### 3. Tabuada Automatizada (`03_tabuada.py`)
* **Objetivo:** Criar repetições com intervalo definido usando o laço `for`.
* **Enunciado:** Solicite ao usuário um número inteiro de 1 a 10. Utilizando o laço `for` e a função `range()`, calcule e exiba a tabuada completa desse número (de 1 a 10) no formato: `X x Y = Resultado`.

#### 4. O Jogo da Adivinhação (`04_adivinhacao.py`)
* **Objetivo:** Controlar repetições baseadas em uma condição ativa usando o laço `while`.
* **Enunciado:** Defina um número secreto no seu código (ex: 7). Crie um loop que peça para o usuário tentar adivinhar o número. O loop deve continuar rodando (repetindo a pergunta) até que o usuário acerte o número. Quando ele acertar, exiba `"Parabéns, você acertou!"` e encerre o programa.

---

## 🚀 Como Executar e Guardar suas Resoluções

1. **Abra o seu Espaço:** Vá até a sua pasta dentro do diretório de contribuição: `03_Comunidade/[Seu_Usuario_GitHub]/1_Estruturas_Controle/`.
2. **Crie os scripts:** Salve seus arquivos `.py` com a lógica de resolução utilizando os nomes sugeridos (ex: `01_classificador_voto.py`).
3. **Execute para validar:** Rode o script no seu terminal para garantir que as condições e repetições estão funcionando direito:
   ```bash
   python 01_classificador_voto.py