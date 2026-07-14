"""
Exercício 07: A Armadilha da Imutabilidade
    Objetivo: Compreender a fundo o conceito de referências de memória e a imutabilidade rasa (shallow) da tupla.
    Conceitos: Tuplas que contêm listas mutáveis internas.

Enunciado:
    Crie uma tupla chamada 'sistema' que guarde informações estáticas e uma lista dinâmica de permissões: 
    ("Admin", "admin@site.com", ["ler", "escrever"]).
    Apenas através de comentários no seu código, explique por que tentar alterar o nome "Admin" geraria erro. 
    Em seguida, através de indexação, acesse a lista que está dentro da tupla e use o .append() para 
    injetar uma nova permissão ("deletar"). Exiba a tupla final, mostrando que a lista interna mudou 
    (apesar da tupla pai continuar blindada)!

Exemplo de Execução:
    > Tupla original: ('Admin', 'admin@site.com', ['ler', 'escrever'])
    --------------------------------------------------------
    Injetando nova permissão na lista interna...
    > Tupla final: ('Admin', 'admin@site.com', ['ler', 'escrever', 'deletar'])
"""