import pygame as pg
from src.utils import get_decimal_from_dms, get_dms_from_decimal

class Earth:
    def __init__(self):
        self.image = pg.image.load("assets/earth.jpg")
        self.rect = pg.Rect((0, 0), (1400, 700))

        self.selection_start_position = None
        self.selection_end_position = None
        self.selecting = False

    def _zoom(self):
        """
        Zooms on the selected area
        """
        pass

    def draw(self, window):
        window.blit(pg.transform.scale(self.image, (1400, 700)), (0, 0))
        if self.selecting:
            pg.draw.rect(
                window,
                (255, 255, 255),
                pg.Rect(
                    self.selection_start_position,
                    (
                        pg.mouse.get_pos()[0] - self.selection_start_position[0],
                        pg.mouse.get_pos()[1] - self.selection_start_position[1]
                    )
                ),
                1
            )

    def get_coord_from_mouse(self, mouse_pos):
        return (
            180 - (mouse_pos[0] / 1400 * 360),
            90 - (mouse_pos[1] / 700 * 180)
        )

    def OnEvent(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.selecting = True
            self.selection_start_position = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.selecting = False
            self.selection_end_position = pg.mouse.get_pos()
            self._zoom()

        if event.type == pg.MOUSEMOTION:
            coord = self.get_coord_from_mouse(pg.mouse.get_pos())
            current_coord = (
                "{}d{}m{}s".format(*get_dms_from_decimal(coord[0])),
                "{}d{}m{}s".format(*get_dms_from_decimal(coord[1]))
            )
            print(f"Current coord: {current_coord}")

