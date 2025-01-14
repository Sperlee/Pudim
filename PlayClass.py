from BaseClass import basic_setup
from fases.fase1.fase1 import fase_1
from PPlay.sprite import Sprite
from Transition import Transition

class Play():
    def __init__(self):
        self.tempo_texto_1 = 5
        self.tempo_texto_2 = 5
        self.acumulador = 0
        self.transicao = Transition()

        self.texto_1 = "assets/texto_1.png"
        self.texto_2 = "assets/texto_2.png"
    

    def play_intro_fase_1(self):

        self.transicao.fade_out()
        basic_setup.bg.__init__(self.texto_1)
        self.transicao.fade_in()

        while self.tempo_texto_1 > 0:
            basic_setup.bg.draw()
            basic_setup.janela.update()
            self.tempo_texto_1 -= basic_setup.janela.delta_time()

        self.transicao.fade_out()
        basic_setup.bg.__init__(self.texto_2)
        self.transicao.fade_in()


        while self.tempo_texto_2 > 0:
            basic_setup.bg.draw()
            basic_setup.janela.update()
            self.tempo_texto_2 -= basic_setup.janela.delta_time()




    def game(self):
        print("bhjn")

    def play_fase_1(self):
        fase_1.__init__()
        output = fase_1.run()
        return output


game = Play

