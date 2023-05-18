import pygame as pg


def update_loading_image(text_template: str, percent: float) -> pg.Surface:
    loading_text = text_template.format(percent)
    return pg.font.SysFont("Arial", 20).render(loading_text, True, (255, 255, 255))

def loading_screen(elements: list, window):
    percent_done = 0
    loading_text = "Loading {}%"

    for index, element in enumerate(elements):
        percent_done = int(index / len(elements) * 100)
        image = update_loading_image(loading_text, percent_done)

        window.fill((0, 0, 0))
        window.blit(image, (window.get_width() / 2 - image.get_width() / 2, window.get_height() / 2 - image.get_height() / 2))
        pg.display.update()
        yield element