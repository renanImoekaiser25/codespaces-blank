'''
atividade 1012
inicio da atividade: 2025.06.18
termino da atividade:
Renan Soares da Silva
'''
# a partir de tres entradas fazer o calculo das areas requisitadas
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
msg = 'TRIANGULO: %.3f' %((A*C)/2)
msg +='\nCIRCULO: %.3f'  %(C**2 * 3.14159)
msg += '\nTRAPEZIO: %.3f' %((A+B)*C/2)
msg += '\nQUADRADO: %.3f'  %(B**2)
msg += '\nRETANGULO: %.3f' %(A * B)
print(msg)