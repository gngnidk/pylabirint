from pygame import *

mixer.init()
mixer.music.load("amb.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.2)
winsound = mixer.Sound("winso.ogg")
losesound = mixer.Sound("losezvyk.ogg")
shootsound = mixer.Sound("shoot.ogg")
stepsound = mixer.Sound("stepzvyk.ogg.ogg")
bonussoubd = mixer.Sound("eror.ogg")
tp = mixer.Sound('tp (1).ogg')
#клас-батько для інших спрайтів
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        # Викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)
 
        #кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (size_x, size_y))

        #кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    #метод, що малює героя на вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
        
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
        self.start_x = player_x
        self.start_y = player_y
        
    ''' переміщає персонажа, застосовуючи поточну горизонтальну та вертикальну швидкість'''
    def update(self): 
        
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if platforms_touched:
            tp.play()
            self.rect.x = self.start_x
            self.rect.y = self.start_y
            return
        
        self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if platforms_touched:
            tp.play()
            self.rect.x = self.start_x
            self.rect.y = self.start_y
            return
    

    def fire(self, direction):
        bullet = Bullet('bullet demo.png', self.rect.centerx, self.rect.centery-2, 50, 50, 15, direction)
        shootsound.play()
        bullets.add(bullet)

class Enemy_h(GameSprite):
        side = "left"
        def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, x1, x2):
            # Викликаємо конструктор класу (Sprite):
            GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
            self.speed = player_speed
            self.x1 =x1
            self.x2 =x2

    #рух ворога
        def update(self):
            if self.rect.x <= self.x1: 
                self.side = "right"
            if self.rect.x >= self.x2:
                self.side = "left"
            if self.side == "left":
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed

class Enemy_v(GameSprite):
    side = "up"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, y1, y2):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
        self.y1 =y1
        self.y2 =y2

   #рух ворога
    def update(self):
        if self.rect.y <= self.y1: #w1.wall_x + w1.wall_width
            self.side = "down"
        if self.rect.y >= self.y2:
            self.side = "up"
        if self.side == "up":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

# клас спрайту-кулі
class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed,direction):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = 50
        self.direction = direction
    #рух ворога
    def update(self):
        if self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed         

win_width = 1440
win_height = 780  






window = display.set_mode((win_width, win_height))
display.set_caption("Пространнственная аномалия")
back = transform.scale(image.load("fon.png"), (win_width, win_height))
bonushave = False
bonus = sprite.Group(GameSprite('anompepsilol.png', 1200, 50, 50,100))
bullets = sprite.Group(GameSprite('bullet demo.png', 1100, 450, 60, 20))
monsters = sprite.Group()
barriers = sprite.Group()



w3 = GameSprite('obgg.png', 1100, 450, 50, 350)
w4 = GameSprite('obgg.png', 650, 450, 50, 350)
w2 = GameSprite('obgl.png', 200, 600, 350, 50)
w5 = GameSprite('obgg.png', 200, 300, 50, 350)
w6 = GameSprite('obgg.png', 200, 200, 50, 350)
w7 = GameSprite('obgg.png', 800, 150, 50, 350)
w8 = GameSprite('obgg.png', 800, 650, 50, 350)
w9 = GameSprite('obgl.png', 500, 150, 350, 50)
w13 = GameSprite('obgl.png', 200, 150, 350, 50)


w14 = GameSprite('obgl.png', 500, 150, 350, 50)
w15 = GameSprite('obgl.png', 500, 150, 350, 50)
w16 = GameSprite('obgl.png', 500, 150, 350, 50)





w10 = GameSprite('obgl.png', 900, 400, 350, 50)
w11 = GameSprite('obgl.png', 1200, 200, 350, 50)
w12 = GameSprite('obgl.png', 1000, 200, 350, 50)
w17 = GameSprite('obgl.png', 800, 400, 350, 50)
w18 = GameSprite('obgl.png', 350, 400, 350, 50)
###kraya niz verx|
w19 = GameSprite('obgl.png', 0, -30, 350, 50)
w20 = GameSprite('obgl.png', 350, -30, 350, 50)
w21 = GameSprite('obgl.png', 650, -30, 350, 50)
w22 = GameSprite('obgl.png', 950, -30, 350, 50)
w23 = GameSprite('obgl.png', 1150, -30, 350, 50)
w24 = GameSprite('obgl.png', 350, 750, 350, 50)
w25 = GameSprite('obgl.png', 650, 750, 350, 50)
w26 = GameSprite('obgl.png', 950, 750, 350, 50)
w27 = GameSprite('obgl.png', 1150, 750, 350, 50)
w28 = GameSprite('obgl.png', 0, 750, 350, 50)

###kraya levo pravo

w29 = GameSprite('obgg.png', 0, 650, 50, 350)
w30= GameSprite('obgg.png', 0, 350, 50, 350)
w31= GameSprite('obgg.png', 0, 150, 50, 350)
w32= GameSprite('obgg.png', 0, 850, 50, 350)
w33= GameSprite('obgg.png', 0, 0, 50, 350)
w34= GameSprite('obgg.png', 1400, 650, 50, 350)
w35= GameSprite('obgg.png', 1400, 350, 50, 350)
w36= GameSprite('obgg.png', 1400, 150, 50, 350)
w37 = GameSprite('obgg.png', 1400, 0, 50, 350)







barriers.add(w2)
barriers.add(w3)
barriers.add(w4)
barriers.add(w5)
barriers.add(w6)
barriers.add(w7)
barriers.add(w8)
barriers.add(w9)
barriers.add(w10)
barriers.add(w11)
barriers.add(w12)
barriers.add(w14)
barriers.add(w13)
barriers.add(w15)
barriers.add(w16)
barriers.add(w17)
barriers.add(w18)
barriers.add(w19)
barriers.add(w20)
barriers.add(w21)
barriers.add(w22)
barriers.add(w23)
barriers.add(w24)
barriers.add(w25)
barriers.add(w26)
barriers.add(w27)
barriers.add(w28)
barriers.add(w29)
barriers.add(w30)
barriers.add(w31)
barriers.add(w32)
barriers.add(w33)
barriers.add(w34)
barriers.add(w35)
barriers.add(w36)
barriers.add(w37)
final_sprite = GameSprite('komp.png', 950, 550, 80, 80)
monster = Enemy_h('enemy.png', 1000, 300, 80, 80, 5, 1000, 1300)
monster3 = Enemy_h('enemy.png', 100, 60, 80, 80,7,100,1000)
monster4 = Enemy_v('enemy.png', 100, 650, 80, 80, 5,200, 670)
monster5 = Enemy_h('enemy.png', 450, 250, 80, 80, 5,300,700)
monster6 = Enemy_h('enemy.png', 400, 470, 80, 80,5,300,500)
ggimage = 'gg.png'
gg = Player(ggimage, 1300, 540, 70, 70, 0, 0)

monsters.add(monster)
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster5)
monsters.add(monster6)
run = True
finish = False
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                gg.x_speed = -5
                stepsound.play()
                gg.image = transform.scale(image.load('gg2 (2).png'), (70, 70))

            elif e.key == K_RIGHT:
                gg.x_speed = 5
                stepsound.play()
                gg.image = transform.scale(image.load('gg.png'), (70, 70))
            elif e.key == K_UP :
                gg.y_speed = -5
                stepsound.play()
            elif e.key == K_DOWN :
                gg.y_speed = 5
                stepsound.play()
            ##
            if e.key == K_LEFT and bonushave == True:
                gg.x_speed = -10
                stepsound.play()
            elif e.key == K_RIGHT and bonushave == True:
                gg.x_speed = 10
                stepsound.play()
            elif e.key == K_UP and bonushave == True:
                gg.y_speed = -10
                stepsound.play()
            elif e.key == K_DOWN and bonushave == True:
                gg.y_speed = 10
                stepsound.play()







            elif e.key == K_d:
                    gg.fire('right')
            elif e.key == K_a:
                    gg.fire("left")
            elif e.key == K_s:
                    gg.fire('down')
            elif e.key == K_w:
                    gg.fire("up")                       
 
        elif e.type == KEYUP:
            if e.key == K_LEFT :
                gg.x_speed = 0
            elif e.key == K_RIGHT:
                gg.x_speed = 0
            elif e.key == K_UP:
                gg.y_speed = 0
            elif e.key == K_DOWN:
                gg.y_speed = 0
    if not finish:
        window.blit(back, (0, 0))
        
        gg.update()  
        bullets.update()
        gg.reset() 
        bullets.draw(window)
        barriers.draw(window)
        monsters.draw(window)
        final_sprite.reset()
        sprite.groupcollide(monsters, bullets, True, True)
        monsters.update()
        monsters.draw(window)
        sprite.groupcollide(bullets, barriers, True, False)
        bonus.draw(window)
        
        if sprite.spritecollide(gg, bonus, True):
            bonushave = True
            bonussoubd.play()
            


        
        if sprite.spritecollide(gg, monsters, False):
            finish = True
            mixer.music.stop()
            losesound.play()
            img = image.load('lose.png')
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
        if sprite.collide_rect(gg, final_sprite):
            
            finish = True
            mixer.music.stop()
            winsound.play()
            img = image.load('final.png')
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
                 
    time.delay(20)
    display.update()