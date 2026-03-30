import math

try:
    salarioHora = float(input("Insira o quanto você recebe por hora trabalhada: "))
    horasTrabalhadas = float(input("Insira o total de horas que você trabalha no mês: "))
except Exception as erro:
    print(f'Um erro ocorreu! Código de erro: {erro}')

try:
    salarioMensalBruto = salarioHora * horasTrabalhadas

    descontoINSS = salarioMensalBruto - (92/100 * salarioMensalBruto)
    descontoIR = salarioMensalBruto - (89/100 * salarioMensalBruto)
    descontoSindicato = salarioMensalBruto - (95/100 * salarioMensalBruto)
    totalDescontos = descontoINSS + descontoIR + descontoSindicato

    salarioMensalLiquido = salarioMensalBruto - totalDescontos

    print(f'O seu salário bruto foi de R${salarioMensalBruto:.2f}')
    print(f'Você pagou R${descontoINSS:.2f} para o INSS')
    print(f'Você pagou R${descontoSindicato:.2f} para o sindicato')
    print(f'Seu salário líquido foi R${salarioMensalLiquido:.2f}')
except Exception as erro:
    print(f'Um erro ocorreu! Código de erro: {erro}')