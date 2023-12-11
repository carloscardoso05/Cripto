import flet as ft
from componentes import *


def main(page: ft.Page):
    modoCifrar = True
    def mudarModo(novoModoCifrar):
        nonlocal modoCifrar
        global menuDecifrar
        global menuCifrar
        modoCifrar = novoModoCifrar
        menuCifrar.visible = modoCifrar
        menuDecifrar.visible = not modoCifrar
        page.update()

    page.fonts = {
        "MuseoModerno": r"fontes\MuseoModerno-Regular.ttf",
        "Baumans": r"fontes\Baumans-Regular.ttf",
        "Prompt": r"fontes\Prompt-Regular.ttf"
    }

    page.title = "CriptoText"
    page.padding = 0
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.TEAL))
    page.appbar = AppBar(on_selected=mudarModo)
    page.add(menuCifrar)
    page.add(menuDecifrar)
    page.update()


ft.app(target=main)
