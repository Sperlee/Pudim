from PPlay.sprite import Sprite
from PPlay.keyboard import Keyboard
from PPlay.window import Window
from BaseClass import basic_setup
from PPlay.sound import Sound


class Julia(Sprite):
    def __init__(self, janela, x, y, speed_x, speed_y, jump_heigth):

        self.som_andar = Sound("assets/walk.ogg")
        self.som_andar.set_volume(150)


        # Chama o método __init__ da classe pai (Sprite)
        super().__init__("sprites/julia_sprites/julia_parada.png")
        self.set_position(x, y)
        self.set_total_duration(1000)
        self.k = 0
        self.speed_x = speed_x
        self.speed_y = -speed_y
        self.jump_width = jump_heigth
        self.teclado = Keyboard()
        basic_setup.janela = janela
        # Guardar as diferentes animações
        self.sprite_parado = "sprites/julia_sprites/julia_parada.png"
        self.sprite_andando_direita = "sprites/julia_sprites/julia_andando_RIGHT.png"
        self.sprite_andando_esquerda = "sprites/julia_sprites/julia_andando_LEFT.png"
        self.sprite_pulo = "sprites/julia_sprites/julia_pulo.png"

        self.is_pulando = False
        # Carregar todas as animações no início

    def andar(self, new_x, new_y):
        x, y = self.x, self.y  # Guardar posição atual
        key = ''
        
        if self.teclado.key_pressed("RIGHT"):
            key = "RIGHT"
        elif self.teclado.key_pressed("LEFT"):
            key = "LEFT"
        elif self.teclado.key_pressed("SPACE"):
            key = "SPACE"

        if (key == 'RIGHT' or key == 'LEFT') and self.k == 0:
            if key == "RIGHT":
                
                if(not self.is_pulando ):
                    
                    super().__init__(self.sprite_andando_direita, 9)
                    self.set_total_duration(1000)
                    self.set_position(new_x, new_y)
            elif key == "LEFT":
                if(not self.is_pulando):
                    super().__init__(self.sprite_andando_esquerda, 9)
                    self.set_total_duration(1000)
                    self.set_position(new_x, new_y)

            self.som_andar.play()
            # if(self.is_pulando):
            #     super().__init__(self.sprite_pulo)
            #     self.set_total_duration(1000)
            #     self.set_position(new_x, new_y)

            #Alguns contratempos foram encontrados, decisão foi de não implementar a animação de pulo


            self.k = 1
        elif (key != 'RIGHT' and key != 'LEFT') and self.k == 1:
            self.som_andar.stop()
            # Voltar para animação parada
            super().__init__(self.sprite_parado)
            self.set_total_duration(1000)
            self.set_position(new_x, new_y)
            self.k = 0

        self.set_position(x, y)  # Manter a posição
        self.move_key_x(self.speed_x * basic_setup.janela.delta_time())


    def pular(self, new_x, new_y, draw_images):

        self.is_pulando = True

        self.set_position(new_x, new_y)
        old_speed = self.speed_y

        while(self.y <= basic_setup.janela.height -113 - 143 + 5):
            
            self.y += ((self.speed_y)* basic_setup.janela.delta_time())
            self.speed_y += 700*basic_setup.janela.delta_time()
      
            self.andar(self.x, self.y)
            basic_setup.bg.draw()


            draw_images()

            self.draw()
            basic_setup.janela.update()

        self.speed_y = old_speed
        self.y = basic_setup.janela.height -113 - 143 + 5
        self.is_pulando = False

    def draw(self):
        super().draw()
        self.update()

    def call_super_init(self, image):
        super().__init__(image)
        super().set_total_duration(1000)