from tkinter import *
janela = Tk()
janela.title("Cotação Atual de Moedas")
texto = Label(janela, text="Clique no botão para ver as cotações de moedas")
texto.grid(column=0, row=0, padx=10, pady=10)

janela.mainloop()



            a = [1, 2, 3]
    b = int(input())
    for b in a :
        print('as')
        
    while True:
        a = input()
        if a != nivel[0,1,2]:
            Linha()
            print('Resposta Incorreta\nTente Novamente')
            Linha()
        elif a == '1' or '2' or '3':
            break

    if barco1[1]<barco2[1]:
        primeiro = barco1
        segundo = barco2
    else:
        primeiro = barco2
        segundo = barco1
    if  primeiro[1]<barco3[1]:
        terceiro = barco3
    else:
        terceiro = segundo
        segundo = primeiro
        primeiro = barco3
    if barco1[1] == barco2[1]:
        if barco1[0]<barco2[0]:
            primeiro = barco1
            segundo = barco2
        else:
            primeiro = berco2
            segundo = barco
            
    if barco1[1] == barco3[1]:
        if barco1[0]<barco3[0]:
            primeiro = barco1
            segundo = barco3
        