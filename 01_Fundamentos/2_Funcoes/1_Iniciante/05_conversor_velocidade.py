"""
DESAFIO 05: Conversor de Velocidade (Km/h para M/s)

Nível: Iniciante (Funções)
Objetivo: Realizar operações de conversão física utilizando isolamento de escopo.
Conceitos: Divisão aritmética, formatação de retorno, escopo local de variáveis.

Enunciado:
    Na física e em desenvolvimento de jogos, converter unidades é essencial.
    Crie uma função chamada 'kmh_para_ms(velocidade_kmh)' que receba uma velocidade em km/h,
    converta para metros por segundo (dividindo o valor por 3.6) e retorne o resultado.
    Exiba o valor final formatado com exatamente duas casas decimais.

Exemplo de Execução:
    Informe a velocidade do veículo (km/h): 110
    --------------------------------------------------------
    > 110.0 km/h equivalem a exatamente: 30.56 m/s
--------------------------------------------------------
"""
# Desenvolva a sua função e o seu código abaixo:

def kmh_para_ms(velocidade_kmh):
    conversor = velocidade_kmh/3.6
    return conversor

print("------ Conversor KM/H para M/S --------")
x_kmh = int(input("Informe a Sua Velocidade(KM/H): "))
x_ms = kmh_para_ms(x_kmh)

print(f"""-------------------------------------------------------
{x_kmh:.2f} km/h equivalem a exatamente: {x_ms:.2f} m/s
-------------------------------------------------------""")