'''
Ativade 1013
2025.05.28
Rena Soares da Silva
'''
# fazer um programa para João que calcule a quantidade de combustivel gasto de acorodo com as horas e km/H sendo que o carro dele faz 12 km/l( joão bem preguisoço, nei pra me pagar pelo código, pode nn)
#entrada dos valores de hora e km/h, respectivamente
x = int(input())
y = int(input())
#calculo da qunatidade de km percorrido e o consumo de gasolina
km = x * y
km_l = km/ 12
#mostra a quantidade de gasolina necessaria
print(f"{km_l:.3f}")