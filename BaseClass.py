from PPlay.window import *
from PPlay.gameimage import *
import constants

class BaseClass():
    def __init__(self):
        self.janela = Window(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
        self.bg = GameImage("./assets/bg.jpeg")
        self.mouse = self.janela.get_mouse()
        self.teclado = self.janela.get_keyboard()

basic_setup = BaseClass()
