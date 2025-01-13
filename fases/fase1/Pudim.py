from PPlay.sprite import Sprite
from BaseClass import basic_setup


class Pudim(Sprite):
    def __init__(self):
        super().__init__("sprites/pudim/andando (1)_0001.png")
        self.set_total_duration(1000)
        # self.k = 0
        self.speed_x = 200
        self.speed_y = - 300
        self.old_speed_y = self.speed_y # velocidade anterior
        self.old_y = self.y
        self.aceleracao_pulo = 450
        # self.jump_width = 0
        self.pulando = False
        self.sprite_parado = "sprites/pudim/andando (1)_0001.png"
        self.sprite_andando_direita = "sprites/pudim/pudim_andando_direita.png"
        self.sprite_andando_esquerda = "sprites/pudim/pudim_andando_esquerda.png"
        self.k = 0 # k = 0 -> parado, k = 1 -> andando - necessario na logica do andar
        # self.sprite_pulo = "sprites/pudim.png"

    def andar(self):
        super().move_key_x(self.speed_x*basic_setup.janela.delta_time())

        x, y  = self.x, self.y
        if basic_setup.teclado.key_pressed("RIGHT") and self.k == 0:
            super().__init__(self.sprite_andando_direita, 8)
            self.set_total_duration(1000)

            self.k = 1
        elif basic_setup.teclado.key_pressed("LEFT") and self.k == 0:
            super().__init__(self.sprite_andando_esquerda, 8)
            self.set_total_duration(1000)
            self.k = 1
        elif self.k == 1 and not basic_setup.teclado.key_pressed("RIGHT") and not basic_setup.teclado.key_pressed("LEFT"):
            super().__init__(self.sprite_parado)
            self.set_total_duration(1000)
            self.k = 0

        self.set_position(x, y)
        # self.update()

    def pular(self):

        if self.speed_y < -self.old_speed_y:
            self.pulando = True
            self.y += self.speed_y * basic_setup.janela.delta_time()
            self.speed_y += self.aceleracao_pulo*basic_setup.janela.delta_time()
        else:
            self.speed_y = self.old_speed_y
            self.pulando = False
            self.y = self.old_y

    def draw(self):
        super().draw()
        self.update()
