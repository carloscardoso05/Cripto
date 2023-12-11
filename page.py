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
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.TEAL))
    page.appbar = AppBar()
    page.update()


ft.app(target=main)
