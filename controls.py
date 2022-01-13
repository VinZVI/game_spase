import pygame, sys
from bullet import Bullet
from ino import Ino
import time


def events(screen, gun, bullets):
    # отработка событий
    for event in pygame.event.get():  # перебираем все события пользователя
        if event.type == pygame.QUIT:  # закрытие окна
            sys.exit()

        elif event.type == pygame.KEYDOWN: # определяем нажатую клавишу
            # вправо
            if event.key == pygame.K_d: # определяем клавишу d для движения вправо
                gun.mright = True

            # влево
            elif event.key == pygame.K_a:  # определяем клавишу а для движения влево
                gun.mleft = True

            # клавиша пробел
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP: # определяем отжатую клавишу
            # вправо
            if event.key == pygame.K_d:
                gun.mright = False
            # влево
            elif event.key == pygame.K_a:
                gun.mleft = False


def update(bg_color, screen, stats, sc, gun, inos, bullets):
    # обновление экрана
    screen.fill(bg_color)  # заливка окна фоновым цветом
    sc.show_score()
    for bullet in bullets.sprites(): # прорисовкка пуль
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()  # прорисовка последнего экрана

def update_bullets(screen, stats, sc, inos, bullets):
    # обновляет позицию пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0: # удаляет пулю после достижения верха экрана
           bullets.remove(bullet)
    colisions = pygame.sprite.groupcollide(bullets, inos, True, True) # проверяет на колизии объекты пришельца и пули, оба удаляются
    if colisions:
        for inos in colisions.values():
            stats.score += 10 * len(inos)
        sc.image_score()
        chec_high_score(stats, sc)
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)


def gun_kill(stats, screen, gun, inos, bullets):
    """столкновение пушки и армии"""
    if stats.guns_left > 0:
        stats.guns_left -=1
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def update_inos(stats, screen, gun, inos, bullets):
    """обновляет позицию инопланетян"""
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos): # при пересечении ино пушки выведется сообщение
        gun_kill(stats, screen, gun, inos, bullets)
    inos_check(stats, screen, gun, inos, bullets)


def inos_check (stats, screen, gun, inos, bullets):
    """проверка до края экрана армии"""
    screen_rect = screen.get_rect()
    for ino in inos.sprites ():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, inos, bullets)
            break

def create_army(screen, inos):
    """создаем армию пришельцев"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width) # считаем сколько пришельцев поместится на экран
    ino_heigth = ino.rect.height # ширина одного пришельца
    number_ino_y = int((600 - 100 - 2 * ino_heigth) / ino_heigth)  # считаем сколько пришельцев поместится на экран

    for raw_number in range(number_ino_y - 1):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number # создаем по оси х пришельцев
            ino.y = ino_heigth + ino_heigth * raw_number # создаем ряды пришельцев
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * raw_number
            inos.add(ino)


def chec_high_score(stats, sc):
    """проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))


