'''
Ativade 1013
2025.05.26
Rena Soares da Silva
'''
#Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”
# entrada dos valores
a, b, c = input(). split(' ')
#correção dos valores
a = int(a)
b = int(b)
c = int(c)
#calculo dos valores
ab = (a + b + abs(a - b))/2
bc = (ab + c + abs(ab - c))/2
#resuldado dos valores
print("%.0f eh o maior" %bc)
