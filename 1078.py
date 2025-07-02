'''
1078
2025.25.21
Renan Soares da Silva
'''
#Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:      
#entrada do valor N
N = int(input())
#Estrutura de repetição
for i in range(10):
    # saída da tabela e calculos
    print("%d x %d = %d" %(i +1, N, N*(i+1) ))