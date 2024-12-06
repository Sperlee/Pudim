from PPlay.keyboard import Keyboard
from Classes.Julia import Julia
import fases.fase1.constants_fase1 as constants_fase1
from utils import set_scale

def fase1(janela, bg):

    teclado = Keyboard()

    bg.__init__("fases/fase1/imagens/plano_de_fundo.png")

    images = constants_fase1.define_game_images(janela)

    julia = Julia(janela, 100, janela.height - 113 - 143 + 5, 200, 200, 100)


    while True:

        bg.draw()

        constants_fase1.draw_images(images)

        julia.andar(julia.x, julia.y)

        if(teclado.key_pressed("SPACE")):
            julia.pular(julia.x, julia.y, bg, constants_fase1.draw_images, images)
        
        julia.draw()

        janela.update()

