'''
tividade 1065
2025.06.09
Renan Soares da Silva
'''
# fazer uma programa que irar ler 5 valores e dizer quantos deles são pares
# criacao da variavel  para gurdar os valores pares
pares = 0
# sistema de repeticao que ira fazer a entrada e a comparacao dos valores 
for i in range(5):
    # entrada
    A = int(input())
    # verificacao dos valores e adiciona a variavel pares
    if A%2 == 0:
        pares += 1
# saida dos numeros pares 
print (f'{pares} valores pares')