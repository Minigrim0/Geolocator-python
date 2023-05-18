import pygame as pg

from src.main_menu import MainMenu

pg.init()

window = pg.display.set_mode((1920, 1080))
pg.display.set_caption("GeoLocator")

menu = MainMenu()
menu(window)
