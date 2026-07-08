"""
DESAFIO 01: Calculadora de Perímetro de Retângulo

Nível: Iniciante (Funções)
Objetivo: Compreender a passagem de múltiplos parâmetros e o retorno de valores calculados.
Conceitos: Definição de função (def), passagem de argumentos, operadores aritméticos, return.

Enunciado:
    Crie uma função chamada 'calcular_perimetro(base, altura)' que receba as dimensões de um 
    terreno retangular e RETORNE o seu perímetro (soma de todos os lados: 2 * (base + altura)).
    Fora da função, peça os dados ao usuário, chame a função passando os valores e exiba o resultado.

Exemplo de Execução:
    Digite a base do retângulo (m): 10.0
    Digite a altura do retângulo (m): 5.0
    --------------------------------------------------------
    > O perímetro do retângulo é: 30.00 m
--------------------------------------------------------
"""
# Desenvolva a sua função e o seu código abaixo:
def Calc_Perimetro(base,altura):
    perimetro=(2*(base+altura))
    return perimetro


print("""
---------------- Simulando Terreno ----------------------      

        _________(X metros)__________
        |                           |
        |                           |
        |                           (Y metros)
        |                           |
        |___________________________|
      
---------------------------------------------------------   
> Precisamos preencher as medidas de X e Y:
---------------------------------------------------------           
      """)
x = int(input("Por favor, informe o valor da Base(X): "))
y = int(input("Por favor, informe o valor da altura(y): "))
perimetro_calculado = Calc_Perimetro(x,y)

if(x>y):
    print(f"""
---------------- Terreno Informado ----------------------      

            _________({x} metros)________
            |                           |
            |                           |
            |                           ({y} metros)
            |                           |
            |___________________________|
        
---------------------------------------------------------        
Perimetro do Terreno = {perimetro_calculado} metros
---------------------------------------------------------          
        """)
    
elif(x<y):
    print(f"""
---------------- Terreno Informado ----------------------      

            ______({x} metros)_____
            |                     |
            |                     |
            |                     |
            |                     ({y} metros)
            |                     |
            |                     |
            |_____________________|
        
---------------------------------------------------------        
Perimetro do Terreno = {perimetro_calculado} metros
---------------------------------------------------------          
        """)
    
else:
        print(f"""
---------------- Terreno Informado ----------------------      

            ____({x} metros)___
            |                 |
            |                 |
            |                 ({y} metros)
            |                 |
            |_________________|
        
---------------------------------------------------------        
Perimetro do Terreno = {perimetro_calculado} metros
---------------------------------------------------------          
        """)