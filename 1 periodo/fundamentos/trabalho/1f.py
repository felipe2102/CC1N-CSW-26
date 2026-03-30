import math

try:
    raio = float(input("Insira o raio da esfera em metros: "))
except Exception as erro:
    print(f'Um erro ocorreu! Código de erro: {erro}')

try:
    volume = (4/3) * math.pi * raio**3
    volume = volume * 1000
    print(f'O volume da esfera de raio {raio} metros é {volume:.2f} litros')
except Exception as erro:
    print(f'Um erro ocorreu! Código de erro: {erro}')