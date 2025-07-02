'''
Atividade 1099
inicio da atividade: 2025.06.16
fim da atividade: 2025.06.16
Renan Soares da Silva
'''
# fazer um programa que ira ler o primeiro valor que dira quantas vezes o codigo ira se repetir e veriificar duas novas entradas a cada repetição e somar todos os números ínpares entre esses valores
# entrada de quantas vezes o código deve se repetir e tabem a criaçãõ da vriavel que ira guarda o valor da soma dos numeros negativos 
R = int(input())
VA = 0
# sistema de repetição baseado com a entrada
for i in range (R):
    # entrada dos valores que devem ser verificados e correção de stg para int
    A, B = input().split(" ")
    A = int(A)
    B = int(B)
    # primeiro sistema principal de verificação para  caso as entradas sejam iguais mostre que não tem numeros ímpares entre eles (0)
    if A == B:
        print(0)
    # segundo e ultimo sistema pricipal de verificação
    else:
        # primeiro sub sistema de verificação que, ira verificar a soma de todos os numeros ímpares se a aprimeira entrada for maior que a segunda e ira mostrar o resultado
        if A > B :
            if A % 2 != 0:
                A -= 1
            while B != A:
                B += 1
                if B % 2 != 0:
                    VA += B
            print(VA)
        # segundo sub sistema que verifica e soma dos numeros ímpares entre a entrada B  e A snedo B > A
        else:
            if B % 2 != 0:
                B -= 1
            while A != B:
                A += 1
                if A % 2 != 0:
                    VA += A
            print(VA)

    VA = 0