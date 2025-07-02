'''
Atividade 1066
2025.06.04
Renan Soares da Silva
'''
# ler 5 valores inteiros e dizer quantos são pares,impares, positivos e negativos
#Entrada dos valores onterios
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
#criação das vriaveis de verificação
p = 0
n = 0
par = 0
impar = 0
#função que verifica se o numero é par/impar ou positio/negativo
def calculo(v):
    #estrutura de verificação
    if v>0:
        #transforma  a variavel local em uma variavel global onde essa variavel pode sair da função e ir ao código original e soma 1 a essa variavel
        global p
        p+=1
    #estrutura de verificação
    elif v<0:
        #transforma  a variavel local em uma variavel global onde essa variavel pode sair da função e ir ao código original e soma 1 a essa variavel
        global n
        n+=1
    #estrutura de verificação
    if v%2==0:
        #transforma  a variavel local em uma variavel global onde essa variavel pode sair da função e ir ao código original e soma 1 a essa variavel
        global par
        par+=1
    #estrutura de verificação
    elif v%2!=0:
        #transforma  a variavel local em uma variavel global onde essa variavel pode sair da função e ir ao código original e soma 1 a essa variavel
        global impar
        impar+=1
# a função sendo chamada e verificando as entradas e guardando os resultados nas variaveis de verificação
calculo(A),calculo(B),calculo(C),calculo(D),calculo(E)
# código da mensagem que ira juntar todas as variaveis de forma que é solicitada e ira mostras essas variaveis 
msg = ("%d valor(es) par(es)" %par) + ("\n%d valor(es) impar(es)" %impar) + ("\n%d valor(es) positivo(s)" %p) + ("\n%d valor(es) negativo(s)" %n)
#saida das variaveis
print(msg)