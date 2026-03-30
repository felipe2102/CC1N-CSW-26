try:
    n1 = int(input("Insira um número: "))
    n2 = int(input("Insira outro número: "))
    n3 = int(input("Insira outro número: "))
except Exception as erro:
    print(f'\n Um erro ocorreu! Código de erro: {erro}')

if (n1 == n2 == n3 or n1 == n2 or n1 == n3 or n3 == n2):
    print("É PRA SER NÚMERO DIFERENTE SEU ANIMAL")
else:
    print(f'\n Um erro ocorreu! Código de erro: {erro}')

try:
    media = (n1 + n2 + n3) / 3
    print(f'A média entre {n1}, {n2} e {n3} é {media}')
except Exception as erro:
    print(f'\n Um erro ocorreu! Código de erro: {erro}')