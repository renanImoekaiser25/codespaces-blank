'''
Atividade 1037
2025.05.14
Renan Soares da Silva
'''
# fazer um programa que diga o intervalo da entrada, entre, 0 a 25, 25 a 50, 50 a 75 e 75 a 100, se o numero for maior deve dizer " Fora de intervalo"
# entrada do numero
Entrada = float(input())
# verificação de intervalo mostra qual o intervalo
if (Entrada >= 0):
    # verificação de intervalo mostra qual o intervalo
    if (Entrada <= 25):
        print('Intervalo [0,25]')
        # verificação de intervalo mostra qual o intervalo
    elif (Entrada <= 50):
        # verificação de intervalo mostra qual o intervalo
        print('Intervalo (25,50]')
        # verificação de intervalo mostra qual o intervalo
    elif (Entrada <= 75):
        print('Intervalo (50,75]')
        # verificação de intervalo mostra qual o intervalo
    elif (Entrada <= 100):
        print('Intervalo (75,100]')
        # verificação de intervalo mostra qual o intervalo
    else:
        print('Fora de intervalo')
        # verificação de intervalo mostra qual o intervalo
else:
        print('Fora de intervalo')
