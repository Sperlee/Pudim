
from button import create_button
from utils import get_text_dimensions
import constants
import pygame
from PPlay.keyboard import Keyboard
from fases.fase_2.fase2 import fase2

def create_menu(janela, mouse, menu_options):

    buttons = create_button(menu_options)

    for i in range(len(buttons)):

        
            
        buttons[i].draw()
        [text_width, text_height] = get_text_dimensions(menu_options[i], constants.MENU_FONT_SIZE)

        #Por algum motivo a palavra DIFICULDADE estava ficando mal centralizada, então fiz um ajuste só pra que ela ficasse centralizada
        if(menu_options[i] == "CONFIGURAÇÕES"):
            text_x = buttons[i].x + constants.BUTTON_WIDTH/2 - text_width/2 - 40
        else:
            text_x = buttons[i].x + constants.BUTTON_WIDTH/2 - text_width/2 -15
        text_y = constants.BUTTON_MARGIN_TOP + i * constants.BUTTON_MARGIN + constants.BUTTON_HEIGHT/2 - text_height/2 - 5
        janela.draw_text(menu_options[i], text_x, text_y, constants.MENU_FONT_SIZE, constants.TEXT_COLOR)

        if mouse.is_over_object(buttons[i]):

            janela.draw_text(menu_options[i], text_x, text_y, constants.MENU_FONT_SIZE, constants.HOVER_TEXT_COLOR)

            if mouse.is_button_pressed(1):
                return i

def handle_menu(janela, teclado, mouse, bg):

    #State vai ser a variável que vai controlar a lógica de qual menu deve ser exibido
    state = 0

    while True:

        bg.draw()

        MENU = 0
        PLAYING = 1
        DIFFICULTY = 2
        RANKING = 3
        EXIT = 4

        if state == MENU:
            menu_choice = create_menu(janela, mouse, ["JOGAR", "CONFIGURAÇÕES","SAIR"])

            match(menu_choice):
                case 0:
                    state = PLAYING
                case 1:
                    state = DIFFICULTY
                case 2:
                    state = RANKING
                case 3:
                    state = EXIT

        elif state == PLAYING:
            play(janela, mouse)

        elif state == DIFFICULTY:
            option = ["VOLTAR", "FÁCIL", "MÉDIO", "DIFÍCIL"]

            menu_choice = create_menu(janela, mouse, option)

            if (menu_choice == 0):
                #É preciso dar um delay aqui pois quando o usuário clica em voltar, o mouse ainda está sobre o botão e ele acaba clicando no botão do menu que é exibido logo em seguida
                pygame.time.wait(200)
                state = MENU

        elif state == RANKING:
            print("Ranking")
            #Não faz nada por enquanto

        elif state == EXIT:
            janela.close()
        
        if teclado.key_pressed("ESC"):
            janela.close()

        janela.update()

        
def ranking(janela, mouse, menu_options):
    while True:
        create_menu(janela, mouse, menu_options)

def play(janela, mouse):

    #Loop vazio que só vai sair quando o usuário pressionar a tecla ESC
    while True:
        if Keyboard().key_pressed("ESC"):
            break
        janela.update()

def difficulty(janela, mouse, menu_options):
    return create_menu(janela, mouse, menu_options)

    # if output == 3:
    #     menu_options[3] = 0



    




