'''
Atividade 1010
2025.05.19
Renan Soares da Silva
'''
#ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
# sitema que separa e atribui um valor as variaveis
peca, quantidade, valor = input().split(' ')
quantidade = int(quantidade)
valor = float(valor)
# sitema que separa e atribui um valor as variaveis
peca2 , quantidade2 , valor2 = input().split(' ')
quantidade2 = int(quantidade2)
valor2 = float(valor2)
#calculao valor a pagar
vpagar = (valor*quantidade) + (valor2*quantidade2)
#Mostra o valor a pagar
print("VALOR A PAGAR: R$ %.2f" %vpagar)
