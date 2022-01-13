import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores



def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 600)) # создаем графическое окно
    pygame.display.set_caption("Космические защитники") # создаем заголовок
    bg_color = (0, 0, 0) # цвет экрана - черный
    gun = Gun(screen) # добавляем объект пушки
    bullets = Group() # добавляем контейнер с пулями
    inos = Group() # добавляем ино на экран
    controls.create_army(screen, inos) # вызываем функцию с группой пришелцев
    stats = Stats() # экземпляр статистики
    sc = Scores(screen, stats) # создаем экземпляр класса Счет


    # создаем основной цикл игры
    while True:
        controls.events(screen, gun, bullets) # вызываем в главном цикле функцию событий для движения пушки
        if stats.run_game:
            gun.update_gun() # функция обновления движения пушки
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, gun, inos, bullets)



run()