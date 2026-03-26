try:
    lado = int(input("Digite o valor do lado do quadrado: "))
except Exception as erro:
    print(f'\nUm erro ocorreu! Mensagem de erro: {erro}')

area = lado*lado
print(f'')