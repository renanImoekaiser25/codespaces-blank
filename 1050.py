'''
Atividade 1050
2025.05.19
Renan Soares da Silva
'''
#fazer um código que leia o DDD e devolva qual estado é
# Entrada do DDD
DDD = int(input())
#Verificação do DDD e saída do estado de acordo com o DDD
if (DDD == 61 or 71 or 21 or 11 or 32 or 19 or 27 or 31):
    if (DDD == 61):
        print("Brasilia")
    elif (DDD == 71):
        print("Salvador")
    elif (DDD == 11):
        print("Sao Paulo")
    elif (DDD == 21):
        print("Rio de Janeiro")
    elif (DDD == 32):
        print("Juiz de Fora")
    elif (DDD == 19):
        print("Campinas")
    elif (DDD == 27):
        print("Vitoria")
    elif (DDD == 31):
        print("Belo Horizonte")
#Caso a verificação do DDD seja "false" a saída será " DDD nâo cadastrado"
    else:
        print("DDD nao cadastrado")