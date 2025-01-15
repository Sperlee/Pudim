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
    ponte = GameImage("fases/fase_2/imagens/ponte.png")


    # Posições iniciais
    #pedras
    for i in range(1,8):
        pedras[i].x = (i-1) * 200
        pedras[i].y = janela.height - pedras[i].height + 50

    #pudim
    pudim.x = pedras[2].x + pudim.width/2
    pudim.y = janela.height - pedras[1].height -10

    #julia
    julia.x = pedras[3].x + julia.width/2 + 30
    julia.y = janela.height - pedras[1].height - julia.height/2 + 20

    #sapo_verde
    sapo_verde.x = pedras[1].x + sapo_verde.width/2
    sapo_verde.y = janela.height - pedras[1].height - 5

    #sapo_vermelho
    for i in range(3):
        sapo_vermelho[i].x = pedras[i+5].x + sapo_vermelho[i].width/2 - 20
        sapo_vermelho[i].y = janela.height - pedras[1].height - 20
    
    #lacinho
    lacinho.x = janela.width - lacinho.width
    lacinho.y = janela.height - lacinho.height - 75

    efeito.x = janela.width - lacinho.width
    efeito.y = janela.height - lacinho.height - 75

    #ponte
    ponte.x = sapo_vermelho[2].x - 10
    ponte.y = janela.height - pedras[1].height 

    return fundo, pudim, julia, sapo_verde, sapo_vermelho, pedras, lacinho, efeito, ponte

def draw(janela, fundo, pudim, julia, sapo_verde, sapo_vermelho, pedras, lacinho, efeito,ponte):
    fundo.draw()
    for i in range(1,7):
        pedras[i].draw()
    for i in range(3):
        sapo_vermelho[i].draw()
    pudim.draw()
    julia.draw()
    sapo_verde.draw()
    lacinho.draw()
    ponte.draw()
    janela.update()

def reset(janela,pudim, julia, sapo_verde, sapo_vermelho, pedras,ponte):
     #pedras
    for i in range(1,8):
        pedras[i].x = (i-1) * 200
        pedras[i].y = janela.height - pedras[i].height + 50

    #pudim
    pudim.x = pedras[2].x + pudim.width/2
    pudim.y = janela.height - pedras[1].height -10

    #julia
    julia.x = pedras[3].x + julia.width/2 + 30
    julia.y = janela.height - pedras[1].height - julia.height/2 + 20

    #sapo_verde
    sapo_verde.x = pedras[1].x + sapo_verde.width/2
    sapo_verde.y = janela.height - pedras[1].height - 5

    #sapo_vermelho
    for i in range(3):
        sapo_vermelho[i].x = pedras[i+5].x + sapo_vermelho[i].width/2 - 20
        sapo_vermelho[i].y = janela.height - pedras[1].height - 20
    #ponte
    ponte.x = sapo_vermelho[2].x - 10
    ponte.y = janela.height - pedras[1].height 