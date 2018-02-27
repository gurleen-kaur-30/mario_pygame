from os import path
import random

#dimensions
WIDTH = 800
HEIGHT = 600
FPS = 60
BG_COLOR = 51,153,255
TITLE = "Mario (beta)"

#colors
WHITE = 255,255,255
BLACK = 0,0,0
GOLD = 255, 223, 0

img_dir = path.join(path.dirname(__file__),'img')
audio = path.join(path.dirname(__file__), 'snd')


#flames
fire = []

#Clouds
clouds = []
for i in range(random.randint(20,80)):
    clouds.append(((random.randint(0,8*WIDTH),random.randint(0,WIDTH/4)),(random.randint(40,150),random.randint(10,80))))

#bricks
bricks=[]
brick_p = []

for i in range(43):
    bricks.append((20*(i),HEIGHT - 20))
    bricks.append(( 20*(i),HEIGHT - 40))
for i in range(50,75):
    bricks.append((20*(i),HEIGHT - 20))
    bricks.append(( 20*(i),HEIGHT - 40))
for i in range(77,78):
    bricks.append((1560 + 20*(i+1), HEIGHT - 20))
    bricks.append((1560 + 20*(i+1), HEIGHT - 40))
for i in range(2):
    bricks.append((1560 + 20*(i+1), HEIGHT - 20))
    bricks.append((1560 + 20*(i+1), HEIGHT - 40))
for i in range(80,88):
    bricks.append((1680 + 20*(i+1), HEIGHT - 20))
    bricks.append((1680 + 20*(i+1), HEIGHT - 40))

for i in range(2):
    bricks.append((1680 + 20*(i+1), HEIGHT - 20))
    bricks.append((1680 + 20*(i+1), HEIGHT - 40))
for i in range(49):
    bricks.append((1800 + 20*(i+1),HEIGHT - 20))
    bricks.append((1800 + 20*(i+1),HEIGHT - 40))

for i in range(15):
    bricks.append((2900+20*(i+1),HEIGHT - 20))
    bricks.append((2900+20*(i+1),HEIGHT - 40))

for i in range(6):
    bricks.append((3520+20*(i+1),HEIGHT - 160))
    bricks.append((3520+20*(i+1),HEIGHT - 180))

for i in range(100):
    bricks.append((3780+20*(i+1),HEIGHT - 20))
    bricks.append((3780+20*(i+1),HEIGHT - 40))

#skyforms
for i in range(7):
    brick_p.append((400+20*(i+1),HEIGHT - 160))
    brick_p.append((400+20*(i+1),HEIGHT - 180))

    #pyramids
for i in range(7):
    brick_p.append((2640+20*(i+1),HEIGHT - 60))
for i in range(6):
    brick_p.append((2660 + 20*(i+1),HEIGHT - 80))
for i in range(5):
    brick_p.append((2680 + 20*(i+1),HEIGHT - 100))
for i in range(4):
    brick_p.append((2700 + 20*(i+1),HEIGHT - 120))
for i in range(3):
    brick_p.append((2720 + 20*(i+1),HEIGHT - 140))
for i in range(2):
    brick_p.append((2740 + 20*(i+1),HEIGHT - 160))
for i in range(1):
    brick_p.append((2760 + 20*(i+1),HEIGHT - 180))
    #pyramids
for i in range(7):
    brick_p.append((2900+20*(i+1),HEIGHT - 60))
for i in range(6):
    brick_p.append((2900 + 20*(i+1),HEIGHT - 80))
for i in range(5):
    brick_p.append((2900 + 20*(i+1),HEIGHT - 100))
for i in range(4):
    brick_p.append((2900 + 20*(i+1),HEIGHT - 120))
for i in range(3):
    brick_p.append((2900 + 20*(i+1),HEIGHT - 140))
for i in range(2):
    brick_p.append((2900 + 20*(i+1),HEIGHT - 160))
for i in range(1):
    brick_p.append((2900 + 20*(i+1),HEIGHT - 180))

#adding fire everywhere
for i in range(800):
    fire.append((20*(i),HEIGHT - 20))


#pipes
pipe_list = [(800,HEIGHT - 117),(1000,HEIGHT - 117),(1300,HEIGHT - 117),(2000,HEIGHT - 117),(3400,HEIGHT - 117),(3800,HEIGHT - 117)]

#Coins
coinsl=[]
for i in range(50):
	x = random.randrange(200,3900)
	y = random.randrange(2*HEIGHT/3,3*HEIGHT/4)
	coinsl.append((x,y))
