import flet as ft
from componentes import *


def main(page: ft.Page):
    page.fonts = {
        "MuseoModerno": r"fontes\MuseoModerno-Regular.ttf",
        "Baumans": r"fontes\Baumans-Regular.ttf",
        "Prompt": r"fontes\Prompt-Regular.ttf"
    }

    page.title = "CriptoText"
    page.padding = 0
    page.bgcolor = "#688787"
    page.appbar = AppBar()
    page.update()


ft.app(target=main)
