import math

try:
    b = int(input("Digite o valor de B: "))
    c = int(input("\nDigite o valor de C: "))
except Exception as erro:
    print(f'Erro ocorrido: {erro}')

try:
    a = b*b + c*c
    a = math.sqrt(a)
    print(f'A hipotenusa de {b} e {c} é aproximadamente {a:.2f}')
except Exception as erro:
    print(f'Erro ocorrido: {erro}')