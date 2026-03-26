import math

try:
    ya = float(input("Insira o valor de Ya: "))
    yb = float(input("\nInsira o valor de Yb: "))
    xa = float(input("\nInsira o valor de Xa: "))
    xb = float(input("\nInsira o valor de Xb: "))
except Exception as erro:
    print(f'Mensagem de erro: {erro}')

try:
    resultado = math.sqrt((xb - xa)** + (yb - ya)**) 
    print(f'O resultadoda equação é {resultado}')
except Exception as erro:
    print(f'Mensagem de erro: {erro}')