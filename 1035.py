'''
Atividade 1035
2025.05.29
Renan Soares da Silva
#Caso leia este comentario, me diga que leu e assim vou começar a botar uns frases aleatorias em algumas atividade.
'''
# escrever um código que irar ler 4 valores e depois de diversas verificações dizer se todas foram atendidas ou não
#entrada dos 4 valores inteiros
A, B, C, D = input().split(" ")
A = int(A)
B = int(B)
C = int(C)
D = int(D)
#sitema de verificação e resposta caso seja true ou false
if ((B>C) and (D>A) and (C + D)>(A + B) and (C,D>0) and ((A%2)==0)):
    # caso seja verdadeiro saira que os valores forão aceitos
    print("Valores aceitos")
else:
    #caso o valor seja falso saira que os valores não foram aceitos
     print("Valores nao aceitos")