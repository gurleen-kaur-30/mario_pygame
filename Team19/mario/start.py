from settings import *
import pygame
import time
from os import path

#inits
pygame.init()
pygame.mixer.init()

#initializations
img_dir = path.join(path.dirname(__file__), 'img')

#displays start window
screen = pygame.display.set_mode((WIDTH,HEIGHT))

st_img = pygame.image.load("bck.jpg").convert()
st_img = pygame.transform.scale(st_img, (WIDTH, HEIGHT))

#blits for the background
screen.blit(st_img,(0,0))

#loading images
c_img = pygame.image.load(path.join(img_dir, "box.png"))
h_img = pygame.image.load(path.join(img_dir, "mk.png"))
stg_img = pygame.image.load(path.join(img_dir, "stg.png"))

#sprites
all_sprites_in_start = pygame.sprite.Group()

#class to set background
class Bck(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(st_img,(WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT

#class to display the box
class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(c_img, (50, 50))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.bottom = self.y

#class
class Hdr(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(h_img, (1500, 300))
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.bottom = 200

#class to display text
class Button(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.img = img
        self.image = pygame.transform.scale(self.img, (350, 150))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2 + 50
        self.rect.bottom = HEIGHT/2 + 30

#defining objects and locations
box1 = Box(WIDTH/2 - 170, HEIGHT/2)
hdr = Hdr()
b1 = Button(stg_img)

#adding sprites to the list
all_sprites_in_start.add(box1)
all_sprites_in_start.add(hdr)
all_sprites_in_start.add(b1)

#a function needed to call the start screen
def start():

    screen.fill(BLACK)
    screen.blit(st_img,(0,0))
    all_sprites_in_start.draw(screen)
    all_sprites_in_start.update()
    pygame.display.update()
