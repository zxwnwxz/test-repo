

from pygame import *
from random import *

#создай окно игры'

width = 1100
height = 600

window = display.set_mode((width, height))
display.set_caption('Flight-Space')
background = transform.scale(image.load('3F3F3F.jpg'), (width, height))

clock = time.Clock()
FPS = 60


#---------------------------------------------------------------------------------------

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.blit(background, (0, 0))

    display.update()
    clock.tick(FPS)
