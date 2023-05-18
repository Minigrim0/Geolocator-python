import pygame as pg


class Runnable:
    def __init__(self):
        self.running = False
        self.window = None

    def run(self, window):
        self.window = window
        self.running = True
        self.pre_load()

        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                else:
                    self.update(event)

            window.fill((0, 0, 0))
            self.draw()
            pg.display.update()
        pg.quit()
        quit()

    def pre_load(self):
        """
        Called just before entering the loop
        """

    def __call__(self, window):
        self.run(window)

    def quit(self):
        self.running = False

    def update(self, event):
        raise NotImplementedError

    def draw(self, window):
        raise NotImplementedError