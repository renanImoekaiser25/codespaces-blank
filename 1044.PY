'''
Atividade 1044
2025.05.19
Renan Soares da Silva
'''
#ler dois valores e dizer se eles são multiplos ou nâo
#le a entrada dos valores
valor1, valor2 = input().split (' ')
#faz a correção dos valores
valor1 = int(valor1)
valor2 = int(valor2)
#verificação se os valores inseridos são
if (valor1 > valor2):
    if (valor1 % valor2 == 0):
        print("Sao Multiplos")
    else:
         print("Nao sao Multiplos")
else:
    if (valor2 % valor1 == 0):
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
