from PPlay.keyboard import Keyboard
from PPlay.sprite import *
import fases.fase1.constants_fase1 as constants_fase1
from utils import set_scale

def fase1(janela, bg):

    teclado = Keyboard()

    bg.__init__("fases/fase1/imagens/plano_de_fundo.png")

    [piso, coluna_guindaste_esquerda, coluna_guindaste_direita, guindaste_superior, painel_de_controle, placa_aviso, conteiner] = constants_fase1.define_game_images(janela)

    julia = Sprite("sprites/julia_sprites/julia_parada.png")
    julia.set_position(100, janela.height - julia.height - piso.height + 5)
    julia.set_total_duration(1000) 


    k = 0

    while True:

        bg.draw()

    

        


        piso.draw()
        coluna_guindaste_esquerda.draw()
        coluna_guindaste_direita.draw()
        guindaste_superior.draw()
        painel_de_controle.draw()
        placa_aviso.draw()
        conteiner.draw()

        key = ''

        if(teclado.key_pressed("RIGHT")):
            key = "RIGHT"
        elif(teclado.key_pressed("LEFT")):
            key = "LEFT"
        
    

        if((key == 'RIGHT' or key == 'LEFT') and k == 0):

            [x, y] = [julia.x, julia.y]
            path = "sprites/julia_sprites/julia_andando_" + key + ".png"
            julia.__init__(path, 9)
            julia.set_position(x, y)
            julia.set_total_duration(1000) 

            k = 1
        elif((key != 'RIGHT' and key != 'LEFT')  and k == 1):
            [x, y] = [julia.x, julia.y]
            julia.__init__("sprites/julia_sprites/julia_parada.png")
            julia.set_position(x, y)
            julia.set_total_duration(1000) 

            k = 0
            
        julia.move_key_x(200*janela.delta_time())

        julia.draw()

        julia.update()

        janela.update()

