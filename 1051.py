'''
Atividade 1051
2025.06.02
Renan Soares da Silva
'''
#calcular o imposto de renda de acorodo como salario (entrada) de acorodo com a tabela da atividade 1051
#Entrada da variavel com ponto flutuante
R = float(input())
#primeiro teste para verificar se é Isento ou não
if (R<2000.00):
    #Saida da verificação caso seja Isento
    print("Isento")
#segunda verificação para definir os juros entre 2000.01 a 3000.00
elif(R<3000.00):
    #calculo e saida dos juros
    R=(R-2000.00)*(8/100)
    print('R$ %.2f' %R)
#terceira verificação para definir os juros de 3000.01 a 4500.00
elif(R<4500.00):
     #segundo calculo e saida dos juros
     R=(R-3000.00)*(18/100)+1000*(8/100)
     print( 'R$ %.2f' %R )
#caso o valor seja acima de 4500.00 sera padronizado um valor fixo de juros
else:
    #calculo do valor de juros e saida do valor.
    R=(R-4500.00)*(28/100)+1500*(18/100)+1000*(8/100)
    print( 'R$ %.2f' %R)