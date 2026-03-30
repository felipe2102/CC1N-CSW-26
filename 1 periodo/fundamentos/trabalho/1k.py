import math

try:
    tamanho = int(input("Insira o tamanho do seu arquivo em Megabytes: "))
    velocidade = int(input("Insira a velocidade da sua internet em Megabytes por segundo: "))
except Exception as erro:
    print(f'Um erro ocorreu! Código de erro: {erro}')

try:
    tempo = tamanho / velocidade

    minutos = int(tempo // 60)
    segundos = int(tempo % 60)

    print(f'Levaria cerca de {minutos} minutos e {segundos} segundos para completar o download')
except Exception as erro:
    print(f'Um erro ocorreu! Código de erro: {erro}')