from Classes.Julia import Julia
from BaseClass import basic_setup
from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite
from fases.fase1.Pudim import Pudim
import pygame
import math
from Transition import Transition
from PPlay.sound import Sound

class Fase1:
    def __init__(self):

        self.som_pulo = Sound("assets/sound_jump.ogg")
        self.som_pulo.set_volume(150)

        self.som_guindaste = Sound("assets/som_guindaste.ogg")
        self.som_guindaste_active = False

        self.som_vitoria = Sound("assets/level-win.mp3")
        self.som_vitoria.set_volume(150)
        self.tempo_vitoria = 1.5
        self.transicao = Transition()
        

        #Elementos da cena
        self.piso = GameImage("fases/fase1/imagens/piso.png")
        self.piso.set_position(0, basic_setup.janela.height - self.piso.height)

        self.julia = Julia(basic_setup.janela, 300, basic_setup.janela.height - 113 - 143 + 5, 200, 150, 100)

        self.pudim = Pudim()
        self.pudim.set_position(400, self.piso.y - self.pudim.height + 10)
        print(self.piso.y - self.pudim.height + 10)

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
        

        #Elementos do guindaste
        self.cabo_guindaste = Sprite("fases/fase1/imagens/guindaste/cabo_guindaste.png")
        self.cabo_guindaste.set_position(self.guindaste_superior.x + 1000, self.guindaste_superior.y)

        self.gancho = Sprite("fases/fase1/imagens/guindaste/gancho.png")
        self.gancho.set_position(self.cabo_guindaste.x - 7, self.cabo_guindaste.y + 602)

        self.guindaste_speed = 400

        #Lista de imagens para renderizar a uma
        self.images = [self.piso,self.conteiner, self.coluna_guindaste_esquerda, self.coluna_guindaste_direita, self.cabo_guindaste, self.gancho, self.guindaste_superior, self.painel_de_controle, self.placa_aviso]

        #Elementos das caixas
        self.caixas = [Sprite("fases/fase1/imagens/caixa1.png"), Sprite("fases/fase1/imagens/caixa2.png"), Sprite("fases/fase1/imagens/caixa3.png"), Sprite("fases/fase1/imagens/caixa4.png"), Sprite("fases/fase1/imagens/caixa5.png")]

        self.movendo_caixa = [False, -1] #a segunda posicao é para saber qual caixa esta sendo movida
        self.caixa_caindo = [False, -1]
        self.caixa_caindo_speed = 400


        #Elementos das divisorias das caixas
        self.divs = [GameImage("fases/fase1/imagens/divisoria.png"), GameImage("fases/fase1/imagens/divisoria.png"), GameImage("fases/fase1/imagens/divisoria.png"), GameImage("fases/fase1/imagens/divisoria.png")]

        for i in range(len(self.divs)):
            self.divs[i].set_position(200 + i*450 - 10, self.piso.y - self.divs[i].height)

        self.play_mode = 0 # 0 = jogo com Julia , 1 = jogo com o pudim, 2 = jogo pelo guindaste



        self.texto_guindaste = GameImage("fases/fase1/imagens/texto_guindaste.png")
        self.texto_manual = GameImage("fases/fase1/imagens/manual.png")

        #Objetivo
        self.coleira = Sprite("fases/fase1/imagens/coleira.png")
        self.coleira.set_position(self.conteiner.x + self.conteiner.width/2 + 40, self.conteiner.y - self.coleira.height -30)

        self.coleira_speed = 200


        #Coisas do manual de regrass

        self.manual = GameImage("fases/fase1/imagens/pergaminho_manual.png")
        self.manual.set_position(basic_setup.janela.width - self.manual.width - 50 , basic_setup.janela.height - self.manual.height - 25)
        # basic_setup.set_scale("fases/fase1/imagens/pergaminho_manual.png", 0.9)

        self.pergaminho_regras = GameImage("fases/fase1/imagens/regras.png")
        self.pergaminho_regras.set_position(25 ,50)
        # basic_setup.set_scale("fases/fase1/imagens/regras.png", 1.1)

        self.texto_regras = ["1. Use as setas para mover a Julia", "2. Apertando a letra 'O' você assume o controle do outro personagem", "3. Use a barra de espaço para pular com o pudim", "4. Use a barra de espaço para controlar o guindaste com a Julia", "5. Quando controlando o guindaste, use a tecla 'A' para pegar uma caixa", "e a tecla 'D' para soltá-la", "6. Caixas maiores não podem ficar em cima de caixas menores"]

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
                if not self.som_guindaste_active:
                    self.som_guindaste.play()
                    self.som_guindaste_active = True
                self.cabo_guindaste.move_key_y(self.guindaste_speed*basic_setup.janela.delta_time())
                self.gancho.move_key_y(self.guindaste_speed*basic_setup.janela.delta_time())
            else:
                self.som_guindaste.stop()
                self.som_guindaste_active = False


            limite_esquerdo = (self.gancho.x >= self.guindaste_superior.x + 200) or (basic_setup.teclado.key_pressed("RIGHT"))
            limite_direito = (self.gancho.x <= self.guindaste_superior.x + self.guindaste_superior.width - 100) or (basic_setup.teclado.key_pressed("LEFT"))

            if(limite_esquerdo and limite_direito):
                if not self.som_guindaste_active:
                    self.som_guindaste.play()
                    self.som_guindaste_active = True
                self.cabo_guindaste.move_key_x(self.guindaste_speed*basic_setup.janela.delta_time())
                self.gancho.move_key_x(self.guindaste_speed*basic_setup.janela.delta_time())
            else:
                self.som_guindaste.stop()
                self.som_guindaste_active = False
            if(basic_setup.teclado.key_pressed("ESC")):
                self.play_mode = 0

    def mover_caixa(self):
            
            index = self.movendo_caixa[1]
            
            limite_inferior = (self.caixas[index].y + self.caixas[index].width <= self.piso.y) or (basic_setup.teclado.key_pressed("UP"))

            limite_superior = (self.caixas[index].y >= self.guindaste_superior.y + self.guindaste_superior.height + 30) or (basic_setup.teclado.key_pressed("DOWN"))

            if(limite_superior and limite_inferior):
                self.caixas[index].move_key_y(self.guindaste_speed*basic_setup.janela.delta_time())


            limite_esquerdo = (self.caixas[index].x >= self.guindaste_superior.x + 200) or (basic_setup.teclado.key_pressed("RIGHT"))
            limite_direito = (self.caixas[index].x <= self.guindaste_superior.x + self.guindaste_superior.width - 100) or (basic_setup.teclado.key_pressed("LEFT"))

            if(limite_esquerdo and limite_direito):
                self.caixas[index].move_key_x(self.guindaste_speed*basic_setup.janela.delta_time())

    def qual_divisoria(self, caixa):

        div1 = -1
        for i in range(len(self.divs)-1):

            
            if caixa.x >= self.divs[i].x + self.divs[i].width and caixa.x + caixa.width < self.divs[i+1].x:
                div1 = i + 1
        
        if(self.caixas.index(caixa) == 4 and caixa.x >= self.divs[2].x):
            div1 = 3

           
        return div1


    def pode_soltar_caixa(self, index):

        if index == 0 and self.qual_divisoria(self.caixas[index])== -1:
            return False


        for i in range(index, 0, -1):
            div1 = self.qual_divisoria(self.caixas[index])
            div2 = self.qual_divisoria(self.caixas[i-1])
            

            if (div1 == -1 or div2 == -1 or div1 == div2) and not (self.caixas[index].x > self.caixas[i-1].x and self.caixas[index].x + self.caixas[index].width < self.caixas[i-1].x + self.caixas[i-1].width):
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
                        self.texto_guindaste.set_position(110, self.conteiner.y - 70)
                        self.texto_guindaste.draw()


                    if basic_setup.teclado.key_pressed("SPACE"):
                        if self.julia.x > self.coluna_guindaste_esquerda.x and self.julia.x < self.coluna_guindaste_esquerda.x + self.coluna_guindaste_esquerda.width - 30:
                            self.play_mode = 2
                            x, y = self.julia.x, self.julia.y
                            self.julia.call_super_init("sprites/julia_sprites/julia_costas.png")
                            self.julia.set_position(x, y)
                          
                    if basic_setup.teclado.key_pressed("O"):
                        self.play_mode = 1
                        pygame.time.delay(500)
                
                case 1:
                    self.pudim.andar(self.caixas, self.piso, self.conteiner)

                    if basic_setup.teclado.key_pressed("O") and not self.pudim.pulando:
                        self.play_mode = 0
                        pygame.time.delay(100)
                    elif basic_setup.teclado.key_pressed("SPACE") or self.pudim.pulando:
                       
                        if(self.pudim.pulando == False):
                            self.som_pulo.play()
                            self.pudim.old_y = self.pudim.y
                            self.pudim.pulando = True
                        self.pudim.pular(self.caixas, self.piso, self.conteiner)
                 



                case 2:
                    # self.texto_manual.set_position(150, self.conteiner.y - 70)
                    # self.texto_manual.draw()

                    self.mover_guindaste()

                    for index, caixa in enumerate(self.caixas):
                        if(self.gancho.collided(caixa) and basic_setup.teclado.key_pressed("A") and not self.movendo_caixa[0] and not self.caixa_caindo[0]):
                           
                            if self.pode_pegar_caixa(index):
                                self.movendo_caixa = [True, index]

                        elif self.caixa_caindo[0] and index != self.caixa_caindo[1] and self.caixas[self.caixa_caindo[1]].collided(caixa):
                            self.caixa_caindo = [False, -1]
                            self.caixa_caindo_speed = 200


            

                    if basic_setup.teclado.key_pressed("D") and self.movendo_caixa[0] and self.pode_soltar_caixa(self.movendo_caixa[1]):
                        
                        self.caixa_caindo = [True,  self.movendo_caixa[1]]

                        self.movendo_caixa = [False, -1]


                    if self.caixa_caindo[0]:
                        self.caixas[self.caixa_caindo[1]].y += (self.caixa_caindo_speed*basic_setup.janela.delta_time())

                        self.caixa_caindo_speed += 500*basic_setup.janela.delta_time()

                        if self.caixas[self.caixa_caindo[1]].y >= self.piso.y - self.caixas[self.caixa_caindo[1]].height:
                            self.caixa_caindo = [False, -1]
                            self.caixa_caindo_speed = 200

                    elif (self.movendo_caixa[0]):
                        self.mover_caixa()

                    
            self.julia.draw()
            self.pudim.draw()
            self.coleira.draw()
            self.manual.draw()
            self.coleira.move_y(math.sin(self.coleira_speed*basic_setup.janela.delta_time())*0.1)
            self.coleira_speed += 500*basic_setup.janela.delta_time()

            if basic_setup.mouse.is_over_object(self.manual):
                self.manual.set_position(basic_setup.janela.width - self.manual.width - 55 , basic_setup.janela.height - self.manual.height - 30)

                self.pergaminho_regras.draw()
                basic_setup.draw_pixel_text(self.texto_regras, self.pergaminho_regras.x+200, self.pergaminho_regras.y+175, 15, (0,0,0))
            else:
                self.manual.set_position(basic_setup.janela.width - self.manual.width - 50 , basic_setup.janela.height - self.manual.height - 25)

            if self.pudim.collided(self.coleira):
                self.som_vitoria.play()
                while self.tempo_vitoria > 0:
                    basic_setup.bg.draw()
                    self.draw_images()
                    self.julia.draw()
                    self.pudim.draw()
                    self.coleira.draw()
                    self.manual.draw()
                    self.tempo_vitoria -= basic_setup.janela.delta_time()
                    basic_setup.janela.update()
                
                return -1
            
            basic_setup.janela.update()




fase_1 = Fase1()
