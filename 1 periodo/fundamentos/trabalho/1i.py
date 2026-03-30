import math

try:
    x1 = int(input("Insira o valor de X1: "))
    y1 = int(input("Insira o valor de Y1: "))
    x2 = int(input("Insira o valor de X2: "))
    y2 = int(input("Insira o valor de Y2: "))
except Exception as erro:
    print(f'Um erro ocorreu! Código de erro: {erro}')

try:
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f'A distância entre o ponto ({x1},{y1}) e o ponto ({x2},{y2}) é {distancia:.2f}')
except Exception as erro:
    print(f'Um erro ocorreu! Código de erro: {erro}')