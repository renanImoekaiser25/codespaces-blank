'''
Atividade 1180
inicio da atividade: 2025.06.18
termino da atividade: 2025.06.18
Renan Soares da Silva
'''
#  fazer um codigo que ira ler uma certa quantia de valore se dizer o menor valor e a sua posicao
#  primeira entrada e a criacao da lista alem da criacao das variaveis
q = int(input())
lista = list(map(int,input().split()))
p = 0
ppt = 0
po = 0
v = lista[0]
# sistema de repeticao que ira verificar qual e o menor numero
for i in range (q):
    ppt = lista [p]
    if ppt<v:
        po = p
        v = lista[p]
    p += 1    
# saida da comparacao como a atividade 1180 pede
print(f'Menor valor: {v}' + f'\nPosicao: {po}')