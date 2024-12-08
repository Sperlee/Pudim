from PPlay.window import *
from PPlay.gameimage import *
from BaseClass import basic_setup
from MenuClass import Menu
from PlayClass import Play
from PerformanceClass import PerformanceMonitor


menu = Menu()
game = Play()
perfomance_monitor = PerformanceMonitor()



# loop principal
while True:
    basic_setup.bg.draw()

    match menu.click_button_index:
        case(0):
            game.play_fase_1()
            # perfomance_monitor.measure_fps()
        case(-1):
            menu.draw_menu()




    basic_setup.janela.update()
