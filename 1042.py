'''
Atividade 1042
2025.05.29
Renan Soares da Silva
'''
# fazer um código que leia três valores em linha e primeiro, os ordene em ordem crecente e dando umalinha de espaço alinhe eles em ordem que forão colocados/lidos
#entrada dos valores
A, B, C = input().split(" ")
A = int(A)
B = int(B)
C = int(C)
#verificação e ordenação dos valores
if (A>B):
    om = A
    sm =  B
else:
    om = B
    sm = A
if (om>C):
    om = om
    sm2 = C
else:
    sm2= om
    om = C
if (sm>sm2):
    smv = sm
    tm = sm2
else:
    smv= sm2
    tm = sm
#mostra os valores em ordem crecente
print(tm)
print(smv)
print(om)
# espaço que a atividade pediu
print("")
# ondem em que os valores forão colocados
print(A)
print(B)
print(C)