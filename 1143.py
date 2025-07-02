'''
 atividade 1143
 2025.05.21
 Renan Soares da Silva
'''
#Escreva um programa que leia um valor inteiro N (1 < N < 1000). Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.
# sistema que define a quantidade de linhas e calcula o nalor e deixa alinhado de acorodo com seu multiplo
N = int(input())
for i in range(1,N+1):
    print('%d %d %d' %(i,i**2,i**3))