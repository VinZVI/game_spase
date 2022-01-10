import pygame, controls
from gun import Gun
from pygame.sprite import Group

def run():

    pygame.init()
    screen = pygame.display.set_mode((500, 600)) # создаем графическое окно
    pygame.display.set_caption("Космические защитники") # создаем заголовок
    bg_color = (0, 0, 0) # цвет экрана - черный
    gun = Gun(screen) # добавляем объект пушки
    bullets = Group() # добавляем контейнер с пулями

    # создаем основной цикл игры
    while True:
        controls.events(screen, gun, bullets) # вызываем в главном цикле функцию событий для движения пушки
        gun.update_gun() # функция обновления движения пушки
        controls.update(bg_color, screen, gun, bullets)
        controls.update_bullets(bullets)



run()