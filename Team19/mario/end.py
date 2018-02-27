import pygame
from settings import *
from os import path
import time

#dimensions
W = 800
H = 600

#declaring image directory
img_dir = path.join(path.dirname(__file__), 'img')

score = 0
screen = pygame.display.set_mode((W, H))

end_img = pygame.image.load("end.jpg").convert()
end_img = pygame.transform.scale(end_img, (W, H))

font_name = pygame.font.match_font('Gumball')
font1 = pygame.font.match_font('arial')

#defining a function to print text on thr screen
def draw_text(surf, text, size, x, y, color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, False, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_text1(surf, text, size, x, y, color):
    font = pygame.font.Font(font1, size)
    text_surface = font.render(text, False, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

#a function to be called in main loop when the game ends
def end():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    screen.blit(end_img, (0, 0))
