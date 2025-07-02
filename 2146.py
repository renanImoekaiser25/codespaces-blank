'''
Atividade 2146
início da atividade: 2025.06.13
termino da atividade:2025.06.16
Renan Soares da Silva
'''
#  fazer um código que dependendo a entrada de uma saida da senha correspondene
# sistema de repeticao
while (True):
    # tenta rodar o codigo, caso de true ele mostra a senha caso nao ele para o codigo
    try:
        S = int(input())
        print(S - 1)
    except EOFError:
        break