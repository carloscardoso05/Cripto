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


def AppBar():
    titulo = ft.Text(
        "CriptoText",
        size=64,
        text_align="start",
        font_family="MuseoModerno",
        color="#87E178",
        weight=ft.FontWeight.BOLD,
        italic=True,
    )

    def BotaoCifrar():
        return ft.ElevatedButton(
            content = ft.Text("Cifrar", font_family="Baumans", size=25),
            height=50,
            width=165,
            style=ft.ButtonStyle(
                color=ft.colors.BLACK,
                bgcolor="#85C7B3",
                shadow_color=ft.colors.BLACK12,
            ),
        )

    def BotaoDecifrar():
        return ft.ElevatedButton(
            content = ft.Text("Decifrar", font_family="Baumans", size=25),
            height=50,
            width=165,
            style=ft.ButtonStyle(
                color="#797373",
                bgcolor=ft.colors.TRANSPARENT,
                shadow_color=ft.colors.BLACK12,
            )
        )

    return ft.AppBar(
        title=titulo,
        center_title=False,
        toolbar_height=160,
        bgcolor='#F4F4F4',
        actions=[
                ft.Container(
                    ft.Row(
                        [BotaoCifrar(), BotaoDecifrar()],
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
