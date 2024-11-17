import pygame

# Inicializa o Pygame para usar suas funções de fonte
pygame.init()

def get_text_dimensions(text, font_size):
    # Cria um objeto de fonte com o tamanho especificado
    font = pygame.font.Font(None, font_size)
    
    # Renderiza o texto em uma superfície
    text_surface = font.render(text, True, (0, 0, 0))
    
    # Obtém as dimensões da superfície em um array como [largura, altura]
    return text_surface.get_size()

#Criei essa função para facilitar o ato de centralizar o texto no botão
