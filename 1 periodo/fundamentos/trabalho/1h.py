import math

try:
    raio = float(input("Insira o valor do raio do cilíndro: "))
    altura = float(input("Insira a altura do cilíndro: "))
except Exception as erro:
    print(f'Um erro ocorreu! Código de erro: {erro}')

try:
    area = 2*math.pi*raio*(raio + altura)

    litrosGastos = area / 3
    latasGastas = litrosGastos / 5
    custoTotal = latasGastas * 50

    print(f'Para a pintura do tanque foram gastas {latasGastas:.2f} latas de tintas, totalizando um custo de R${custoTotal:.2f}')
except Exception as erro:
    print(f'Um erro ocorreu! Código de erro: {erro}')