from . import constants2
from BaseClass import basic_setup


def fase2(janela,mouse,teclado):
    fundo,pudim, julia, sapo_verde, sapo_vermelho, pedras, pipoca, efeito,ponte = constants2.criar(janela)
    lista = [1,sapo_verde,pudim,julia,0,sapo_vermelho[0],sapo_vermelho[1],sapo_vermelho[2],1]
    lista_direitra = [sapo_vermelho[0],sapo_vermelho[1],sapo_vermelho[2]]
    lista_esquerda = [sapo_verde,pudim,julia]
    lista_final = [1,sapo_vermelho[0],sapo_vermelho[1],sapo_vermelho[2],0,sapo_verde,pudim,julia,1]
    speed = 500
    while True:
        c = 0
        pedras[7].draw()
        fundo.draw()
        for i in range(9):
            if ((lista[i] != 0 and lista[i] != 1) and mouse.is_over_object(lista[i]) and mouse.is_button_pressed(1)):
                constants2.pulo.play()
                for j in range(3):
                    #elementos da esquerda

                    if(lista[i] == lista_esquerda[j]):
                        #pulado somente uma pedra
                        if(i < 7 and lista[i+1] == 0):
                            speed = 700
                            while(lista[i].x <= pedras[i+1].x + 100):
                                lista[i].x += 1
                                lista[i].y -= speed*janela.delta_time()
                                speed -= 7
                                if(lista[i].collided_perfect(pedras[i+1])):
                                    break
                                lista[i].draw()
                                constants2.draw(janela, fundo, pudim, julia, sapo_verde, sapo_vermelho, pedras, pipoca, efeito,ponte)
                            #lista[i].y = pedras[2].y - lista[i].height/2
                            lista[i],lista[i+1] = lista[i+1],lista[i]

                        #pulando duas pedras
                        if(i < 7 and lista[i+2] == 0):
                            speed = 700
                            while(lista[i].x <= pedras[i+2].x + 100):
                                lista[i].x += 1
                                lista[i].y -= speed*janela.delta_time()
                                speed -= 3.4
                                if(lista[i].collided_perfect(pedras[i+2])):
                                    break
                                lista[i].draw()
                                constants2.draw(janela, fundo, pudim, julia, sapo_verde, sapo_vermelho, pedras, pipoca, efeito,ponte)
                            #lista[i].y = pedras[2].y - lista[i].height/2
                            lista[i].draw()
                            lista[i],lista[i+2] = lista[i+2],lista[i]


                for j in range(3):
                    #elementos da direita

                    if(lista[i] == lista_direitra[j]):
                        #pulando somente uma pedra
                        if(lista[i-1] == 0 and i-1 > 0):
                            speed = 700
                            while(lista[i].x >= pedras[i-1].x - 100):
                                lista[i].x -= 1
                                lista[i].y -= speed*janela.delta_time()
                                speed -= 7
                                if(lista[i].collided_perfect(pedras[i-1])):
                                    lista[i].y -= speed*janela.delta_time()
                                    break
                                lista[i].draw()
                                constants2.draw(janela, fundo, pudim, julia, sapo_verde, sapo_vermelho, pedras, pipoca, efeito,ponte)
                            #lista[i].y = pedras[2].y - lista[i].height/2
                            lista[i],lista[i-1] = lista[i-1],lista[i]


                        #pulando duas pedras
                        if(i > 2 and lista[i-2] == 0):
                            speed = 700
                            while(lista[i].x >= pedras[i-2].x - 100):
                                lista[i].x -= 1
                                lista[i].y -= speed*janela.delta_time()
                                speed -= 3.4
                                if(lista[i].collided_perfect(pedras[i-2])):
                                    break
                                lista[i].draw()
                                constants2.draw(janela, fundo, pudim, julia, sapo_verde, sapo_vermelho, pedras, pipoca, efeito,ponte)
                            lista[i].y = pedras[2].y - lista[i].height/2
                            lista[i],lista[i-2] = lista[i-2],lista[i]
        if(teclado.key_pressed("R")):
            lista = [1,sapo_verde,pudim,julia,0,sapo_vermelho[0],sapo_vermelho[1],sapo_vermelho[2],1]
            constants2.reset(janela,pudim, julia, sapo_verde, sapo_vermelho, pedras,ponte)
        for i in range(9):
            if(lista[i] == lista_final[i]):
                c+=1
        if(c == 9):
            constants2.win.play()
            break
        for i in range(1,7):
            pedras[i].draw()
        for i in range(3):
            sapo_vermelho[i].draw()
        julia.draw()
        ponte.draw()
        pudim.draw()
        sapo_verde.draw()
        pipoca.draw()
        constants2.pergaminho.draw()
        if(mouse.is_over_object(constants2.pergaminho) and mouse.is_button_pressed(1)):
            constants2.pergaminho2.draw()
            basic_setup.draw_pixel_text(constants2.vetor, 150, 200, 20,(0,0,0))
        janela.update()