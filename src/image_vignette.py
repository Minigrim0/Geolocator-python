import pygame as pg
import os


class ImageVignette:
    def __init__(self, path):
        self.path = path
        self.filename = os.path.basename(path)

        self.image = pg.Surface((500, 150))

        self.rect = self.image.get_rect()

        self._load()

    def _load(self):
        image = pg.image.load(self.path)
        image = pg.transform.scale(image, (200, 150))
        filename_image = pg.font.SysFont("Arial", 20).render(self.filename, True, (255, 255, 255))

        self.image.blit(image, (0, 0))
        self.image.blit(filename_image, (200, 75 - filename_image.get_height() / 2))

    def draw(self, window, position: tuple):
        window.blit(self.image, position)