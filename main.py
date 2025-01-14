from PPlay.window import *
from PPlay.gameimage import *
from BaseClass import basic_setup
from MenuClass import Menu
from PlayClass import Play
from PerformanceClass import PerformanceMonitor
from fases.fase_2.fase2 import fase2

menu = Menu()
game = Play()
perfomance_monitor = PerformanceMonitor()



# loop principal
while True:
    basic_setup.bg.draw()

    match menu.click_button_index:
        case(0):
            fase2(basic_setup.janela,basic_setup.mouse,basic_setup.teclado)
            game.play_fase_1()
            perfomance_monitor.measure_fps()
        case(-1):
            menu.draw_menu()




    basic_setup.janela.update()
