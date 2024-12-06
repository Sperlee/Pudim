from PPlay.window import Window
from PPlay.gameimage import GameImage
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
import constants
from menu import handle_menu

janela = Window(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
teclado = Keyboard()
mouse = Mouse()

bg = GameImage("./assets/bg.jpeg")

while True:

    bg.draw()

    handle_menu(janela, teclado, mouse, bg)

    if teclado.key_pressed("ESC"):
        janela.close()