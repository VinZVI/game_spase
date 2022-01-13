import pygame

class Bullet (pygame.sprite.Sprite):
    # создаем свой класс Пули на основе класса sprite
    def __init__(self, screen, gun):
        # создаем пулю в позиции пушки
        super(Bullet, self).__init__() # берем из основного класса sprite -> init
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 250, 12) # создаем спрайт пули и где он появляется
        self.color = 139, 195, 74
        self.speed = 6.5
        self.rect.centerx = gun.rect.centerx # пуля появляется по центру пушки
        self.rect.top = gun.rect.top # пуля появляется в верхней части пушки
        self.y = float(self.rect.y)

    def update(self):
        # перемещение пули вверх
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        # рисуем пулю на экране
        pygame.draw.rect(self.screen, self.color, self.rect)


