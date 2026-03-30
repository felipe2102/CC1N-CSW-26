import math

try:
    raio = float(input("Insira o valor do raio da caixa d'água: "))
    altura = float(input("Insira a altura da caixa d'água: "))
except Exception as erro:
    print(f'Um erro ocorreu! Código de erro: {erro}')

try:
    volume = 2*math.pi*raio*(raio + altura)
    volume = volume * 1000
    autonomia = volume / 1350

    print(f"A autonomia da caixa d'água é de {autonomia:.1f} horas")
except Exception as erro:
    print(f'Um erro ocorreu! Código de erro: {erro}')