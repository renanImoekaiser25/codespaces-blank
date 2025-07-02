'''
Atividade 1564
2025.06.05
Renan Soares da Silva
'''
#fazer um progama que ira indentificar se ha reclamações da copa, se tiver reclamação terá duas copas e se tiver nenhuma tera uma copa
# criação da variavel que ira comportar as reclamações
R = 0  
#  sistema de repetição infinito
while (True):
    # tenta executar o código, caso de erro ele segue para o proximo código
    try:
        # entrada
        R = int(input())
        # sistema de verificação
        if R == 0:
          print("vai ter copa!")
        else:
           print("vai ter duas!")
    # estrututra que irá verificar se o código deu erro e ira quebrar/parar o código infinito do while
    except EOFError:
        break