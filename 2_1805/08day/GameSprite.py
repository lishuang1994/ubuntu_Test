
#背景精灵
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)
class GameSprite(pygame.sprite.Sprite):#父类
    def __init__(self,image,speed=1):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self):
        self.rect.y +=self.speed
class BackGroundSprite(GameSprite):
    def __init__(self,is_alt=False):
        imagename = "./images/background.png"
        super().__init__(imagename,100)
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        super().update()#调用父类
        #把移除屏幕的背景放到屏幕上方
        if self.rect.y >= SCRRN_RECT.height:
            self.rect.y = -self.rect.height
