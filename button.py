import pygame as pg


class Button:
    def __init__(
            self,
            position: tuple,
            size: tuple,
            text: str,
            color: tuple,
            font: pg.font.Font,
            font_size: int,
            callback: callable = None
        ):
        self.position = position
        self.size = size
        self.text = text
        self.color = color
        self.font = font
        self.font_size = font_size

        self.image = pg.Surface(self.size)
        self.hovered_image = pg.Surface(self.size)
        self.clicked_image = pg.Surface(self.size)
        self.rect = self.image.get_rect()

        self.callback = callback
        self.hovered = False
        self.clicked = False

        self._load()

    def set_callback(self, callback: callable) -> None:
        self.callback = callback

    def _load(self) -> None:
        self.image.fill(self.color)
        self.hovered_image.fill((self.color[0] - 50, self.color[1] - 50, self.color[2] - 50))
        self.clicked_image.fill((self.color[0] - 100, self.color[1] - 100, self.color[2] - 100))
        self.rect.topleft = self.position

    def _draw_text(self, window) -> None:
        text = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        window.blit(text, text_rect)

    def draw(self, window) -> None:
        if self.clicked:
            window.blit(self.clicked_image, self.rect)
        elif self.hovered:
            window.blit(self.hovered_image, self.rect)
        else:
            window.blit(self.image, self.rect)
        self._draw_text(window)

    def update(self, event) -> bool:
        """
        Handles the given event.

        Args:
            event (pg.Event): The event to handle

        Returns:
            bool: True if the event was processed, False otherwise
        """

        self.clicked = False
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if event.type == pg.MOUSEBUTTONDOWN:
                self.clicked = True
            elif event.type == pg.MOUSEBUTTONUP:
                if self.callback is not None:
                    self.callback()
                return True

            self.hovered = True
        else:
            self.hovered = False

        return False
