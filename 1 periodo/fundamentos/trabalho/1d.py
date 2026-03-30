import math

try:
    raio = float(input("Insira o valor do raio do círculo:"))
except Exception as erro:
    print(f'Um erro ocorreu! Código de erro: {erro}')

try:
    area = math.pi*raio**2
    comprimento = 2*math.pi*raio
    print(f"A área do círculo é {area:.2f} e o comprimento é {comprimento:.2f}")
except Exception as erro:
    print(f'Um erro ocorreu! Código de erro: {erro}')