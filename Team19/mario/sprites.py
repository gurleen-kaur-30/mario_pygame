#imports
import pygame as pg
from settings import *
#using vectora
vec = pg.math.Vector2

#player class
class Player(pg.sprite.Sprite):

    def __init__(self,game):
        #initializing variables and attributes
        pg.sprite.Sprite.__init__(self)
        self.char = pg.image.load(path.join(img_dir, "right_stand.png")).convert()
        self.image = pg.transform.scale(self.char,(35,45))
        self.game=game
        self.rect = self.image.get_rect()
        self.rect.center = (10,HEIGHT - 10)
        self.pos = vec(WIDTH/8,HEIGHT - 40) #position
        self.vx = 0
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def jump(self):
        #defining jump
        self.rect.x += 2
        #player can jump if only it is on platform
        hits = pg.sprite.spritecollide(self,self.game.platforms,False)
        self.rect.x -= 2
        if hits:
            self.vel.y = -15
        self.rect.x += 2
        hitp = pg.sprite.spritecollide(self,self.game.pipes,False)
        self.rect.x -= 2
        if hitp:
            self.vel.y = -15

    def update(self):
        #updating the player for the action
        self.acc = vec(0,0.7)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]: #left key action
            self.char = pg.image.load(path.join(img_dir, "left_jump.png")).convert()
            self.image = pg.transform.scale(self.char,(35,45))
            self.rect = self.image.get_rect()
            self.vel.x = -3
            self.pos.x += self.vel.x
            self.char = pg.image.load(path.join(img_dir, "left_stand.png")).convert()
            self.image = pg.transform.scale(self.char,(35,45))
            self.rect = self.image.get_rect()

        if keys[pg.K_RIGHT]:
            self.char = pg.image.load(path.join(img_dir, "right_jump.png")).convert()
            self.image = pg.transform.scale(self.char,(35,45))
            self.rect = self.image.get_rect()
            self.vel.x = 3
            self.pos.x += self.vel.x
            self.char = pg.image.load(path.join(img_dir, "right_stand.png")).convert()
            self.image = pg.transform.scale(self.char,(35,45))
            self.rect = self.image.get_rect()

        #moving our character foward or backward with simple arthematics
        self.vel += self.acc
        self.pos.y += self.vel.y + 0.5*self.acc.y
        #so that the player doesn't end up outside the screen
        if self.pos.x > WIDTH-10:
            self.pos.x = WIDTH-10
        if self.pos.x < 10:
            self.pos.x = 10

        self.rect.midbottom = self.pos

        #if the position of player is below the platform
        if self.pos.y >= HEIGHT-20:
                    self.game.show_end_screen

#class for platforms
class Platform(pg.sprite.Sprite):
    def __init__(self,(x,y)):
        #initializing all bricks that act as platforms
        pg.sprite.Sprite.__init__(self)
        self.base = pg.image.load(path.join(img_dir, "brick.png")).convert()
        self.image = pg.transform.scale(self.base,(20,20))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#class for Pipes
class Pipes(pg.sprite.Sprite):
    def __init__(self,(x,y)):
        #initializing all the pipes
        pg.sprite.Sprite.__init__(self)
        self.pipe = pg.image.load(path.join(img_dir, "pipe.png")).convert()
        self.image = pg.transform.scale(self.pipe,(60,100))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#class for clouds that needs to be scrolled
class Clouds(pg.sprite.Sprite):
    def __init__(self,(x,y),(w,h)):
        pg.sprite.Sprite.__init__(self)
        self.pipe = pg.image.load(path.join(img_dir, "clouds.png")).convert()
        self.image = pg.transform.scale(self.pipe,(w,h))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#Flag in the end to mark the end of game
class Flag(pg.sprite.Sprite):
    def __init__(self,(x,y)):
        pg.sprite.Sprite.__init__(self)
        self.pipe = pg.image.load(path.join(img_dir, "flag.png")).convert()
        self.image = pg.transform.scale(self.pipe,(100,HEIGHT/2))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#Coins that need to be collected to get some score
class Coins(pg.sprite.Sprite):
    def __init__(self,(x,y)):
        pg.sprite.Sprite.__init__(self)
        self.coin = pg.image.load(path.join(img_dir, "coinz.GIF")).convert()
        self.image = pg.transform.scale(self.coin,(50,40))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

'''
#ghosts which kill the player if in contact
class Ghosts(pg.sprite.Sprite):
    def __init__(self,(x,y),dir):
        pg.sprite.Sprite.__init__(self)
        self.char = pg.image.load(path.join(img_dir, "gastly_left.png")).convert()
        self.image = pg.transform.scale(self.char,(50,50))
        #self.image = pg.Surface((30,40))
        #self.image.fill((255,255,0)) #yellow
        self.rect = self.image.get_rect()
        self.pos = vec(x,y) #position
        self.vx = 0
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def update(self):
        if dir == 1:
            self.char = pg.image.load(path.join(img_dir, "gastly_left.png")).convert()
            self.image = pg.transform.scale(self.char,(50,50))
            self.rect = self.image.get_rect()
            self.vel.x = -4
            self.pos.x += self.vel.x

        if dir == 0:
            self.char = pg.image.load(path.join(img_dir, "gastly_right.png")).convert()
            self.image = pg.transform.scale(self.char,(50,50))
            self.rect = self.image.get_rect()
            self.vel.x = 4
            self.pos.x += self.vel.x

        self.vel += self.acc
'''

#fire in the gaps that indicate killing of the player when touch
class Fire(pg.sprite.Sprite):
    def __init__(self,(x,y)):
        pg.sprite.Sprite.__init__(self)
        self.pipe = pg.image.load(path.join(img_dir, "fire.jpg")).convert()
        self.image = pg.transform.scale(self.pipe,(20,20))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
