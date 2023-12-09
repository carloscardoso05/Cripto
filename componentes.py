import flet as ft

def BotaoSelecionarArquivos(page: ft.Page, on_selected = None, extensoes_permitidas:list[str] | None = None):
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
