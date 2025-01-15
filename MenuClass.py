from PPlay.gameimage import GameImage
from utils import get_text_dimensions
import constants
from BaseClass import basic_setup
import pygame


class Menu():
    def __init__(self):
        self.janela = basic_setup.janela
        self.teclado = basic_setup.teclado
        self.mouse = basic_setup.mouse
        
        self.current_buttons_words = ["START", "SAIR"]
        self.current_buttons = [GameImage("./assets/button.png") for i in range(len(self.current_buttons_words))]
        self.click_button_index = -1
        

    def set_buttons_position(self):
        y = constants.BUTTON_MARGIN_TOP  # Posição inicial para o primeiro botão
        margin = constants.BUTTON_MARGIN  # Margem entre os botões
                
        # Lista com os nomes dos botões        
        # Criando os objetos GameImage e atribuindo suas posições
        for button in self.current_buttons:
    
            button.set_position(constants.BUTTON_WIDTH / 2, y)
            
            # Atualiza a posição y para o próximo botão, somando a margem
            y += margin
    
    def create_menu(self):

        self.set_buttons_position()

        for i in range(len(self.current_buttons)):
            self.current_buttons[i].draw()
            [text_width, text_height] = get_text_dimensions(self.current_buttons_words[i], constants.MENU_FONT_SIZE)

            #Por algum motivo a palavra DIFICULDADE estava ficando mal centralizada, então fiz um ajuste só pra que ela ficasse centralizada
            if(self.current_buttons_words[i] == "DIFICULDADE"):
                text_x = self.current_buttons[i].x + constants.BUTTON_WIDTH/2 - text_width/2 - 50
            else:
                text_x = self.current_buttons[i].x + constants.BUTTON_WIDTH/2 - text_width/2 - 50
            text_y = constants.BUTTON_MARGIN_TOP + i * constants.BUTTON_MARGIN + constants.BUTTON_HEIGHT/2 - text_height/2 - 10
            basic_setup.draw_pixel_text([self.current_buttons_words[i]], text_x, text_y, constants.MENU_FONT_SIZE, constants.TEXT_COLOR)

            if self.mouse.is_over_object(self.current_buttons[i]):

                basic_setup.draw_pixel_text([self.current_buttons_words[i]], text_x, text_y, constants.MENU_FONT_SIZE, constants.HOVER_TEXT_COLOR)

                if self.mouse.is_button_pressed(1):
                    self.click_button_index = i
                    pygame.time.delay(100)

    def draw_menu(self):

        self.create_menu()

        basic_setup.janela.update()

        if self.click_button_index != -1:
            return self.click_button_index