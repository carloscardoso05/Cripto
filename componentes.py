import flet as ft


def BotaoSelecionarArquivos(page: ft.Page, on_selected=None, extensoes_permitidas: list[str] | None = None):
    """Botão que abre um diálogo para selecionar arquivos

    Args:
        page (ft.Page): Página do flet
        on_selected (opcional): Função para ser executada quando o usuário selecionar os arquivos. Recebe como argumento uma lista com os caminhos dos arquivos selecionados ou uma lista vazia se nenhum for selecionado.
        extensoes_permitidas (list[str] | None, opcional): Lista das extensões permitidas, None se todas forem. Padrão é None.
    """

    def pick_files_result(e: ft.FilePickerResultEvent):
        caminhos = list(map(lambda f: f.path, e.files)) if e.files else []
        on_selected(caminhos)

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)

    page.overlay.append(pick_files_dialog)

    return ft.ElevatedButton(
        "Selecionar Arquivos",
        icon=ft.icons.FILE_OPEN,
        on_click=lambda _: pick_files_dialog.pick_files(
            allow_multiple=True,
            allowed_extensions=extensoes_permitidas
        )
    )


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
        toolbar_height=160,
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


def inputFraseSenha():
    return ft.Container(
        ft.Column(
            controls=[
                ft.Text("Frase Senha", font_family="Prompt",
                        weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, size=25, color=ft.colors.WHITE),
                ft.TextField(
                    border_radius=ft.border_radius.all(20),
                    bgcolor=ft.colors.WHITE,
                    border_color=ft.colors.TEAL_900,
                    focused_border_width=3
                )
            ]
        ),
        padding=ft.padding.all(20),
        border_radius=25,
        bgcolor=ft.colors.TEAL_700
    )


def inputMensagem():
    return ft.Container(
        ft.Column(
            controls=[
                ft.Text("Mensagem de Texto", font_family="Prompt",
                        weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, size=25, color=ft.colors.WHITE),
                ft.TextField(
                    border_radius=ft.border_radius.all(20),
                    multiline=True,
                    min_lines=5,
                    bgcolor=ft.colors.WHITE,
                    border_color=ft.colors.TEAL_900,
                    focused_border_width=3
                )
            ]
        ),
        padding=ft.padding.all(20),
        border_radius=25,
        bgcolor=ft.colors.TEAL_700
    )


menuCifrar = ft.Container(
    alignment=ft.alignment.center,
    content=ft.Column(
        width=400,
        controls=[
            inputFraseSenha(),
            inputMensagem(),
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        content=ft.Text(
                            "Cifrar",
                            font_family="Baumans"
                        )
                    ),
                    ft.IconButton(icon=ft.icons.UPLOAD_FILE_OUTLINED)
                ]
            ),
        ]
    )
)


menuDecifrar = ft.Container(
    visible=False,
    alignment=ft.alignment.center,
    content=ft.Column(
        width=400,
        controls=[
            inputFraseSenha(),
            inputMensagem(),
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        content=ft.Text(
                            "Decifrar",
                            font_family="Baumans"
                        )
                    ),
                    ft.IconButton(icon=ft.icons.UPLOAD_FILE_OUTLINED)
                ]
            ),
        ]
    )
)
