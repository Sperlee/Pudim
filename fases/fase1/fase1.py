from Classes.Julia import Julia
from BaseClass import basic_setup
from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite


class Fase1:
    def __init__(self):
        self.julia = Julia(basic_setup.janela, 300, basic_setup.janela.height - 113 - 143 + 5, 200, 150, 100)
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

        self.cabo_guindaste = Sprite("fases/fase1/imagens/guindaste/cabo_guindaste.png")
        self.cabo_guindaste.set_position(self.guindaste_superior.x + 200, self.guindaste_superior.y)

        self.gancho = Sprite("fases/fase1/imagens/guindaste/gancho.png")
        self.gancho.set_position(self.cabo_guindaste.x - 7, self.cabo_guindaste.y + 602)

        self.guindaste_speed = 200

        self.images = [self.piso,self.conteiner, self.coluna_guindaste_esquerda, self.coluna_guindaste_direita, self.cabo_guindaste, self.gancho, self.guindaste_superior, self.painel_de_controle, self.placa_aviso]

        self.play_mode = 0 # 0 = jogo normal na plataforma ,  1 = jogo pelo guindaste

    def draw_images(self):
        for image in self.images:
            image.draw()

    def mover_guindaste(self):
            
            limite_inferior = (self.cabo_guindaste.y <= self.guindaste_superior.y) or (basic_setup.teclado.key_pressed("UP"))

            limite_superior = (self.gancho.y >= self.guindaste_superior.y + self.guindaste_superior.height + 30) or (basic_setup.teclado.key_pressed("DOWN"))

            if(limite_superior and limite_inferior):
                self.cabo_guindaste.move_key_y(self.guindaste_speed*basic_setup.janela.delta_time())
                self.gancho.move_key_y(self.guindaste_speed*basic_setup.janela.delta_time())


            limite_esquerdo = (self.gancho.x >= self.guindaste_superior.x + 200) or (basic_setup.teclado.key_pressed("RIGHT"))
            limite_direito = (self.gancho.x <= self.guindaste_superior.x + self.guindaste_superior.width - 100) or (basic_setup.teclado.key_pressed("LEFT"))

            if(limite_esquerdo and limite_direito):
                self.cabo_guindaste.move_key_x(self.guindaste_speed*basic_setup.janela.delta_time())
                self.gancho.move_key_x(self.guindaste_speed*basic_setup.janela.delta_time())

 
                


    def run(self):
        basic_setup.bg.__init__("fases/fase1/imagens/plano_de_fundo.png")

        while True:
            basic_setup.bg.draw()
            self.draw_images()
            match self.play_mode:
                case 0:
                    self.julia.andar(self.julia.x, self.julia.y)

                    if self.julia.x > self.coluna_guindaste_esquerda.x and self.julia.x < self.coluna_guindaste_esquerda.x + self.coluna_guindaste_esquerda.width - 30:
                        basic_setup.janela.draw_text("Pressione espaço para jogar pelo guindaste", 200, self.conteiner.y - 70, 50, (255, 255, 255), "Arial", True)


                    if basic_setup.teclado.key_pressed("SPACE"):
                        if self.julia.x > self.coluna_guindaste_esquerda.x and self.julia.x < self.coluna_guindaste_esquerda.x + self.coluna_guindaste_esquerda.width - 30:
                            self.play_mode = 1
                            break 
                        else:
                            self.julia.pular(self.julia.x, self.julia.y, self.draw_images)

                case 1:

                    self.mover_guindaste()

                    
                    print("jogo pelo guindaste")
                
            

            

            self.julia.draw()
            basic_setup.janela.update()

        

fase_1 = Fase1()
