from PPlay.gameimage import GameImage

def define_game_images(janela):
    piso = GameImage("fases/fase1/imagens/piso.png")
    piso.set_position(0, janela.height - piso.height)
    coluna_guindaste_esquerda = GameImage("fases/fase1/imagens/guindaste/coluna_guindaste.png")
    coluna_guindaste_esquerda.set_position(20, janela.height - piso.height - coluna_guindaste_esquerda.height)

    coluna_guindaste_direita = GameImage("fases/fase1/imagens/guindaste/coluna_guindaste.png")
    coluna_guindaste_direita.set_position(janela.width - coluna_guindaste_direita.width - 20, janela.height - piso.height - coluna_guindaste_direita.height) 
    guindaste_superior = GameImage("fases/fase1/imagens/guindaste/guindaste_superior.png")
    guindaste_superior.set_position(45, coluna_guindaste_esquerda.y - guindaste_superior.height)

    painel_de_controle = GameImage("fases/fase1/imagens/painel_de_controle.png")
    painel_de_controle.set_position(coluna_guindaste_esquerda.x + 40, piso.y - painel_de_controle.height - 70)

    placa_aviso = GameImage("fases/fase1/imagens/placa_aviso.png")
    placa_aviso.set_position(painel_de_controle.x + 10, painel_de_controle.y - placa_aviso.height - 10)

    conteiner = GameImage("fases/fase1/imagens/conteiner.png")
    conteiner.set_position(janela.width/2 - conteiner.width/2, piso.y - conteiner.height + 5)

    return [piso, coluna_guindaste_esquerda, coluna_guindaste_direita, guindaste_superior, painel_de_controle, placa_aviso, conteiner]