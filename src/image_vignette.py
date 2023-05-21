import pygame as pg
import piexif
from PIL import Image

import os


class ImageVignette:
    def __init__(self, path):
        self.path = path
        self.filename = os.path.basename(path)
        self.image = pg.Surface((500, 150))
        self.rect = pg.Rect((0, 0), (500, 150))
        self.selected = False
        self.coord = "Unknown"

        self._load()

    def _load(self):
        img = Image.open(self.path)
        if img.info.get('exif', None) is not None:
            exif_dict = piexif.load(img.info['exif'])
            if exif_dict.get('GPS', None) is not None:
                self.coord = exif_dict['GPS']

        image = pg.image.load(self.path)
        image = pg.transform.scale(image, (200, 150))
        filename_image = pg.font.SysFont("Arial", 20).render(self.filename, True, (255, 255, 255))
        coord_image = pg.font.SysFont("Arial", 15).render(f"Coordinates: {str(self.coord)}", True, (255, 255, 255))

        self.image.blit(image, (0, 0))
        self.image.blit(filename_image, (210, 75 - filename_image.get_height() / 2))
        self.image.blit(coord_image, (210, 75 + coord_image.get_height() / 2))

    def draw(self, window, position: tuple):
        self.rect.topleft = position
        window.blit(self.image, position)
        if self.selected:
            pg.draw.rect(window, (255, 100, 100), self.rect, 1)
        else:
            pg.draw.rect(window, (255, 255, 255), self.rect, 1)
