import pygame as pg

from button import Button
from dialog import browse_button


class MainMenu:
    def __init__(self) -> None:
        self.running = False
        self.buttons = []

        self._load()

    def run(self) -> None:
        self.running = True

        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            pg.display.update()
        pg.quit()
        quit()

    def _load(self) -> None:
        choose_folder_button = Button(
            ((1280 - 150) / 2, (720 / 2) - 75),
            (150, 50),
            "Choose Folder",
            (255, 255, 255), pg.font.SysFont("Arial", 20), 20)
        self.buttons.append(choose_folder_button)

    def update(self, event) -> None:
        for button in self.buttons:
            if button.update(event):
                return

    def draw(self, window) -> None:
        for button in self.buttons:
            button.draw(window)

    def quit(self) -> None:
        self.running = False
