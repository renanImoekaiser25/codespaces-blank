'''
Atividade 1048
2025.06.02
Renan Soares da Silva
'''
#calcular o reajuste de salario de acorod com a tabela e mostrar o novo salario, o quanto de acrecimo ea porcentagem que foi aumentado
#entrada do valor do salario
s = float(input())

p = 0
#verificação se, o salario está de acorodo com a amplitude e calculo do salario de acorodo com a tabela da atividade 1048
if (s<=400):
    p = 15
#verificação se, o salario está de acorodo com a amplitude e calculo do salario de acorodo com a tabela da atividade 1048
elif (s<=800.00):
    p = 12
#verificação se, o salario está de acorodo com a amplitude e calculo do salario de acorodo com a tabela da atividade 1048
elif (s<=1200.00):
    p = 10
#verificação se, o salario está de acorodo com a amplitude e calculo do salario de acorodo com a tabela da atividade 1048
elif (s<=2000.00):
    p = 7
#verificação se, o salario está de acorodo com a amplitude e calculo do salario de acorodo com a tabela da atividade 1048
elif (s>2000.00):
    p = 4
    
def mostra(msg):
    print(msg)

msg='Novo salario: %.2f' %(s+(s*(p/100)))
msg +=('\nReajuste ganho: %.2f' %(s*(p/100)))
msg+=('\nEm percentual: %d %%' %p)

mostra(msg)

