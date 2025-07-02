'''
Atividade 1060
2025.09.06
Renan Soares da Silva
'''
# fazer um codigo que ira ler 6 valores e ira dizer quantos deles são positivos 
# criacao de uma variavel que ira gurdar os valroes positivos
pos = 0
# estrutura de repetiçaõ que receber uma entrada e verificar se ela é positivo ou não
for i in range (6):
    # entrada
    B = float(input())
    #  sistema de verificacao e adicao a variavel pos
    if B > 0:
        pos += 1
# mostra o quantas entradas sao positivas
print(f"{pos} valores positivos")