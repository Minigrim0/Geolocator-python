import pygame as pg

from main_menu import MainMenu

pg.init()

window = pg.display.set_mode((1280, 720))
pg.display.set_caption("GeoLocator")

menu = MainMenu()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        else:
            menu.update(event)

    window.fill((0, 0, 0))
    menu.draw(window)
    pg.display.update()
