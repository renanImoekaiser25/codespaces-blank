'''
Atividade 1114
2025.05.21
Renan Soares da Silva
'''
# criar um código com uma senha fixa sendo 2002, caso seja a senha correta deve aparecer "Acesso Permitido" , caso não,  "Senha Invalida"
#Vatiavel que ira guardar a senha fixa
Senha = 2002
# criação da variavel de entrada
entrada = 0
# verificação, se  for falso ele ira repetir todo o código apartir desse ponto, cose seja verdadeiro esse código
while (entrada != Senha):
    #entrada de uma senha qualquer
    entrada = int(input())  
     #verificação s a senha da "entrada" è igual a "senha"
    if (entrada == Senha):
       print("Acesso Permitido")
    else:
    #caso não, senha invalida.
      print("Senha Invalida")