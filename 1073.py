'''
Atividade 1073
2025.06.04
Renan Soare da Silva
'''
# ler um valor iteiro e fazer o quadrado de todos os pares de 1 aé esse valor 
# entrada do valor inteiro
E = int(input())
# criação de uma variavel para que possa fazer os calculos
r = 0
# sistema de condição e repetição 
while r != E:
    # sistema de repetição que ira fazer o calculo e mostrar o resultado dos calculos
    r += 1
    if r%2 == 0:
        print("%d^2 = %d" %(r,r**2))