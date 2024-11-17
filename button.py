import pygame
import constants
from PPlay.gameimage import GameImage

def create_button(menu_options):

    buttons = len(menu_options)*[None]

    #Criação de uma GameImage para cada botão em menu_options seguindo os valores das constantes definidas em constants.py
    for index in range(len(menu_options)):

        button = GameImage("./assets/button.png")
        button.set_position(constants.WINDOW_WIDTH/2 - constants.BUTTON_WIDTH/2, constants.BUTTON_MARGIN_TOP + index * constants.BUTTON_MARGIN)

        buttons[index] = button

    return buttons
