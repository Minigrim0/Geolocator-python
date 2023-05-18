import pygame as pg
from tkinter import filedialog
from tkinter import *

from src.image_list import ImageList
from src.button import Button
from src.runnable import Runnable

class MainMenu(Runnable):
    def __init__(self) -> None:
        super().__init__()
        self.buttons = []
        self.error: str = None
        self.error_image: pg.Surface = None

    # Callbacks
    def _load_directory(self) -> None:
        dirname = filedialog.askdirectory()
        if dirname:
            self.running = False
            ImageList(dirname)(self.window)
        else:
            print("No directory selected")
            self.set_error("No directory selected")

    def pre_load(self) -> None:
        choose_folder_button = Button(
            ((self.window.get_width() - 150) / 2, (self.window.get_height() / 2) - 75),
            (150, 50),
            "Choose Folder",
            (255, 255, 255),
            pg.font.SysFont("Arial", 20),
            20,
            callback=self._load_directory
        )
        quit_button = Button(
            ((self.window.get_width() - 150) / 2, (self.window.get_height() / 2) + 75),
            (150, 50),
            "Quit",
            (255, 100, 100),
            pg.font.SysFont("Arial", 20),
            20,
            callback=self.quit
        )

        self.buttons.append(choose_folder_button)
        self.buttons.append(quit_button)

    def set_error(self, error: str) -> None:
        self.error = error
        if self.error:
            self.error_image = pg.font.SysFont("Arial", 20).render(self.error, True, (255, 0, 0))

    def update(self, event) -> None:
        for button in self.buttons:
            if button.update(event):
                return

    def draw(self) -> None:
        for button in self.buttons:
            button.draw(self.window)

        if self.error:
            self.window.blit(self.error_image, ((self.window.get_width() - self.error_image.get_width()) / 2, (self.window.get_height() / 2) - 25))
