import glob
import pygame as pg

from src.runnable import Runnable
from src.image_vignette import ImageVignette
from src.loading_screen import loading_screen

class ImageList(Runnable):
    def __init__(self, dir):
        super().__init__()
        self.dir = dir
        self.images = []
        self.offset = 0

    def pre_load(self):
        image_list = sorted(glob.glob(self.dir + "/*.jpg"))

        for image_path in loading_screen(image_list, self.window):
            self.images.append(ImageVignette(image_path))

    def update(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.offset += 15
                if self.offset > 0:
                    self.offset = 0
            elif event.button == 5:
                self.offset -= 15
                if self.offset < -len(self.images) * 150 + self.window.get_height():
                    self.offset = -len(self.images) * 150 + self.window.get_height()

    def draw(self):
        for i, image in enumerate(self.images):
            image.draw(self.window, (20, self.offset + i * 150 + 20))
