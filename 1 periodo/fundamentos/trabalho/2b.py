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

if (imc < 18.5):
    print("Você está classififcado como no estado de magreza.")
elif (18.5 < imc > 25):
    print("Você está saudável")
elif (25 < imc < 30):
    print("Você está sobrepeso")
elif (30 < imc < 35):
    print("Você está com obesidade grau I")
elif (35 < imc < 40):
    print("Você está com obesidade grau II (severa)")
elif (40 <= imc):
    print("Você está com obesidade grau III (mórbida)")
else:
    print("você está morto")