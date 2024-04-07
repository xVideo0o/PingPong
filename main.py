from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Ball(GameSprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__(img, x, y, w, h, speed)
        self.speed_x = 0
        self.speed_y = 0
    
    def set_direction(self, speed_x, speed_y):
        self.speed_x = 0
        self.speed_y = 0
    def update(self):
        self.rect.x += self.speed_x*self.speed
        self.rect.y += self.speed_y*self.speed

    def check_direction(self, pl1, pl2):
        global point_l, point_r
        if self.rect.y<=0:
            self.speed_y*=-1
        elif self.rect.y >= 500 - self.rect.height:
            self.speed_y*=-1
        elif self.rect.spritecollide(pl1.rect):
            self.speed_x *=-1
        elif self.rect.spritecollide(pl2.rect):
            self.speed_x *=-1

        elif self.rect.x <= 0:
            point_r +=1
            self.rect.x = 700/2-self.rect.width/2
            self.rect.y = 500/2-self.rect.hidth/2

        elif self.rect.x >=  500 - self.rect.width:
            point_l +=1
            self.rect.x = 700/2-self.rect.width/2
            self.rect.y = 700/2-self.rect.width/2


point_l = 0
point_r = 0

direction = []
ball = Ball('Player.png', 700/2-self.rect.width/2, 700/2-self.rect.width/2, 50, 50, 10)
# ball.set.direction

window = display.set_mode((700, 500))
display.set_caption('ПингПонг')
background = transform.scale(image.load('fon.png'), (700, 500))

clock = time.Clock()
FPS = 100

game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False



    display.update()
    clock.tick(FPS)