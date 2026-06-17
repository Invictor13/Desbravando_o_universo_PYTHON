# 🧪 Exercícios Práticos: Programação Orientada a Objetos (POO)

Bem-vindo ao laboratório de POO! Aqui o seu nível como desenvolvedor sobe um degrau importante. Você vai aprender a modelar sistemas simulando o mundo real, agrupando dados (atributos) e comportamentos (métodos) dentro de estruturas chamadas Classes.

---

## 🎯 Desafios Práticos

### 🟨 Nível: Iniciante (Classes, Atributos e Métodos)

#### 1. Modelando um Carro (`01_classe_carro.py`)
* **Objetivo:** Criar uma classe básica, instanciar objetos e manipular atributos por meio de métodos.
* **Enunciado:** Crie uma classe chamada `Carro` que possua:
  * Atributos de instância: `marca`, `modelo` e `velocidade_atual` (que sempre começa em `0`).
  * Um método construtor (`__init__`).
  * Um método chamado `acelerar(quantidade)`, que aumenta a `velocidade_atual` com base no valor passado.
  * Um método chamado `exibir_status()`, que mostra a marca, modelo e a velocidade atual do carro.
* *Ação:* Instancie um objeto dessa classe (ex: um Fusca), acelere ele algumas vezes e exiba o status na tela.

#### 2. Gerenciador de Conta Bancária Simples (`02_conta_bancaria.py`)
* **Objetivo:** Entender o conceito de estado do objeto e validação interna.
* **Enunciado:** Crie uma classe `ContaBancaria` com os atributos `titular` e `saldo` (iniciado com o valor que o usuário escolher no construtor). Crie os métodos `depositar(valor)` e `sacar(valor)`. O método de saque deve validar se a conta possui saldo suficiente antes de subtrair o valor. Se não tiver, exiba uma mensagem de erro.

---

### 🟧 Nível: Intermediário (Encapsulamento e Relações entre Objetos)

#### 3. Cadastro de Clientes Protegido (`03_encapsulamento.py`)
* **Objetivo:** Praticar o encapsulamento de atributos (atributos privados) e o uso de métodos *getters* e *setters* ou `@property`.
* **Enunciado:** Crie uma classe `Usuario` onde os atributos `__nome` e `__cpf` sejam **privados** (utilizando o duplo sublinhado `__`). 
  * Crie um método `@property` para permitir a leitura do nome.
  * Crie um método *setter* para o nome que valide se o texto não está vazio antes de atualizar. 
  * Garanta que o CPF só possa ser lido, mas nunca alterado depois que o objeto for criado.

#### 4. O Sistema do Pet Shop (`04_sistema_animais.py`)
* **Objetivo:** Exercitar o conceito de Herança e Polimorfismo.
* **Enunciado:** Crie uma classe base (mãe) chamada `Animal` com um atributo `nome` e um método `emitir_som()`, que apenas exibe um som genérico ou uma mensagem de "O animal faz um som". 
  * Crie duas subclasses (classes filhas): `Cachorro` e `Gato`.
  * Faça o *override* (sobrescrita) do método `emitir_som()` em cada uma delas para que o cachorro exiba `"Au Au!"` e o gato exiba `"Miau!"`.
  * Instancie um cachorro e um gato em um loop e faça ambos emitirem seus respectivos sons para ver o polimorfismo acontecer na prática.

---

## 🚀 Como Executar e Guardar suas Resoluções

1. **Vá para seu Espaço Dev:** Navegue até o seu diretório na comunidade: `03_Comunidade/[Seu_Usuario_GitHub]/3_POO/`.
2. **Crie os Scripts:** Desenvolva os códigos `.py` usando as nomenclaturas indicadas (ex: `01_classe_carro.py`).
3. **Valide no Terminal:** Rode o script para garantir que os objetos estão interagindo de forma correta e os métodos estão respondendo bem:
```bash
   python 01_classe_carro.py