'''
Atividade 1134
inicio da ativida: 2025.06.11
termino da ativida: 2025.06.13
Renan Soares da Silva
'''
# obejetivo: fazer um progrma que ira ler a entrada e de acordo com a entrada verificar se esta dentro da lsita, caso esteja adicionar um a variavel que foi requerida, caso nao, devera pedir mais uma saida. 
# criação das variáveis 
Aa = 0
G = 0
D = 0
# sistema de repetição e verificação alem do sistema de entrada
while (True):
    A = int(input())
    if A == 1:
        Aa += 1
    elif A == 2:
        G += 1
    elif A == 3:
        D += 1
    elif A == 4:
        break
# criação da mesnsgem e a saída da própria
msg = (('MUITO OBRIGADO' + f'\nAlcool: {Aa}' + f'\nGasolina: {G}' + f'\nDiesel: {D}'))
print(msg)