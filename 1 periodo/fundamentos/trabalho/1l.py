import math

try:
    lado = float(input("Insira o lado do tanque de combustível: "))
    altura = float(input("Insira a altura do tanque de combustível: "))
except Exception as erro:
    print(f'Um erro ocorreu! Código de erro: {erro}')

try:
    volume = lado*lado*altura
    volume = volume * 1000
    autonomia = volume / 10
    print(f'A autonomia do carro é de {autonomia:.2f} km')
except Exception as erro:
    print(f'Um erro ocorreu! Código de erro: {erro}')