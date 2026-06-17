# 🧪 Exercícios Práticos: Funções

Bem-vindo ao laboratório de Funções! É aqui que o seu código deixa de ser apenas um script linear e passa a ser uma aplicação organizada, modular e profissional. Você vai aprender a isolar blocos de lógica, passar parâmetros, capturar retornos e documentar suas funções.

---

## 🎯 Desafios Práticos

### 🟨 Nível: Iniciante (Modularização Básica)

#### 1. Saudação com Horário (`01_saudacao.py`)
* **Objetivo:** Criar uma função simples com parâmetros e sem retorno direto (apenas exibição).
* **Enunciado:** Defina uma função chamada `saudar_usuario(nome, periodo)`. Ela deve receber o nome de uma pessoa e o período do dia (ex: `"Manhã"`, `"Tarde"`, `"Noite"`) e exibir uma mensagem na tela (Ex: `"Bom dia, Carlos!"` ou `"Boa noite, Carlos!"` dependendo do período informado).

#### 2. Conversor de Temperatura (`02_conversor_termico.py`)
* **Objetivo:** Praticar funções que realizam cálculos e utilizam a palavra-chave `return`.
* **Enunciado:** Crie uma função chamada `celsius_para_fahrenheit(celsius)`. Ela deve receber uma temperatura em graus Celsius, aplicar a fórmula de conversão ($F = C \times 1.8 + 32$) e **retornar** o valor em Fahrenheit. Fora da função, peça o valor ao usuário, chame a função e exiba o resultado retornado.

---

### 🟧 Nível: Intermediário (Lógica Avançada e Boas Práticas)

#### 3. O Otimizador de Texto (`03_otimizador_texto.py`)
* **Objetivo:** Manipular strings dentro de funções e documentar o código com *Docstrings*.
* **Enunciado:** Desenvolva uma função chamada `contar_e_limpar(texto)`. Ela deve:
  1. Remover os espaços em branco extras no início e no fim da string (usando `.strip()`).
  2. Contar quantos caracteres o texto possui (sem contar os espaços extras que foram removidos).
  3. **Retornar** a string limpa e a contagem de caracteres.
* *Desafio Extra:* Adicione uma *Docstring* (comentário de múltiplas linhas logo abaixo da definição da função) explicando o que ela faz, seus parâmetros e seus retornos.

#### 4. Calculadora com Funções de Primeira Classe (`04_super_calculadora.py`)
* **Objetivo:** Trabalhar com múltiplas funções e reutilização de escopo.
* **Enunciado:** Crie quatro funções básicas: `somar(a, b)`, `subtrair(a, b)`, `multiplicar(a, b)` e `dividir(a, b)`. Depois, crie uma quinta função principal chamada `calcular(operacao, n1, n2)` que receba uma string com o nome da operação desejada e os dois números, chame a função correspondente e retorne o resultado final.

---

## 🚀 Como Executar e Guardar suas Resoluções

1. **Acesse seu Diretório:** Vá para a sua pasta exclusiva na comunidade: `03_Comunidade/[Seu_Usuario_GitHub]/2_Funcoes/`.
2. **Crie os Arquivos:** Desenvolva os scripts `.py` utilizando a nomenclatura sugerida (ex: `01_saudacao.py`).
3. **Execute para Validar:** Teste no seu terminal se as funções estão retornando e exibindo os valores esperados:
```bash
   python 01_saudacao.py