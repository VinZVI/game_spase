import pygame
from pygame.sprite import Sprite

class Gun(Sprite):

    def __init__(self, screen):
        # инициализация пушки
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/pixil-frame-0.png') # подгружаем картинку
        self.rect = self.image.get_rect() # представляем картинку как прямоугольник
        self.screen_rect = screen.get_rect() # передставили экран ка прямоугольник
        self.rect.centerx = self.screen_rect.centerx # координаты "х" центра пушки равны координаты "х" центра экрана
        self.center = float(self.rect.centerx) # переабразуем в вещественное число
        self.rect.bottom = self.screen_rect.bottom # положение нижней координаты
        self.mright = False # флаг для движения в право
        self.mleft = False # флаг для движения в плево

    def output (self):
        # отрисовка пушки
        self.screen.blit(self.image, self.rect) # метод blit отрисовывает изображение пушки на экране

    def update_gun(self):
        # обновление позиции пушки для движении вправо
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5

        # обновление позиции пушки для движении влево
        if self.mleft and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def  create_gun(self):
        """размечает пушку по центру"""
        self.center = self.screen_rect.centerx
