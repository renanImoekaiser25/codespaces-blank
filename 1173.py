'''
Atividade 1173
inici da atividade: 2025.06.16
termino da atividade: 2025.06.18
Renan Soares da Silva
'''
# fazer um programa que a aprtir da entrada ira fazer o dobro dele 10 vezes e a cada multiplicação ira printar "N[(posição)] = (produto)"
# entrada do numero que devera ser multiplicado
e = int(input())
# criação de uma variavel suporte
n = 0
# estruttura de repeticao que fara o tabalho que mostrar o valor no N[0] até o N[10]
for i in range (10):
    # saida dos resultados
    print(f"N[{n}] = {e}")
    # correcao das variaveis para as proximas posicoes
    e = e*2
    n += 1