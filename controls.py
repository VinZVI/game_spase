import pygame, sys
from bullet import Bullet


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


def update(bg_color, screen, gun, bullets):
    # обновление экрана
    screen.fill(bg_color)  # заливка окна фоновым цветом
    for bullet in bullets.sprites(): # прорисовкка пуль
        bullet.draw_bullet()
    gun.output()
    pygame.display.flip()  # прорисовка последнего экрана

def update_bullets(bullets):
    # обновляет позицию пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0: # удаляет пулю после достижения верха экрана
           bullets.remove(bullet)
    #print (len (bullets))