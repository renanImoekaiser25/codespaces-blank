'''
Atividade 1079
2025.06.11
Renan Soares da Silva
'''
#  fazer uma entrada que ira ler um valor para saber qunatas vezes o codigo deve ser executado e a cada repeticao aplicar a media ponderada e cada repeticao 3 valores
# entrada para um valor que ira definir o numero de repeticoes do codigo
E = int(input())
# estrutura de repeticao 
for i in range (E):
    # criacao de um lista e um sistema que irar colocar numeros a lista
    X = list(map(float, input().split()))
    # calculo ponderado dos valores da lista
    V = ((X[0]*2 + X[1]*3 + X[2]*5)/10)
    # mostra os valores da lista
    print(f"{V:.1f}")