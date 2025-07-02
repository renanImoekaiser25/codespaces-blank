'''
Ativade 1013
2025.05.28
Rena Soares da Silva
'''
#calcular as notas que devem ser entregue de acorodo como valor de entrada
#valor de entrada e correção do valor para numero inteiro
N,M = input().split('.')
N = int(N)
M = int(M)
#calculo do valor em notas
n100 = N// 100
N = N % 100
n50 = N// 50
N = N % 50
n20 = N// 20
N = N % 20
n10 = N// 10
N = N % 10
n5 = N// 5
N = N % 5
n2 = N// 2
m1 = N % 2
#calculo do valor em moedas
m50 = M // 50
M = M % 50
m25 = M // 25
M = M % 25
m10 = M // 10
M = M % 10
m05 = M // 5
m01 = M % 5
#depois de 15 mil calculos, aqui mostra a quantidade e o valor das notas e moedas que devem ser entregues 
print("NOTAS:")
print('%d nota(s) de R$ 100.00' %n100)
print('%d nota(s) de R$ 50.00' %n50)
print('%d nota(s) de R$ 20.00' %n20)
print('%d nota(s) de R$ 10.00' %n10)
print('%d nota(s) de R$ 5.00' %n5)
print('%d nota(s) de R$ 2.00' %n2)
print('MOEDAS:')
print("%d moeda(s) de R$ 1.00" %m1)
print("%d moeda(s) de R$ 0.50" %m50)
print("%d moeda(s) de R$ 0.25" %m25)
print("%d moeda(s) de R$ 0.10" %m10)
print("%d moeda(s) de R$ 0.05" %m05)
print("%d moeda(s) de R$ 0.01" %m01)