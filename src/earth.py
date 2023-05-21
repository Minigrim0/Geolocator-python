import pygame as pg
from src.utils import get_decimal_from_dms, get_dms_from_decimal

class Earth:
    def __init__(self):
        self.image = pg.image.load("assets/earth.jpg")
        self.rect = pg.Rect((0, 0), (1400, 700))

    def draw(self, window):
        window.blit(pg.transform.scale(self.image, (1400, 700)), (0, 0))

    def get_coord_from_mouse(self, mouse_pos):
        return (
            180 - (mouse_pos[0] / 1400 * 360),
            90 - (mouse_pos[1] / 700 * 180)
        )

    def OnEvent(self, event):
        if event.type == pg.MOUSEMOTION:
            coord = self.get_coord_from_mouse(pg.mouse.get_pos())
            current_coord = (
                "{}d{}m{}s".format(*get_dms_from_decimal(coord[0])),
                "{}d{}m{}s".format(*get_dms_from_decimal(coord[1]))
            )
            print(f"Current coord: {current_coord}")
