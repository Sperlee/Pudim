from BaseClass import basic_setup
import pygame

class Transition:
    def __init__(self):
        self.fade_surface = pygame.Surface((basic_setup.janela.width, basic_setup.janela.height))
        self.fade_surface.fill((0, 0, 0))
        self.alpha = 0
        self.fade_surface.set_alpha(self.alpha)

    def fade_out(self, speed=200):
        done = False
        while not done:
            self.alpha += speed*basic_setup.janela.delta_time()
            if self.alpha >= 255:
                self.alpha = 255
                done = True
                
            self.fade_surface.set_alpha(self.alpha)
            basic_setup.bg.draw()
            basic_setup.janela.get_screen().blit(self.fade_surface, (0,0))
            basic_setup.janela.update()

    def fade_in(self, speed=200):
        done = False
        while not done:
            
            self.alpha -= speed*basic_setup.janela.delta_time()
            if self.alpha <= 0:
                self.alpha = 0
                done = True
                
            self.fade_surface.set_alpha(self.alpha)
            basic_setup.bg.draw()
            basic_setup.janela.get_screen().blit(self.fade_surface, (0,0))
            basic_setup.janela.update()

