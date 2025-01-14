from PPlay.window import *
from PPlay.sound import *
from PPlay.gameimage import *
from BaseClass import basic_setup
from MenuClass import Menu
from PlayClass import Play
from PerformanceClass import PerformanceMonitor
from fases.fase_2.fase2 import fase2
<<<<<<< HEAD
=======
from Transition import Transition

>>>>>>> 9b61ace4024e15279f41f3d21f4c856b0ec919e4

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
<<<<<<< HEAD
            fase2(basic_setup.janela,basic_setup.mouse,basic_setup.teclado)
            game.play_fase_1()
            perfomance_monitor.measure_fps()
=======

            # game.play_intro_fase_1()
            transition.fade_out()
            game.play_fase_1()
            transition.fade_in()
            fase2(basic_setup.janela, basic_setup.mouse)
            # perfomance_monitor.measure_fps()
>>>>>>> 9b61ace4024e15279f41f3d21f4c856b0ec919e4
        case(-1):
            menu.draw_menu()




    basic_setup.janela.update()
