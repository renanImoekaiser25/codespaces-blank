'''
Ativade 1013
2025.05.28
Rena Soares da Silva
'''
#calcular o valor da entrada na menor quantidade cedulas possiveis sendo que as cedulas são; 100, 50, 20, 10, 5, 2 , 1
#entrada de um numero inteiro para o calculo das cedulas
I = int(input())
Iverdadeiro = I
N100 = I//100
I = I %100
N50 = I//50
I = I%50
N20 = I// 20
I = I%20
N10 = I//10
I = I%10
N5 = I//5
I = I%5
N2 = I//2
I = I%2
N1 = I//1
I = I%1
 
print(Iverdadeiro)
print('%d nota(s) de R$ 100,00' %N100)
print('%d nota(s) de R$ 50,00' %N50)
print('%d nota(s) de R$ 20,00' %N20)
print('%d nota(s) de R$ 10,00' %N10)
print('%d nota(s) de R$ 5,00' %N5)
print('%d nota(s) de R$ 2,00' %N2)
print('%d nota(s) de R$ 1,00' %N1)
