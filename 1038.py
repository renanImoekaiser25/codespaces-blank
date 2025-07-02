'''
Atividade 1038
2025.05.21
Renan Soares da Silva
'''
# Através da tabela da atvidade, realizar um código que ira ler a tabela dependendo dos itens reuisitados e calcular o valor a pagar
#lista dos valores
Lista_valor =[4.00,4.50,5.00,2.00,1.50]
# entrada de quais valores forão escolidos
entrada1, entrada2 = input(). split(' ')
#correção dos valores
entrada1 = int(entrada1) - 1
entrada2 = int(entrada2)
# a atribuição dos valores as variaveis corretas e a soma delas
entrada3 = Lista_valor[entrada1] * entrada2
# mostra a soma dos valores e mostra o valor final.
print ("Total: R$ %.2f" %entrada3)