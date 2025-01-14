from BaseClass import basic_setup
from fases.fase1.fase1 import fase_1
from PPlay.sprite import Sprite
from Transition import Transition

class Play():
    def __init__(self):
        self.tempo_texto_1 = 1
        self.tempo_texto_2 = 1
        self.acumulador = 0
        self.transicao = Transition()

        self.bg_1 = "fases/fase1/imagens/plano_de_fundo.png"
        self.bg_2 = "fases/fase_2/imagens/fundo.png"
      

        self.texto_1 = [
            "Julia e seu fiel escudeiro,", "Pudim, buscam encontrar", 
            "Pipoca, uma poodle fujona,", "que fugiu assustada com", 
            "a buzina de um navio no porto.", "", 
            "Uma senhora disse tê-la visto", "perto de alguns conteineres..."
        ]

        self.texto_2 = ["Tem alguma coisa em cima do conteiner", "que pode ser útil para pegar a Pipoca", "", "Acho que o pudim pode subir nas caixas", "e pular ali em cima para pegar o objeto..."]

        self.texto_3 = [
            "Pudim, o fiel escudeiro,", "subiu no contêiner mais alto", 
            "e avistou Pipoca correndo", "em direção ao parque próximo.", 
            "Julia agora sabe para onde ir!", "", 
            "Ajude-a a seguir Pipoca e", "continuar a busca pela sua", 
            "companheira fujona, que está", "cada vez mais perto!"
        ]

        self.texto_4 = [
        "Julia chegou ao parque e", "encontrou um grande lago.", 
        "Do outro lado, está Pipoca,", "mas há sapos pelo caminho.", 
        "Eles podem atrapalhar sua", "travessia até a poodle.", "", 
        "Ajude Julia a atravessar o", "lago e desviar dos sapos.", 
        "Pipoca está tão perto agora!", "Não desista!"
        ]

    

    def play_intro_fase_1(self):
        self.transicao.fade_out()
        basic_setup.bg.__init__(self.bg_1)
        self.transicao.fade_in()

        while self.tempo_texto_1 > 0:
            basic_setup.bg.draw()
            basic_setup.draw_pixel_text(
            self.texto_1, 
            100,  # x position 
            100,  # y position
            30,   # size
            (255,255,255),  # color
           
        )
            basic_setup.janela.update()
            self.tempo_texto_1 -= basic_setup.janela.delta_time()

        self.transicao.fade_out()


        self.transicao.fade_in()


        while self.tempo_texto_2 > 0:
            basic_setup.bg.draw()
            basic_setup.draw_pixel_text(
            self.texto_2, 
            100,  # x position 
            100,  # y position
            30,   # size
            (255,255,255),  # color
           
        )
            basic_setup.janela.update()
            self.tempo_texto_2 -= basic_setup.janela.delta_time()
        self.transicao.fade_out()
        basic_setup.bg.__init__("assets/image.png")
        self.transicao.fade_in()



    def play_intro_fase_2(self):
        self.transicao.fade_out()
        basic_setup.bg.__init__(self.bg_2)
        self.transicao.fade_in()

        while self.tempo_texto_1 > 0:
            basic_setup.bg.draw()
            basic_setup.draw_pixel_text(
            self.texto_3, 
            100,  # x position 
            100,  # y position
            30,   # size
            (255,255,255),  # color
           
        )
            basic_setup.janela.update()
            self.tempo_texto_1 -= basic_setup.janela.delta_time()

        self.transicao.fade_out()


        self.transicao.fade_in()


        while self.tempo_texto_2 > 0:
            basic_setup.bg.draw()
            basic_setup.draw_pixel_text(
            self.texto_4, 
            100,  # x position 
            100,  # y position
            30,   # size
            (255,255,255),  # color
           
        )
            basic_setup.janela.update()
            self.tempo_texto_2 -= basic_setup.janela.delta_time()
        self.transicao.fade_out()
        self.transicao.fade_in()
    
        

    def play_fase_1(self):
        
        fase_1.__init__()
        output = fase_1.run()
        return output


game = Play

