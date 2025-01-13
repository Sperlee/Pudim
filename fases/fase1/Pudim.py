from PPlay.sprite import Sprite
from BaseClass import basic_setup
import math


class Pudim(Sprite):
    def __init__(self):
        super().__init__("sprites/pudim/pudim_parado.png")
        self.set_total_duration(1000)
        # self.k = 0
        self.speed_x = 200
        self.speed_y = - 300
        self.speed_cair = 300
        self.old_speed_cair =  self.speed_cair
        self.old_speed_y = self.speed_y # velocidade anterior
        self.old_y = self.y
        self.aceleracao_pulo = 550
        # self.jump_width = 0
        self.pulando = False
        self.sprite_parado = "sprites/pudim/pudim_parado.png"
        self.sprite_andando_direita = "sprites/pudim/pudim_andando_direita.png"
        self.sprite_andando_esquerda = "sprites/pudim/pudim_andando_esquerda.png"
        self.k = 0 # k = 0 -> parado, k = 1 -> andando - necessario na logica do andar
        # self.sprite_pulo = "sprites/pudim.png"

        self.pode_cair_no_conteiner = False
        self.pode_cair = False
        self.pode_cair_na_caixa = False

    def andar(self, caixas, piso, conteiner):
        x, y = self.x, self.y
        standing = False

        # Check if standing on any surface
        for caixa in caixas:
            if (self.x + self.width > caixa.x and 
                self.x < caixa.x + caixa.width and 
                abs(self.y + self.height - caixa.y) < 5):
                standing = True
            
            if(self.collided(caixa)) and not standing and not self.pulando:
            
                self.set_position(x-1, y)
            
                return

        # Check container collision
        if (not standing and 
            self.x + self.width > conteiner.x and 
            self.x < conteiner.x + conteiner.width and 
            abs(self.y + self.height - conteiner.y) < 5):
            standing = True

        # Check floor collision
        if abs(self.y + self.height - piso.y) < 5:
            standing = True

        # Handle walking animation
        if basic_setup.teclado.key_pressed("RIGHT") and self.k == 0:
            super().__init__(self.sprite_andando_direita, 8)
            self.set_total_duration(1000)
            self.k = 1
            self.update()
        elif basic_setup.teclado.key_pressed("LEFT") and self.k == 0:
            super().__init__(self.sprite_andando_esquerda, 8)
            self.set_total_duration(1000)
            self.k = 1
            self.update()
        elif self.k == 1 and not basic_setup.teclado.key_pressed("RIGHT") and not basic_setup.teclado.key_pressed("LEFT"):
            super().__init__(self.sprite_parado)
            self.set_total_duration(1000)
            self.k = 0

        # Update position and handle falling
        self.set_position(x, y)
        super().move_key_x(self.speed_x * basic_setup.janela.delta_time())

        if not standing and not self.pulando:
            self.pulando = True
            self.speed_y = 0
        

    def pular(self, caixas, piso, conteiner):
        
        for caixa in caixas:
            if self.y + self.height < caixa.y:
                self.pode_cair_na_caixa = True
            
                
            if self.collided(caixa) and self.pulando:
                self.pode_cair = True
                self.y = caixa.y - self.height -2
                self.speed_y = self.old_speed_y
                self.pulando = False
                self.pode_cair_na_caixa = False
                return
            
        if self.collided(piso) and self.pulando:
            self.y = piso.y - self.height
            self.speed_y = self.old_speed_y
            self.pulando = False
            return
        elif self.collided(conteiner) and self.pulando and self.pode_cair_no_conteiner:
            self.y = conteiner.y - self.height
            self.speed_y = self.old_speed_y
            self.pulando = False
            return
        else:

            if self.y + self.height < conteiner.y:
                self.pode_cair_no_conteiner = True
            else:
                self.pode_cair_no_conteiner = False


            self.y += self.speed_y * basic_setup.janela.delta_time()
            self.speed_y += self.aceleracao_pulo*basic_setup.janela.delta_time()
  

    def draw(self):
        super().draw()
        self.update()
