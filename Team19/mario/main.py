 #pygame imports
import pygame as pg
from settings import *
from sprites import *
from start import *
from end import *
from os import path


#classes
class Game:

    def __init__(self):
        #initialize game window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = False

    def load_sound(self):
        #includes the sound directory and the start Sound
        self.snd_dir = path.join(path.dirname(__file__), 'snd')
        self.start_m = pg.mixer.Sound(path.join(self.snd_dir,"start.wav"))

    def new(self):
        #start a new

        self.score = 0
        #groups!
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.pipes = pg.sprite.Group()
        self.clouds = pg.sprite.Group()
        self.skyforms = pg.sprite.Group()
        self.flags = pg.sprite.Group()
        self.coinss = pg.sprite.Group()
        self.flares = pg.sprite.Group()

        #defining predefined objects
        self.player = Player(self)
        self.f = Flag((4200,HEIGHT/2))

        #adding players
        self.all_sprites.add(self.player)

        #adding flag
        self.flags.add(self.f)

        #adding clouds
        for clo in (clouds):
            self.clouds.add(Clouds(*clo))

        #adding fire
        for i in range(len(fire)):
            self.flares.add(Fire(fire[i]))

        #adding pipes as sprites
        for i in range(len(pipe_list)):
            self.all_sprites.add(Pipes(pipe_list[i]))
            self.pipes.add(Pipes(pipe_list[i]))

        #adding bricks as sprites
        for i in range(len(bricks)):
            self.platforms.add(Platform(bricks[i]))

        #adding skyforms as sprites
        for i in range(len(brick_p)):
            self.skyforms.add(Platform(brick_p[i]))
            self.platforms.add(Platform(brick_p[i]))
            self.pipes.add(Platform(brick_p[i]))

        #adding coins as all_sprites
        for i in range(len(coinsl)):
    	    self.coinss.add(Coins(coinsl[i]))

        self.run()

    def run(self):
        #game loop

        #the method has to be ran for the game to run :P
        self.playing = True
        while self.playing:
            self.draw()
            self.update()
            self.events()
            self.clock.tick(FPS)


    def update(self):
        #loop update
        self.all_sprites.update()
        #self.goos.update()
        #self.g.update()
        #platform collision
        #if the character has some velocity on platform
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player,self.platforms,False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.y < lowest.rect.bottom :
                    self.player.pos.y = lowest.rect.top
                    self.player.vel.y = 0

        #skyform collision

        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player,self.skyforms,False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.y < lowest.rect.bottom :
                    self.player.pos.y = lowest.rect.top
                    self.player.vel.y = 0


        #pipe collision
        if self.player.vel.y > 0 and abs(self.player.vel.x) > 0:
            hitsp = pg.sprite.spritecollide(self.player,self.pipes,False)
            if hitsp:
                if self.player.pos.y < hitsp[0].rect.centery:
                    self.player.pos.y = hitsp[0].rect.top
                    self.player.vel.y = 0
                if self.player.pos.y < hitsp[0].rect.centery and self.player.pos.x < hitsp[0].rect.x:
                    self.player.pos.y = hitsp[0].rect.top
                    self.player.vel.x = 0
                    self.player.vel.y = 0
    	hitsh = pg.sprite.spritecollide(self.player,self.pipes,False)
    	if self.player.vel.x>0 and self.player.pos.y > HEIGHT - 117:

    		if hitsh:
    			if self.player.pos.x > hitsh[0].rect.left :
    				self.player.pos.x = hitsh[0].rect.left
    				self.player.vel.x = 0
    	if self.player.vel.x<0 and self.player.pos.y > HEIGHT - 117:
    		if hitsh:
    			if self.player.pos.x < hitsh[0].rect.right:
    				self.player.pos.x = hitsh[0].rect.right
    				self.player.vel.x = 0

        #coin collision
        hitsc = pg.sprite.spritecollide(self.player,self.coinss,True)
    	if hitsc:
            sounda = pg.mixer.Sound("coins.wav")
            self.score += 10
            sounda.play()

        #flag collision
        hitsf = pg.sprite.spritecollide(self.player,self.flags,True)
    	if hitsf:
            self.show_end_screen()

        #scrolling
        #all the object other the players are moved away from the screen that gives a look like the screen is getting scrolled
        if self.player.rect.right >= WIDTH / 2:
            key = pg.key.get_pressed()
            if key[pg.K_RIGHT]:
                self.player.pos.x -= abs(self.player.vel.x)
                for plat in self.platforms:
                    plat.rect.x -= abs(self.player.vel.x)
                for sky in self.skyforms:
                    sky.rect.x -= abs(self.player.vel.x)
                for flare in self.flares:
                    flare.rect.x -= abs(self.player.vel.x)
                self.f.rect.x -= abs(self.player.vel.x)
                pg.display.flip()
                pg.display.update()
                for tube in self.pipes:
                    tube.rect.x -=abs(self.player.vel.x)
                for clo in self.clouds:
                    clo.rect.x -= abs(self.player.vel.x)
                for coi in self.coinss:
        		    coi.rect.x -=abs(self.player.vel.x)

        if self.player.rect.right <= WIDTH / 4:
            key = pg.key.get_pressed()
            if key[pg.K_LEFT]:
                self.player.pos.x +=max(abs(self.player.vel.x),3)
                for plat in self.platforms:
                    plat.rect.x += abs(self.player.vel.x)
                for sky in self.skyforms:
                    sky.rect.x += abs(self.player.vel.x)
                for flare in self.flares:
                    flare.rect.x += abs(self.player.vel.x)
                self.f.rect.x += abs(self.player.vel.x)
                pg.display.flip()
                pg.display.update()
                for tube in self.pipes:
                    tube.rect.x +=abs(self.player.vel.x)
                for clo in self.clouds:
                    clo.rect.x += abs(self.player.vel.x)
                for coi in self.coinss:
        		    coi.rect.x +=abs(self.player.vel.x)



    def events(self):
        #loop events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()
        if self.player.pos.y >= HEIGHT-20:
                    self.show_end_screen()

        self.draw()

    def draw(self):
        #loop draw
        #draws and blits all required images and characters
        self.screen.fill(BG_COLOR)
        self.screen.blit(self.f.image,self.f.rect)
        for flare in self.flares:
            self.screen.blit(flare.image,flare.rect)
        for clo in self.clouds:
            self.screen.blit(clo.image,clo.rect)
        for tube in self.pipes:
            self.screen.blit(tube.image,tube.rect)
        self.screen.blit(self.player.image,self.player.rect)
        for coi in self.coinss:
    	    self.screen.blit(coi.image,coi.rect)
        for plat in self.platforms:
            self.screen.blit(plat.image,plat.rect)
        for sky in self.skyforms:
            self.screen.blit(sky.image,sky.rect)
        #text
        draw_text(screen, "Score: " + str(self.score), 40, 100, 50, GOLD)
        draw_text1(screen, "  ^ ------ to jump", 20, 100, 100, WHITE)
        draw_text1(screen, "    <   > ------ for directions", 20, 100, 130, WHITE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
        pg.display.update()

    def show_start_screen(self):
        #start show
        #shows the start screen
        start()
        self.start_m.play()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.running = True

            if event.type == pg.QUIT:
                exit()

    def show_end_screen(self):
        #end show
        #shows the end screen when the player dies
        time.sleep(1)
        end()
        draw_text(screen, "Score: " + str(self.score), 50, 400, 300, WHITE)
        pg.display.update()
        #waits for an input from the user about respawning
        i = 1
        while i<6:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.new()
            time.sleep(i)
            i+=1
        #exits if no input is given for 5 seconds
        exit()

#runnning the game :)
g= Game()
g.load_sound()

while True:
    pg.mixer.music.load(path.join(audio,"music.ogg"))
    g.show_start_screen()
    while g.running:
        pg.mixer.music.play(loops=-1)
        g.new()
pg.quit()
