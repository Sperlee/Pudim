from . import constants2


def fase2(janela,mouse):
    fundo,pudim, julia, sapo_verde, sapo_vermelho, pedras, lacinho, efeito = constants2.criar(janela)
    lista = [1,sapo_verde,pudim,julia,0,sapo_vermelho[0],sapo_vermelho[1],sapo_vermelho[2],1]
    lista_direitra = [sapo_vermelho[0],sapo_vermelho[1],sapo_vermelho[2]]
    lista_esquerda = [sapo_verde,pudim,julia]
    lista_final = [1,sapo_vermelho[0],sapo_vermelho[1],sapo_vermelho[2],0,sapo_verde,pudim,julia,1]
    speed = 500
    while True:
        c = 0
        fundo.draw()
        for i in range(9):
            if ((lista[i] != 0 and lista[i] != 1) and mouse.is_over_object(lista[i]) and mouse.is_button_pressed(1)):
                for j in range(3):
                    if(lista[i] == lista_esquerda[j]):
                        if(i < 7 and lista[i+1] == 0):
                            speed = 500
                            while(lista[i].x <= pedras[i+1].x + lista[i].width/2):
                                lista[i].x += 1
                                if(lista[i].y <= janela.height - pedras[2].height - 20):
                                    lista[i].y -= speed*janela.delta_time()
                                speed -= 6
                                lista[i].draw()
                                constants2.draw(janela, fundo, pudim, julia, sapo_verde, sapo_vermelho, pedras, lacinho, efeito)
                            lista[i].y = pedras[2].y - lista[i].height/2
                            lista[i],lista[i+1] = lista[i+1],lista[i]
                        if(i < 7 and lista[i+2] == 0):
                            speed = 500
                            while(lista[i].x <= pedras[i+2].x + lista[i].width/2):
                                lista[i].x += 1
                                if(lista[i].y <= pedras[2].y):
                                    lista[i].y -= speed*janela.delta_time()
                                speed -= 3
                                lista[i].draw()
                                constants2.draw(janela, fundo, pudim, julia, sapo_verde, sapo_vermelho, pedras, lacinho, efeito)
                            lista[i].y = pedras[2].y - lista[i].height/2
                            lista[i].draw()
                            lista[i],lista[i+2] = lista[i+2],lista[i]
                for j in range(3):
                    if(lista[i] == lista_direitra[j]):
                        if(lista[i-1] == 0 and i-1 > 0):
                            speed = 500
                            while(lista[i].x >= pedras[i-1].x + lista[i].width/2):
                                lista[i].x -= 1
                                if(lista[i].y <= pedras[2].y):
                                    lista[i].y -= speed*janela.delta_time()
                                speed -= 6
                                lista[i].draw()
                                constants2.draw(janela, fundo, pudim, julia, sapo_verde, sapo_vermelho, pedras, lacinho, efeito)
                            lista[i].y = pedras[2].y - lista[i].height/2
                            lista[i],lista[i-1] = lista[i-1],lista[i]
                        if(i > 2 and lista[i-2] == 0):
                            speed = 500
                            while(lista[i].x >= pedras[i-2].x + lista[i].width/2):
                                lista[i].x -= 1
                                if(lista[i].y <= pedras[2].y):
                                    lista[i].y -= speed*janela.delta_time()
                                speed -= 3
                                lista[i].draw()
                                constants2.draw(janela, fundo, pudim, julia, sapo_verde, sapo_vermelho, pedras, lacinho, efeito)
                            lista[i].y = pedras[2].y - lista[i].height/2
                            lista[i],lista[i-2] = lista[i-2],lista[i]
        
        for i in range(9):
            if(lista[i] == lista_final[i]):
                c+=1
        if(c == 9):
            janela.close()

    
        for i in range(1,8):
            pedras[i].draw()
        for i in range(3):
            sapo_vermelho[i].draw()
        pudim.draw()
        julia.draw()
        sapo_verde.draw()
        janela.update()