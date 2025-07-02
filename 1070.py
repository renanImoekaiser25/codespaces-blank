'''
Atividade 1070
2025.06.11
Renan Soares da Silva
'''
# fazer um codigo que a partir do valor de entrada mostra os proximos 6 numeros impares após o iicial, inclusive ele se for o caso
# entrada do valor que sera verificado
X = int(input())
# sistema de verificacao
if X % 2 == 0:
    # correcao do valor caso seja par
    X += 1
    # sistema que mostra os proximos 6 numeros impares a partir da entrada
    for i in range (6):
        print(X)
        X += 2    
# sistema que fara aparecer os proximos 6 numeros ipares incluindo a entrada
else:
    for i in range (6):
        print(X)
        X += 2