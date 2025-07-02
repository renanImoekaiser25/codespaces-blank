'''
Atividade 1153
2025.06.11
'''
# de acorodo com a entrada calcular seu fatorial
# entrdada
E = int(input())
# variavel que ira conter o resultado final e o primeiro calculo
V = E*(E-1)
# estrutura de repeticao e calculo das variaves do fatorial
for i in range (E-2):
    V = V*(E-2)
    E -= 1
# mostra o resultado final
print(V)