from PPlay.gameimage import GameImage

def criar(janela):
    fundo = GameImage("fases/fase_2/imagens/fundo.png")
    pudim = GameImage("fases/fase_2/imagens/pudim.png")
    julia = GameImage("fases/fase_2/imagens/julia.png")
    sapo_verde = GameImage("fases/fase_2/imagens/sapo_verde.png")
    sapo_vermelho = [GameImage("fases/fase_2/imagens/sapo_vermelho.png"), GameImage("fases/fase_2/imagens/sapo_vermelho.png"), GameImage("fases/fase_2/imagens/sapo_vermelho.png")]
    pedras = [1,GameImage("fases/fase_2/imagens/pedra.png"),GameImage("fases/fase_2/imagens/pedra.png"),GameImage("fases/fase_2/imagens/pedra.png"),GameImage("fases/fase_2/imagens/pedra.png"),GameImage("fases/fase_2/imagens/pedra.png"),GameImage("fases/fase_2/imagens/pedra.png"),GameImage("fases/fase_2/imagens/pedra.png"),1]
    lacinho = GameImage("fases/fase_2/imagens/lacinho.png")
    efeito = GameImage("fases/fase_2/imagens/efeito.png")


    # Posições iniciais
    #pedras
    for i in range(1,8):
        pedras[i].x = (i-1) * 200
        pedras[i].y = janela.height - pedras[i].height + 50

    #pudim
    pudim.x = pedras[2].x + pudim.width/2
    pudim.y = janela.height - pedras[1].height + 15

    #julia
    julia.x = pedras[3].x + julia.width/2 + 30
    julia.y = janela.height - pedras[1].height - julia.height/2 + 35

    #sapo_verde
    sapo_verde.x = pedras[1].x + sapo_verde.width/2
    sapo_verde.y = janela.height - pedras[1].height + 15

    #sapo_vermelho
    for i in range(3):
        sapo_vermelho[i].x = pedras[i+5].x + sapo_vermelho[i].width/2 - 20
        sapo_vermelho[i].y = janela.height - pedras[1].height

    return fundo, pudim, julia, sapo_verde, sapo_vermelho, pedras, lacinho, efeito

def draw(janela, fundo, pudim, julia, sapo_verde, sapo_vermelho, pedras, lacinho, efeito):
    fundo.draw()
    for i in range(1,8):
        pedras[i].draw()
    for i in range(3):
        sapo_vermelho[i].draw()
    pudim.draw()
    julia.draw()
    sapo_verde.draw()
    janela.update()
