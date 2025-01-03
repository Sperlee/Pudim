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
        self.cabo_guindaste.set_position(self.guindaste_superior.x + 1000, self.guindaste_superior.y)

        self.gancho = Sprite("fases/fase1/imagens/guindaste/gancho.png")
        self.gancho.set_position(self.cabo_guindaste.x - 7, self.cabo_guindaste.y + 602)

        self.guindaste_speed = 200

        self.images = [self.piso,self.conteiner, self.coluna_guindaste_esquerda, self.coluna_guindaste_direita, self.cabo_guindaste, self.gancho, self.guindaste_superior, self.painel_de_controle, self.placa_aviso]

        self.caixas = [Sprite("fases/fase1/imagens/caixa1.png"), Sprite("fases/fase1/imagens/caixa2.png"), Sprite("fases/fase1/imagens/caixa3.png"), Sprite("fases/fase1/imagens/caixa4.png"), Sprite("fases/fase1/imagens/caixa5.png")]

        self.divs = [GameImage("fases/fase1/imagens/divisoria.png"), GameImage("fases/fase1/imagens/divisoria.png"), GameImage("fases/fase1/imagens/divisoria.png"), GameImage("fases/fase1/imagens/divisoria.png")]

        for i in range(len(self.divs)):
            self.divs[i].set_position(200 + i*450 - 10, self.piso.y - self.divs[i].height)

        self.play_mode = 0 # 0 = jogo normal na plataforma ,  1 = jogo pelo guindaste

        self.movendo_caixa = [False, -1] #a segunda posicao é para saber qual caixa esta sendo movida

    def draw_images(self):
        for image in self.images:
            image.draw()
        for caixa in self.caixas:
            caixa.draw()
        for div in self.divs:
            div.draw()

    def set_caixas_position(self):

        self.caixas[4].set_position(1100, self.piso.y - self.caixas[4].height)
        for i in range(len(self.caixas)-2, -1, -1):
            self.caixas[i].y = self.caixas[i+1].y - self.caixas[i].height + 10
            self.caixas[i].x = self.caixas[i+1].x +50

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

            if(basic_setup.teclado.key_pressed("ESC")):
                self.play_mode = 0

    def qual_divisoria(self, caixa):

        div1 = -1
        for i in range(len(self.divs)-1):

            
            if caixa.x >= self.divs[i].x + self.divs[i].width and caixa.x + caixa.width < self.divs[i+1].x:
                div1 = i + 1
           
        return div1


    def pode_soltar_caixa(self, index):

        if index == 0 and self.qual_divisoria(self.caixas[index])== -1:
            return False


        for i in range(index, 0, -1):
            div1 = self.qual_divisoria(self.caixas[index])
            div2 = self.qual_divisoria(self.caixas[i-1])

            if div1 == -1 or div2 == -1 or div1 == div2:
                return False
        return True

        
    
    def pode_pegar_caixa(self, index):

        if index == 0:
            return True
    
        
        for i in range(index, 0, -1):
            div1 = self.qual_divisoria(self.caixas[index])
            div2 = self.qual_divisoria(self.caixas[i-1])
            if self.caixas[index].y > self.caixas[i-1].y and div1 == div2:
                return False
            
        return True
    
    



    def run(self):
        basic_setup.bg.__init__("fases/fase1/imagens/plano_de_fundo.png")
        self.set_caixas_position()


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
                            x, y = self.julia.x, self.julia.y
                            self.julia.call_super_init("sprites/julia_sprites/julia_costas.png")
                            self.julia.set_position(x, y)
                            break 
                        else:
                            self.julia.pular(self.julia.x, self.julia.y, self.draw_images)

                case 1:

                    self.mover_guindaste()

                    for index, caixa in enumerate(self.caixas):
                        if(self.gancho.collided(caixa) and basic_setup.teclado.key_pressed("C") and not self.movendo_caixa[0] ):
                           
                            if self.pode_pegar_caixa(index):
                                self.movendo_caixa = [True, index]

                        elif basic_setup.teclado.key_pressed("D") and self.movendo_caixa[0]:
                            if self.pode_soltar_caixa(self.movendo_caixa[1]):
                                self.movendo_caixa = [False, -1]
                            




                        # print(self.movendo_caixa)

                        if (self.movendo_caixa[0] and index == self.movendo_caixa[1]) and (not caixa.collided(self.guindaste_superior) or basic_setup.teclado.key_pressed("DOWN")) and (not caixa.collided(self.piso) or basic_setup.teclado.key_pressed("UP")):
                            caixa.move_key_x(self.guindaste_speed*basic_setup.janela.delta_time())
                            caixa.move_key_y(self.guindaste_speed*basic_setup.janela.delta_time())

                        # elif self.movendo_caixa[0]  and (self.movendo_caixa[1] ==  0 or ((abs(self.caixas[self.movendo_caixa[1]].x - self.caixas[self.movendo_caixa[1]-1].x) > 300) and (self.movendo_caixa[1]< index and self.caixas[self.movendo_caixa[1]].y < self.caixas[self.movendo_caixa[1]+ 1].y))):
                        #     basic_setup.janela.draw_text("Aqui tu pode soltar a caixa", 200, self.conteiner.y - 70, 50, (255, 255, 255), "Arial", True)
                        #     if basic_setup.teclado.key_pressed("D"):
                        #         self.movendo_caixa = [False, -1]


                        # else:
                        #     basic_setup.janela.draw_text("Aqui tu NAO pode soltar a caixa", 200, self.conteiner.y - 70, 50, (255, 255, 255), "Arial", True)


                   

                    
                    # print("jogo pelo guindaste")
                
            

            

            self.julia.draw()
            basic_setup.janela.update()



        

fase_1 = Fase1()
