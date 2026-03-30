import math

try:
    altura = float(input("Insira a sua altura em metros: "))
    peso = float(input("\nInsira o seu peso em kilogramas: "))
except Exception as erro:
    print(f'\n Um erro ocorreu! Código de erro: {erro}')

try:
    imc = peso / altura**2
    print(f'O seu IMC é {imc:.1f}.')
except Exception as erro:
    print(f'Um erro ocorreu! Código de erro: {erro}')