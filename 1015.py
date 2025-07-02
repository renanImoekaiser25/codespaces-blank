'''
Ativade 1013
2025.05.28
Rena Soares da Silva
'''
# calcular a distancia entra dois pontos
# entrada dos valores x e y
pi1 = input().split(" ")
pi2 = input().split(" ")
#coreção dos valores de x e y para float e ondem onde os valores que a vieram da entrada devem ir
x1 = float(pi1[0])
x2 = float(pi2[0])
y1 = float(pi1[1])
y2 = float(pi2[1])
#calculo da distancia
pi1 = (x2 - x1)**2
pi2 = (y2 - y1)**2
distancia = (pi1 + pi2)**0.5
#mostra o resutado do calculoo da distancia
print(f'{distancia:.4f}')