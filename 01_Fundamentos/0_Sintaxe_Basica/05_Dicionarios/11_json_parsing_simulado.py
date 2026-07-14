"""
Exercício 11: Simulação de Parsing de JSON
    Objetivo: Navegar em estruturas de dicionários aninhados, simulando a leitura de uma API.
    Conceitos: Dicionários dentro de dicionários, acesso múltiplo encadeado (ex: dict[k1][k2]).

Enunciado:
    No mundo real, APIs retornam dados no formato JSON, que no Python são lidos como dicionários.
    Crie o seguinte dicionário aninhado simulando uma resposta de API:
    api_response = {
        "usuario": 101,
        "perfil": {
            "nome": "Marcos",
            "contato": {"email": "marcos@email.com", "telefone": "9999-9999"}
        }
    }
    
    O seu desafio é escrever um código que navegue por essa estrutura e extraia 
    apenas o e-mail do usuário, imprimindo-o na tela.

Exemplo de Execução:
    Processando resposta da API...
    --------------------------------------------------------
    > E-mail extraído do JSON: marcos@email.com
    --------------------------------------------------------
"""