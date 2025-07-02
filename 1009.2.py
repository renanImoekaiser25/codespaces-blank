'''
Atividade 1009
2025.05.12
Renan Soares da silva
'''
# fazer um programa que leia o nome, salário fixo e as vendas de um vendedor, e calcular a sua comissão
#nome do vendedor
NOME = input()
# salario fixo
SALARIO = float(input())
#total de vendas
VENDAS = float(input())
# comissão e total do salário
TOTAL = SALARIO + VENDAS*0.15
#mostra o salario do vendedor
print("TOTAL = R$ %.2f" %TOTAL)
