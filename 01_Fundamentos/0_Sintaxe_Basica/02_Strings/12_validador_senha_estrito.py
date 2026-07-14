"""
Exercício 12: Validador de Senha Estrito
    Objetivo: Criar uma rotina de segurança que valida requisitos corporativos de uma senha[cite: 166].
    Conceitos: Métodos como .isupper(), .islower(), .isdigit() e loops de varredura[cite: 167].

Enunciado:
    Desenvolva um programa que receba uma senha digitada pelo usuário e valide se 
    ela cumpre todas as seguintes regras de segurança: mínimo de 8 caracteres, 
    pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial[cite: 166].

Exemplo de Execução:
    Digite a sua senha: SenhaForte123!
    --------------------------------------------------------
    > Status: Senha válida e segura!
    --------------------------------------------------------
"""
# Entrada do usuário
senha = input("Digite a sua senha: ")

# Variáveis de controle de requisitos
tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_especial = False

# Caracteres especiais considerados (pode adicionar mais se necessário)
caracteres_especiais = "!@#$%^&*()-_=+[{]};:'\",<.>/?\\|`~"

# Validação do tamanho mínimo
tamanho_valido = len(senha) >= 8

# Varredura caractere por caractere
for caractere in senha:
    if caractere.isupper():
        tem_maiuscula = True
    elif caractere.islower():
        tem_minuscula = True
    elif caractere.isdigit():
        tem_numero = True
    elif caractere in caracteres_especiais:
        tem_especial = True

# Validação final: Todas as condições precisam ser verdadeiras (True)
print("--------------------------------------------------------")
if tamanho_valido and tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
    print("> Status: Senha válida e segura!")
else:
    print("> Status: Senha INVÁLIDA. Certifique-se de incluir:")
    if not tamanho_valido: print("  - Mínimo de 8 caracteres")
    if not tem_maiuscula:  print("  - Pelo menos uma letra maiúscula")
    if not tem_minuscula:  print("  - Pelo menos uma letra minúscula")
    if not tem_numero:     print("  - Pelo menos um número")
    if not tem_especial:   print("  - Pelo menos um caractere especial (!@#$...)")
print("--------------------------------------------------------")