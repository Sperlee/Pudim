from PPlay.window import *
from PPlay.sound import *
from PPlay.gameimage import *
from BaseClass import basic_setup
from MenuClass import Menu
from PlayClass import Play
from PerformanceClass import PerformanceMonitor
from fases.fase_2.fase2 import fase2
from Transition import Transition


menu = Menu()
game = Play()
perfomance_monitor = PerformanceMonitor()

musica = Sound("Lake Jupiter - John Patitucci (online-audio-converter.com).ogg")
musica.loop = True
musica.play()


transition = Transition()


# loop principal
while True:
    basic_setup.bg.draw()

    match menu.click_button_index:
        case(0):
            #game.play_intro_fase_1()
            #game.play_fase_1()
            #game.play_intro_fase_2()
            fase2(basic_setup.janela,basic_setup.mouse,basic_setup.teclado)
        case(-1):
            menu.draw_menu()




    basic_setup.janela.update()
