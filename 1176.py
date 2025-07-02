'''
Atividade 1176
inicio da atividade: 2025.06.18
termino na atividade:2025.06.18
Renan Soares da Silva
'''
# fazer uma projecao do sistema matemacido de Fibonacci, sendo que a primeira entrada é a quantidades de vezes que o codigo sera executado e apos isso o proximo  numero sera quantas vezes a sistema matematico devera ser feito, a cada saida devera aparecer a quantidade de vezes que foi repetido e o resultado
# entrada de quantas repeticoes sera
I = int(input())
# sistema de repeticao principal
for i  in range(I):
    # correcao dos valores e criacao das variaveis principais e suporte
    p = 0
    s = 1
    va = 0
    # entrada de quantas vezes sera feito o sistema matematico
    v = int(input())
    # estrutura de repeticao secundario
    for i in range(v):
        # calculo e correcao das variaveis
        va = p + s
        s = p
        p = va
    #  saida dos resultados
    print(f'Fib({v}) = {va}')    