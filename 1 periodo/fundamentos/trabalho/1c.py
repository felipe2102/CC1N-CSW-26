try:
    lado = float(input("Insira o valor do lado do retângulo:"))
    altura = float(input("Insira o valor da altura do retângulo:"))
except Exception as erro:
    print(f'\nUm erro ocorreu! Mensagem de erro: {erro}')

area = lado*altura

print(f'A área do retângulo de lado {lado} e altura {altura} é {area}')