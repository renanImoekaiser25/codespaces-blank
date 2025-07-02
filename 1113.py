'''
Atividade 1113
2025.06.11
Renan Soares da Silva
'''
# obejetivo : fazer um código que ira ler dois valores e dizer se a ordem deles é cresente ou decresente
# criraçao das variaveis
A = 1
B = 0
# criacao de um sistema de repeticao e tambem um sistema de entrada e verificacao
while A != B:
    # entrada dos valores em linha
    A, B = input().split(" ")
    # correcao dos valores
    A = int(A)
    B = int(B)
    # sistema de verificacao
    if A > B:
        print('Decrescente')
    elif A < B:
        print('Crescente')
    # sistema para parar o codigo
    if A == B:
        break