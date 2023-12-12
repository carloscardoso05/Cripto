import flet as ft
from AppBar import AppBar
from MenuCifrarDecifrar import MenuCifrarDecifrar


def main(page: ft.Page):
    menuCifrarDecifrar = MenuCifrarDecifrar(page)

    def mudarModo(modo_cifrar):
        nonlocal menuCifrarDecifrar
        menuCifrarDecifrar.set_modo_cifrar(modo_cifrar)

    page.fonts = {
        "MuseoModerno": r"fontes\MuseoModerno-Regular.ttf",
        "Baumans": r"fontes\Baumans-Regular.ttf",
        "Prompt": r"fontes\Prompt-Regular.ttf"
    }

    page.title = "CriptoText"
    page.scroll = ft.ScrollMode.ALWAYS
    page.padding = ft.padding.only(left=20, right=20, top=10, bottom=30)
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.TEAL))
    page.bgcolor = ft.colors.TEAL_100
    page.appbar = AppBar(on_selected=mudarModo)
    page.add(menuCifrarDecifrar)
    page.update()


ft.app(target=main)
