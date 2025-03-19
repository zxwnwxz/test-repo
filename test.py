# Идея - Сделать космо-корабль, который пытаеться улететь из ( куда-то ) в ( куда-то ), по пути него должны быть враги ( Другие корабли ).

from pygame import *
from random import *

# Классы
#-----------                                                   ------------                                    -------------
# Класс спрайт ( ОЧЕНЬ ВАЖНО )

class GameSprite(sprite.Sprite):
    def __init__(self, filename, x, y, speed, width, height):
        super().__init__()
        
        self.image = transform.scale(image.load(filename), (width, height))
        self.speed = speed

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
         window.blit(self.image, (self.rect.x, self.rect.y))




class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w]and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s]and self.rect.y < height - self.image.get_height():
            self.rect.y += self.speed
        if key_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < width - self.image.get_width():
            self.rect.x += self.speed

class UFO(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > height:
            lost += 1
            self.rect.y = randint(-100, -50)
            self.rect.x = randint(0, width - self.image.get_width())

class UFO2(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > height:
            lost += 1
            self.rect.y = randint(-100, -50)
            self.rect.x = randint(0, width - self.image.get_width())






#создай окно игры'

width = 800
height = 700

window = display.set_mode((width, height))
display.set_caption('Arcade flight-Space')
background = transform.scale(image.load('3F3F3F.png'), (width, height))

clock = time.Clock()
FPS = 60

font.init()
font1 = font.Font(None, 72)
font2 = font.Font(None, 34)
win_text = font1.render('Как ты прошёл это?', True, (0, 128, 0))
lose_text = font1.render('Ты проиграл.', True, (128, 0, 0))


lost = 0

player = Player('Space_shuttle.png', 300, 400, 5, 75, 100)



monsters = sprite.Group()
for i in range(8):
    ufo = UFO('Meteor.png', randint(0, 450), randint(-100, -50), 3, 40, 100 )
    monsters.add(ufo)

onsters = sprite.Group()
for i in range(2):
    ufo2 = UFO2('png.png', randint(0, 450), randint(-100, -50), 3, 140, 100 )
    onsters.add(ufo2)


#---------------------------------------------------------------------------------------

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.blit(background, (0, 0))
        player.reset()
        player.update()
        monsters.update()
        monsters.draw(window)


        lost_text = font2.render('Твой рекорд: ' + str(lost) + ' км.', True, (255, 255, 255))
        window.blit(lost_text, (10, 10))
            

        if sprite.spritecollide(player, monsters, False) or sprite.spritecollide(player, onsters, False):
            window.blit(lose_text, (230, 200))
            finish = True

        if lost >= 100000:
            window.blit(win_text, (350, 200))
            finish = True

        if lost >= 40:
            onsters.update()
            onsters.draw(window)


    display.update()
    clock.tick(FPS)




# #Создай собственный Шутер!

# from pygame import *
# from random import *

# class GameSprite(sprite.Sprite):
#     def __init__(self, filename, x, y, speed, width, height):
#         super().__init__()
        
#         self.image = transform.scale(image.load(filename), (width, height))
#         self.speed = speed

#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
    
#     def reset(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))

# class Player(GameSprite):
#     def update(self):
#         key_pressed = key.get_pressed()
#         if key_pressed[K_w]and self.rect.y > 0:
#             self.rect.y -= self.speed
#         if key_pressed[K_s]and self.rect.y < height - self.image.get_height():
#             self.rect.y += self.speed
#         if key_pressed[K_a] and self.rect.x > 0:
#             self.rect.x -= self.speed
#         if key_pressed[K_d] and self.rect.x < width - self.image.get_width():
#             self.rect.x += self.speed
#     def fire(self):
#         bullet = Bullet('bullet.png', self.rect.centerx -6, self.rect.y, 15, 15, 20)
#         bullets.add(bullet)


# class UFO(GameSprite):
#     def update(self):
#         global lost
#         self.rect.y += self.speed
#         if self.rect.y > height:
#             lost += 1
#             self.rect.y = randint(-100, -50)
#             self.rect.x = randint(0, width - self.image.get_width())

# class Bullet(GameSprite):
#     def update(self):
#         self.rect.y -= self.speed
#         if self.rect.y < 0:
#             self.kill()

# #создай окно игры'

# width = 700
# height = 500

# window = display.set_mode((width, height))
# display.set_caption('Space')
# background = transform.scale(image.load('galaxy.jpg'), (width, height))

# clock = time.Clock()
# FPS = 60

# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()


# font.init()
# font1 = font.Font(None, 72)
# font2 = font.Font(None, 24)
# win_text = font1.render('You win', True, (0, 128, 0))
# lose_text = font1.render('You lose', True, (128, 0, 0))


# score = 0
# lost = 0



# player = Player('rocket.png', 300, 400, 5, 75, 100)

# bullets = sprite.Group()
# monsters = sprite.Group()
# for i in range(5):
#     ufo = UFO('ufo.png', randint(0, 450), randint(-100, -50), 3, 50, 50 )
#     monsters.add(ufo)

# #Игровой цикл
# #---------------------------------------------------------------------------------------

# game = True
# finish = False
# while game:
#     for e in event.get():
#         if e.type == QUIT:
#             game = False
#         if e.type == KEYDOWN:
#             if e.key == K_SPACE:
#                 player.fire()
        
#     if finish != True:
#         window.blit(background, (0, 0))
#         player.reset()
#         player.update()
#         bullets.update()
#         bullets.draw(window)
#         monsters.update()
#         monsters.draw(window)

#         score_text = font2.render('Счёт: ' + str(score), True, (255, 255, 255))
#         lost_text = font2.render('Пропущенно: ' + str(lost), True, (255, 255, 255))
#         window.blit(score_text, (10, 10))
#         window.blit(lost_text, (10, 40))

#         #player.fire()

#         collides = sprite.groupcollide(monsters, bullets, True, True)
#         for c in collides:
#             score += 1
#             ufo = UFO('ufo.png', randint(0, 450), randint(-100, -50), 3, 50, 50 )
#             monsters.add(ufo)
            

        

#         if sprite.spritecollide(player, monsters, False) or lost >= 3:
#             window.blit(lose_text, (300, 200))
#             finish = True
            

#         if score >= 10:
#             window.blit(win_text, (350, 200))
#             finish = True

        

#     display.update()
#     clock.tick(FPS)

# class Wall(sprite.Sprite):
#     def __init__(self, r, g, b, x, y, w, h ):
#         super().__init__()
#         self.r = r
#         self.g = g
#         self.b = b
#         self.w = w
#         self.h = h 

#         self.image = Surface((w, h))
#         self.image.fill((r, g, b))
    
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y

#     def draw_wall(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))
