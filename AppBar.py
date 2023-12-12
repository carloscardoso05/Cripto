import flet as ft

def AppBar(on_selected):
    modoCifrar = True
    titulo = ft.Text(
        "CriptoText",
        size=64,
        text_align="start",
        font_family="MuseoModerno",
        color=ft.colors.TEAL,
        weight=ft.FontWeight.BOLD,
        italic=True,
    )

    botaoCifrar = ft.ElevatedButton(
        content=ft.Text("Cifrar", font_family="Baumans", size=25),
        height=50,
        width=165,
        bgcolor=ft.colors.TEAL_100,
        data=True
    )

    botaoDecifrar = ft.ElevatedButton(
        content=ft.Text("Decifrar", font_family="Baumans", size=25),
        height=50,
        width=165,
        bgcolor=ft.colors.TRANSPARENT,
        data=False
    )

    def mudarModo(e: ft.ControlEvent):
        nonlocal modoCifrar
        modoCifrar = e.control.data
        botaoCifrar.bgcolor = ft.colors.TEAL_100 if modoCifrar else ft.colors.TRANSPARENT
        botaoDecifrar.bgcolor = ft.colors.TEAL_100 if not modoCifrar else ft.colors.TRANSPARENT
        on_selected(modoCifrar)
        e.page.update()

    botaoCifrar.on_click = mudarModo
    botaoDecifrar.on_click = mudarModo

    return ft.AppBar(
        title=titulo,
        center_title=False,
        toolbar_height=120,
        actions=[
            ft.Container(
                ft.Row(
                    [botaoCifrar, botaoDecifrar],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                ),
                bgcolor="#D9D9D9",
                border_radius=40,
                height=76,
                width=385,
                margin=20,
            )
        ],
    )