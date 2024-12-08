from Classes.Julia import Julia
from BaseClass import basic_setup
from PPlay.gameimage import GameImage


class Fase1:
    def __init__(self):
        self.julia = Julia(basic_setup.janela, 300, basic_setup.janela.height - 113 - 143 + 5, 200, 200, 100)
        self.piso = GameImage("fases/fase1/imagens/piso.png")
        self.piso.set_position(0, basic_setup.janela.height - self.piso.height)

        self.coluna_guindaste_esquerda = GameImage("fases/fase1/imagens/guindaste/coluna_guindaste.png")
        self.coluna_guindaste_esquerda.set_position(20, basic_setup.janela.height - self.piso.height - self.coluna_guindaste_esquerda.height)

        self.coluna_guindaste_direita = GameImage("fases/fase1/imagens/guindaste/coluna_guindaste.png")
        self.coluna_guindaste_direita.set_position(basic_setup.janela.width - self.coluna_guindaste_direita.width - 20, basic_setup.janela.height - self.piso.height - self.coluna_guindaste_direita.height)

        self.guindaste_superior = GameImage("fases/fase1/imagens/guindaste/guindaste_superior.png")
        self.guindaste_superior.set_position(45, self.coluna_guindaste_esquerda.y - self.guindaste_superior.height)

        self.painel_de_controle = GameImage("fases/fase1/imagens/painel_de_controle.png")
        self.painel_de_controle.set_position(self.coluna_guindaste_esquerda.x + 40, self.piso.y - self.painel_de_controle.height - 70)

        self.placa_aviso = GameImage("fases/fase1/imagens/placa_aviso.png")
        self.placa_aviso.set_position(self.painel_de_controle.x + 10, self.painel_de_controle.y - self.placa_aviso.height - 10)

        self.conteiner = GameImage("fases/fase1/imagens/conteiner.png")
        self.conteiner.set_position(basic_setup.janela.width/2 - self.conteiner.width/2, self.piso.y - self.conteiner.height + 5)

        self.images = [self.piso, self.coluna_guindaste_esquerda, self.coluna_guindaste_direita, self.guindaste_superior, self.painel_de_controle, self.placa_aviso, self.conteiner]

    def draw_images(self):
        for image in self.images:
            image.draw()


    def run(self):
        basic_setup.bg.__init__("fases/fase1/imagens/plano_de_fundo.png")

        while True:
            basic_setup.bg.draw()
            self.draw_images()
            self.julia.andar(self.julia.x, self.julia.y)

            if basic_setup.teclado.key_pressed("SPACE"):
                self.julia.pular(self.julia.x, self.julia.y, self.draw_images)

            self.julia.draw()
            basic_setup.janela.update()

fase_1 = Fase1()
