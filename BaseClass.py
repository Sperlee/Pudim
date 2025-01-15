from PPlay.window import *
from PPlay.gameimage import *
import constants

import pygame

class BaseClass():
    def __init__(self):
        self.janela = Window(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
        self.bg = GameImage("./assets/bg.png")
        self.mouse = self.janela.get_mouse()
        self.teclado = self.janela.get_keyboard()
        self.pixel_font = pygame.font.Font("fontes/PressStart2P-Regular.ttf", 20)
    
    def draw_pixel_text(self, text, x, y, size, color):

        for linha in text:
            font = pygame.font.Font("fontes/PressStart2P-Regular.ttf", size)
            text = font.render(linha, True, color)
            self.janela.screen.blit(text, (x, y))
            y += 50
        # font = pygame.font.Font("fontes/PressStart2P-Regular.ttf", size)
        # text = font.render(text, True, color)
        # self.janela.screen.blit(text, (x, y))
    
    def set_scale(self,imagem, scale):

        original_image = pygame.image.load(imagem)

        resized_image = pygame.transform.scale(original_image, (original_image.get_width()*scale,original_image.get_height()*scale))

        pygame.image.save(resized_image, imagem)

basic_setup = BaseClass()
